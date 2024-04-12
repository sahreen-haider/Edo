import os
import getpass
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import AgentExecutor, create_openai_functions_agent, load_tools
from langchain.memory import ConversationBufferMemory
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv, find_dotenv
# from rag import *
# from langchain_community.utilities import SerpAPIWrapper
# import dotenv


_ = load_dotenv(find_dotenv)

instructions = 'you are an assistant.'
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)

llm = ChatOpenAI(temperature=0.1)
output_parser = StrOutputParser()
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
tavily_tool = TavilySearchResults(include_images=True)
tools = [tavily_tool]

agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent,
    tools = tools,
    memory=memory,
    verbose=False
)
