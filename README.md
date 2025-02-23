# Langchain Groq Chain of Agents Example

This project demonstrates a simple chain of Langchain agents using Groq's language models. It includes two agents that perform sequential tasks:

1.  **Time Agent:** Gets the current time using a custom `TimeTool`.
2.  **Uppercase Agent:** Converts text to uppercase using a custom `UppercaseTool`.

The agents are orchestrated using the `ChainOfAgents` class, where the output of the first agent becomes part of the input for the second agent. This showcases a basic example of how to chain agents together to perform more complex tasks.

## Prerequisites

*   **Groq API Key:** You need a Groq API key to use Groq's language models. Sign up at [https://console.groq.com/](https://console.groq.com/) to create an account and obtain your API key.
*   **Python 3.7+**
*   **pip** (Python package installer)

## Setup

1.  **Clone the repository:**

    If you haven't already cloned the repository containing `chain_of_agents.py`, clone it now using Git:

    ```bash
    git clone https://github.com/ramin4251/Chain-of-Agents/
    cd Chain-of-Agents
    ```

2.  **Create a `.env` file:**

    In the project directory, create a file named `.env`. This file will store your Groq API key securely. Add the following line to `.env`, replacing `YOUR_GROQ_API_KEY` with your actual Groq API key:

    ```
    GROQ_API_KEY=YOUR_GROQ_API_KEY
    ```


3.  **Install Python dependencies:**

    It's recommended to create a virtual environment to keep your project dependencies isolated. If you're not familiar with virtual environments, you can skip this step, but it's good practice.

    ```bash
    # (Optional) Create a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows

    # Install required Python packages from requirements.txt
    pip install -r requirements.txt
    ```

## How to Run the Code

To execute the chain of agents, simply run the `chain_of_agents.py` script from your terminal within the project directory:

```bash
python chain_of_agents.py
```

The script will:

Initialize the agents with their respective tools and prompts.

Run the agents sequentially using the ChainOfAgents class.

Print the output of each agent to the console.

Finally, print the overall result from the chain of agents.

Example Output
When you run chain_of_agents.py, you should see output similar to the following (the time will reflect the current time when you run the script):

```
Running Agent 1
Agent 1 Output: 03:30 PM

Running Agent 2
Agent 2 Output: HELLO THERE 03:30 PM

Final Answer:
HELLO THERE 03:30 PM
```

Agents and Tools
Agent 1: Time Agent

Tool: TimeTool - A custom tool defined in the script that uses Python's datetime library to get the current time and format it.

Prompt: time_agent_prompt - Instructs the agent to use only the TimeTool and return only the current time.

Agent 2: Uppercase Agent

Tool: UppercaseTool - A custom tool that converts input text to uppercase using Python's upper() string method.

Prompt: uppercase_agent_prompt - Instructs the agent to use only the UppercaseTool to convert the input text to uppercase.

## Chain of Agents (ChainOfAgents Class)
The ChainOfAgents class in chain_of_agents.py is responsible for orchestrating the sequence of agents. It takes a list of agents and their associated tools as input. The run() method iterates through the agents, executing each one and passing the output of the previous agent as part of the input to the next agent. This simple chain demonstrates how you can combine specialized agents to perform more complex workflows.

## Further Exploration and Customization
This is a basic example to get you started with chaining Langchain agents using Groq models. You can expand upon this project in many ways, such as:

## Adding More Agents and Tools: 
Create more specialized agents and tools to perform a wider range of tasks (e.g., a weather agent, a translation agent, a search agent).

## More Complex Agent Interactions: 
Design more sophisticated chains where agents interact in more complex ways, perhaps with conditional logic or feedback loops.

## Different Groq Models: 
Experiment with different Groq models from the MODEL_LIST to see how they perform with these agents and prompts.

## Refining Prompts: 
Improve the agent prompts to guide the agents more effectively and achieve better results.

## Error Handling and Robustness: 
Enhance the error handling in the ChainOfAgents class to make the chain more robust.

## User Interface: 
Build a simple user interface (e.g., using a web framework like Flask or Streamlit) to make it easier to interact with the chain of agents.

Feel free to modify and experiment with this code to explore the possibilities of Langchain agents and Groq's powerful language models!
