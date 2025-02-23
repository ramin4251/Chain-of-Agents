

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate

load_dotenv(dotenv_path=r'.env')
groq_api_key = os.getenv("GROQ_API_KEY")
MODEL_LIST = [
    "gemma2-9b-it",
    "llama-3.3-70b-specdec",
    "deepseek-r1-distill-llama-70b",
    "qwen-2.5-32b",
    "deepseek-r1-distill-qwen-32b",
    "mixtral-8x7b-32768",
]
model_to_use = MODEL_LIST[-1]


def get_current_time(*args, **kwargs):
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")


time_tool = Tool(name="TimeTool", func=get_current_time, description="Provides the current time.")


def convert_to_uppercase(text: str):
    return text.upper()


uppercase_tool = Tool(name="UppercaseTool", func=convert_to_uppercase, description="Converts given text to uppercase.")

llm = ChatGroq(model=model_to_use, api_key=groq_api_key)

time_agent_prompt = PromptTemplate.from_template("""
You are a helpful agent that can get the current time.
You have access to the TimeTool to get the current time.
Your goal is to use the TimeTool to find the current time when asked and return ONLY the time.
Instructions:
1. Think step-by-step about how to answer the question.
2. Decide if you need to use a tool. You MUST use the TimeTool.
3. Use the TimeTool to get the current time.
4. Respond with ONLY the time as the "Final Answer". Do not add any extra words or sentences.
Example Interaction:
User Question: What time is it?
Agent steps:
Thought: I need to get the current time. I will use the TimeTool.
Action: TimeTool
Action Input:  (No input needed for TimeTool)
Observation: 10:30 AM  (Example time)
Thought: I have the current time. Now I can give the final answer.
Final Answer: 10:30 AM
TOOLS:
------
{tools}
Format you MUST use:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action (REQUIRED if you choose Action)
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I am ready to answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
{agent_scratchpad}
""")

uppercase_agent_prompt = PromptTemplate.from_template("""
You are a helpful agent that convert text to uppercase.
You have access to the UppercaseTool. You DO NOT have access to any other tool.
When you receive an input text:
1. Use the UppercaseTool to convert ONLY this extracted text to uppercase.
2. Respond with "Final Answer".

Example Interaction:
Input: uppercase this text: 'hello world' and attach time: 01:30 PM
Agent steps:
Thought: I need to uppercase whole this text.
Action: UppercaseTool
Action Input: hello world 1:30 PM
Observation: HELLO WORLD 1:30 PM
Thought: I have converted the text to uppercase. Now I need to generate "Final Answer".
Final Answer: HELLO WORLD 01:30 PM

TOOLS:
------
{tools}
Format you MUST use:
Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action (REQUIRED if you choose Action)
Observation: the result of the action
... (this Thought/Action/Observation can repeat N times)
Thought: I am ready to answer
Final Answer: the final answer to the original input question
Begin!
Question: {input}
{agent_scratchpad}
""")


agent_1_tools = [time_tool]
agent_1 = create_react_agent(llm=llm, tools=agent_1_tools, prompt=time_agent_prompt)

agent_2_tools = [uppercase_tool]
agent_2 = create_react_agent(llm=llm, tools=agent_2_tools, prompt=uppercase_agent_prompt)


class ChainOfAgents:
    def __init__(self, agents_and_tools):
        self.agents_and_tools = agents_and_tools

    def run(self, input_data):
        current_input = input_data
        for i, (agent, tools) in enumerate(self.agents_and_tools):
            print(f"Running Agent {i + 1}")
            executor = AgentExecutor(agent=agent, tools=tools)
            try:
                result = executor.invoke({"input": input_data + current_input})
                current_input = result['output']
                print(f"Agent {i + 1} Output: {result['output']}\n")
            except Exception as e:
                print(f"Error in Agent {i + 1}: {e}")
                break
        return current_input


chain_of_agents = ChainOfAgents(agents_and_tools=[(agent_1, agent_1_tools), (agent_2, agent_2_tools)])

print(chain_of_agents.run("what is current time? uppercase this text: 'hello there' "))
