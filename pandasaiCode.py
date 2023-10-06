!pip install pandas openai pandasai 

import pandas as pd

from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# To get an openai key go to https://openai.com/, create an account, then go to profile -> View API Keys -> API keys -> Create new Secreat key
llm = OpenAI(api_token="your-openai-key-here")

df = pd.read_csv('/path/simpleFood.csv')
sdf = SmartDataframe(df, config={"llm": llm,"conversational": True})

# Basic information about the dataset
df.head()
df.shape
df.info()

# Question 1
sdf.chat("How many restaurants are there in NY?")

# Question 2
sdf.chat("What is the period of the week with the most orders and how many?")

# Question 3
sdf.chat("which type of food takes the shortest preparation time and how long it takes? Also show the order_id")

# Question 4
sdf.chat("What is the average price of each type of food?")

# Question 5
sdf.chat("What is the most famous cuisine among customers and what is the percentage of orders compared to the rest?")

# Question 6
sdf.chat("What are the 10 restaurants that made the most money?")

# Question about chart
sdf.chat("calculate the sum of each restaurant's earnings, then plot some charts with the 10 highest earnings")

# Question 7
sdf.chat("Which customer placed the largest number of orders? How much were they and how much was spent?")

# Question about chart
sdf.chat("plot a bar chart about customer orders 52832 and the type of food")
