## Instagram Automation using CrewAI

Welcome to the Instagram Crew project, powered by crewAI. This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.
## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [Poetry](https://python-poetry.org/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install Poetry:

```bash
pip install poetry
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
poetry lock
```
```bash
poetry install
```
### Customizing

**Add your `OPENAI_API_KEY` or `GROQ_API_KEY `into the `.env` file**.

**Add your `LANGTRACE_API_KEY` if you want to track/monitor the process happening in the backend.**

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this:

```bash
python main.py
```

This command initializes the instagram Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Understanding Your Crew

The instagram Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `tasks.py`, leveraging their collective skills to achieve complex objectives. The `agents.py` file outlines the capabilities and configurations of each agent in your crew.
