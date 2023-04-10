# import statements

import pandas as pd
import matplotlib.pyplot as plt

"""## Data Exploration

**Challenge**: Read the .csv file and store it in a Pandas dataframe
"""

df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

"""**Challenge**: Examine the first 5 rows and the last 5 rows of the of the dataframe"""

print(df.head())
print(df.tail())

"""**Challenge:** Check how many rows and how many columns there are. 
What are the dimensions of the dataframe?
"""

print(df.shape)

"""**Challenge**: Count the number of entries in each column of the dataframe"""

df.count()

"""**Challenge**: Calculate the total number of post per language.
Which Programming language has had the highest total number of posts of all time?
"""

print(df.groupby("TAG").sum())
print("\nPROGRAMMING LANGUAGE WITH HIGHEST NUMBER OF POSTS: ", df.groupby("TAG").sum().idxmax()["POSTS"])

"""Some languages are older (e.g., C) and other languages are newer (e.g., Swift). The dataset starts in September 2008.

**Challenge**: How many months of data exist per language? Which language had the fewest months with an entry? 

"""

print(df.groupby("TAG").count())
print("\nLANGUAGE WITH FEWEST MONTHS OF POSTS: ", df.groupby("TAG").count().idxmin()["POSTS"])

"""## Data Cleaning

Let's fix the date format to make it more readable. We need to use Pandas to change format from a string of "2008-07-01 
00:00:00" to a datetime object with the format of "2008-07-01"
"""

print(df.DATE[1])

print(type(df.DATE[1]))

df.DATE = pd.to_datetime(df.DATE)
print(df.DATE)

"""## Data Manipulation


"""

reshaped_df = df.pivot(index="DATE", columns="TAG", values="POSTS")
print(reshaped_df)

"""**Challenge**: What are the dimensions of our new dataframe? How many rows and columns does it have? Print out the 
column names and print out the first 5 rows of the dataframe."""

print(reshaped_df.shape)

print(reshaped_df.columns)

reshaped_df.head()

"""**Challenge**: Count the number of entries per programming language. Why might the number of entries be different?"""

reshaped_df.count()

reshaped_df.fillna(0, inplace=True)

reshaped_df.isna().values.any()

"""## Data Visualisation with with Matplotlib

**Challenge**: Use the [matplotlib documentation](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.
pyplot.plot.html#matplotlib.pyplot.plot) to plot a single programming language (e.g., java) on a chart.
"""

x = reshaped_df.index

y1 = reshaped_df["java"]
y2 = reshaped_df["python"]

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)
plt.plot(x, y1)

"""**Challenge**: Show two line (e.g. for Java and Python) on the same chart."""

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)

for column in reshaped_df.columns:
    plt.plot(x, reshaped_df[column], linewidth=3, label=reshaped_df[column].name)

plt.legend(fontsize=16)

"""# Smoothing out Time Series Data

Time series data can be quite noisy, with a lot of up and down spikes. To better see a trend we can plot an average 
of, say 6 or 12 observations. This is called the rolling mean. We calculate the average in a window of time and move 
it forward by one observation. Pandas has two handy methods already built in to work this out: [rolling()](
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.rolling.html) and [mean()](
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.core.window.rolling.Rolling.mean.html)."""

roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.ylabel("Number of Posts", fontsize=14)
plt.ylim(0, 35000)
for column in roll_df.columns:
    plt.plot(x, roll_df[column], linewidth=3, label=roll_df[column].name)

plt.legend(fontsize=16)
