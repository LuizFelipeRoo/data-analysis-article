!pip install langchain pandas openai

from langchain import OpenAI
from langchain.agents import load_tools, initialize_agent, create_pandas_dataframe_agent, Tool, AgentType
from langchain.llms import OpenAI

import pandas as pd
import os

# To get an openai key go to https://openai.com/, create an account, then go to profile -> View API Keys -> API keys -> Create new Secreat key
os.environ["OPENAI_API_KEY"] = "your-API-key-here"

llm = OpenAI(model="text-davinci-003", temperature=0)
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False)

df = pd.read_csv('/path/simpleFood.csv')
agent = create_pandas_dataframe_agent(llm, df, verbose=False)

# Question 1
agent.run('How many restaurants are there in NY?')

# Question 2
agent.run('What is the period of the week with the most orders and how many?')

# Question 3
agent.run('which type of food takes the shortest preparation time and how long it takes? Also show the order_id')

# Question 4
agent.run('What is the average price of each type of food?')

# Question 5
agent.run('What is the most famous cuisine among customers and what is the percentage of orders compared to the rest?')

# Question 6
agent.run('What are the 10 restaurants that made the most money?')

# Question about chart
agent.run('calculate the sum of each restaurants earnings, then plot some charts with the 10 highest earnings')

# Question 7
agent.run('Which customer placed the largest number of orders? How much were they and how much was spent?')

# Question avout chart
agent.run('plot some charts about customer orders 52832 and the type of food')
