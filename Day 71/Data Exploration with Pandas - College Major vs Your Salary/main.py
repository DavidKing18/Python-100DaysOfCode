import pandas as pd
df = pd.read_csv("salaries_by_college_major.csv")

print(df.head())  # To peek at the top 5 rows of our dataframe

print(df.shape)  # To see the number of rows and columns

print(df.columns)  # To access the column names directly

print(df.isna())  # To check for missing values and junk data.

print(df.tail())  # To check the last couple of rows in the dataframe

clean_df = df.dropna()
print(clean_df.tail())

print(clean_df['Starting Median Salary'])

print(clean_df['Starting Median Salary'].max())  # gets largest value

print(clean_df['Starting Median Salary'].idxmax())  # gives us index for the row with the largest value

print(clean_df["Undergraduate Major"].loc[43])  # to retrieve given row under specified column

print(clean_df.loc[43])  # to retrieve an entire row


# Challenge
# What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is
# defined as having 10+ years of experience).


