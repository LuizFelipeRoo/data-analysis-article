# data-analysis-article
codes and datasets used in the article

# pandas code to check if the answer is correct

# Question 1
df['restaurant'].nunique()

# Question 2
(df["day"]=="Weekend").sum()
(df["day"]=="Weekday").sum()

# Question 3
df.nsmallest(1, 'preparation(min)')

# Question 4
df_grouped = df.groupby('cuisine')['cost'].mean()

# Question 5
sdf.plot_pie_chart(labels="cuisine", values="cuisine")

# Question 6
df_sum = df.groupby('restaurant')['cost'].sum().nlargest(10)

# Question 7
df_customer = df.loc[df['customer'] == 52832, 'cost'].sum()
