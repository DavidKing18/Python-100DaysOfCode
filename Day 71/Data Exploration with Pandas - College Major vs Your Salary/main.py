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

career_id = clean_df["Mid-Career Median Salary"].idxmax()
college_career = clean_df["Undergraduate Major"].loc[career_id]
salary = clean_df["Mid-Career Median Salary"].loc[career_id]
print("\nCollege major with highest mid-career salary: {}  |  ID: {}  |  Salary: {}".format(college_career, career_id, salary))

# Which college major has the lowest starting salary and how much do graduates earn after university?

career_id = clean_df["Starting Median Salary"].idxmin()
college_career = clean_df["Undergraduate Major"].loc[career_id]
salary = clean_df["Mid-Career Median Salary"].loc[career_id]
print("\nCollege major with lowest starting salary: {}  |  ID: {}  |  Salary: {}".format(college_career, career_id, salary))
print(clean_df.loc[career_id])
# Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?

career_id = clean_df["Mid-Career Median Salary"].idxmin()
college_career = clean_df["Undergraduate Major"].loc[career_id]
salary = clean_df["Mid-Career Median Salary"].loc[career_id]
print("\nCollege major with lowest mid-career salary: {}  |  ID: {}  |  Salary: {}".format(college_career, career_id, salary))
print(clean_df.loc[career_id])


######################################################################################################
# Sorting Values & Adding Columns: Majors with the Most Potential vs Lowest Risk
######################################################################################################

spread_col = clean_df["Mid-Career 90th Percentile Salary"] - clean_df["Mid-Career 10th Percentile Salary"]
clean_df.insert(loc=5, column="Difference", value=spread_col)
print(clean_df.head())

low_risk = clean_df.sort_values("Difference")
print(low_risk[["Undergraduate Major", "Difference"]].tail())

# Challenge
highest_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
print(highest_potential[["Undergraduate Major", "Mid-Career 90th Percentile Salary"]].head())

high_risk = clean_df.sort_values("Difference", ascending=False)
print(high_risk[["Undergraduate Major", "Difference"]].head())

highest_average = clean_df.sort_values("Mid-Career Median Salary", ascending=False)
print(highest_average[["Undergraduate Major", "Mid-Career Median Salary"]].head())

print(clean_df.groupby('Group').count())

pd.options.display.float_format = '{:,.2f}'.format   # To configure number formats in the output
print(clean_df.groupby('Group').mean())
