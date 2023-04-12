""" # Introduction

Today we'll dive deep into a dataset all about LEGO. From the dataset we can ask a bunch of interesting questions
about the history of the LEGO company, their product offering, and which LEGO set ultimately rules them all:

<ul type="square">
<li>What is the most enormous LEGO set ever created and how many parts did it have?</li>

<li>How did the LEGO company start out? In which year were the first LEGO sets released and how many sets did the
company sell when it first launched?</li>

<li>Which LEGO theme has the most sets? Is it one of LEGO's own themes like Ninjago or a theme they licensed liked
Harry Potter or Marvel Superheroes?</li>

<li>When did the LEGO company really expand its product offering? Can we spot a change in the company strategy based
on how many themes and sets did it released year-on-year?</li>

<li>Did LEGO sets grow in size and complexity over time? Do older LEGO
sets tend to have more or fewer parts than newer sets?</li>
</ul>

**Data Source**

[Rebrickable](https://rebrickable.com/downloads/) has compiled data on all the LEGO pieces in existence. I recommend
you use download the .csv files provided in this lesson.

# Import Statements
"""

import pandas as pd
import matplotlib.pyplot as plt

"""# Data Exploration

**Challenge**: How many different colours does the LEGO company produce? Read the colors.csv file in the data folder 
and find the total number of unique colours. Try using the [.nunique() method](
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.nunique.html?highlight=nunique#pandas
.DataFrame.nunique) to accomplish this."""

colors = pd.read_csv("data/colors.csv")

colors.head()

colors['name'].nunique()

"""**Challenge**: Find the number of transparent colours where <code>is_trans == 't'</code> versus the number of 
opaque colours where <code>is_trans == 'f'</code>. See if you can accomplish this in two different ways."""

is_trans = 0
is_not_trans = 0
for lego in colors.is_trans:
    if lego == 't':
        is_trans += 1
    elif lego == 'f':
        is_not_trans += 1

print(f"f: {is_not_trans}")
print(f"t: {is_trans}")

colors.groupby("is_trans").count()

print(colors.is_trans.value_counts())

"""### Understanding LEGO Themes vs. LEGO Sets

Walk into a LEGO store and you will see their products organised by theme. Their themes include Star Wars, Batman, 
Harry Potter and many more.

<img src="https://i.imgur.com/aKcwkSx.png">

A lego **set** is a particular box of LEGO or product. Therefore, a single theme typically has many different sets.

<img src="https://i.imgur.com/whB1olq.png">

The <code>sets.csv</code> data contains a list of sets over the years and the number of parts that each of these sets 
contained.

**Challenge**: Read the sets.csv data and take a look at the first and last couple of rows.
"""

sets = pd.read_csv("data/sets.csv")

print(sets.head())

print(sets.tail())

"""**Challenge**: In which year were the first LEGO sets released and what were these sets called?"""

print(sets.sort_values("year"))

"""**Challenge**: How many different sets did LEGO sell in their first year? How many types of LEGO products were on 
offer in the year the company started?"""

print(sets[sets.year == 1949])

"""**Challenge**: Find the top 5 LEGO sets with the most number of parts. """

print(sets.sort_values("num_parts", ascending=False).head())

"""**Challenge**: Use <code>.groupby()</code> and <code>.count()</code> to show the number of LEGO sets released 
year-on-year. How do the number of sets released in 1955 compare to the number of sets released in 2019?"""

sets_by_year = sets.groupby("year").count()
print(sets_by_year["set_num"].tail())

"""**Challenge**: Show the number of LEGO releases on a line chart using Matplotlib. <br> <br> Note that the .csv 
file is from late 2020, so to plot the full calendar years, you will have to exclude some data from your chart. Can 
you use the slicing techniques covered in Day 21 to avoid plotting the last two years? The same syntax will work on 
Pandas DataFrames."""

plt.plot(sets_by_year.index[:-2], sets_by_year["set_num"][:-2])


"""### Aggregate Data with the Python .agg() Function

Let's work out the number of different themes shipped by year. This means we have to count the number of unique 
theme_ids per calendar year."""

themes_by_year = sets.groupby("year").agg({"theme_id": pd.Series.nunique})
print(themes_by_year)

themes_by_year.rename(columns={"theme_id": "nr_themes"}, inplace=True)
print(themes_by_year.head())

themes_by_year.tail()

"""**Challenge**: Plot the number of themes released by year on a line chart. Only include the full calendar years (
i.e., exclude 2020 and 2021)."""

plt.plot(themes_by_year.index[:-2], themes_by_year["nr_themes"][:-2])

"""### Line Charts with Two Seperate Axes"""

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.plot(themes_by_year.index[:-2], themes_by_year["nr_themes"][:-2], color='b')
ax2.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], color='g')

ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Themes", color="blue")
ax2.set_ylabel("Number of Sets", color="green")

"""**Challenge**: Use the <code>.groupby()</code> and <code>.agg()</code> function together to figure out the average 
number of parts per set. How many parts did the average LEGO set released in 1954 compared to say, 2017?"""

parts_by_set = sets.groupby("year").agg({"num_parts": pd.Series.mean})
parts_by_set.rename(columns={"num_parts": "average num_parts"}, inplace=True)
print(parts_by_set)

print(parts_by_set.tail())

"""### Scatter Plots in Matplotlib

**Challenge**: Has the size and complexity of LEGO sets increased over time based on the number of parts? Plot the 
average number of parts over time using a Matplotlib scatter plot. See if you can use the [scatter plot 
documentation](https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.scatter.html) before I show you the 
solution. Do you spot a trend in the chart?"""

plt.scatter(x=parts_by_set.index[:-2], y=parts_by_set["average num_parts"][:-2])

"""### Number of Sets per LEGO Theme

LEGO has licensed many hit franchises from Harry Potter to Marvel Super Heros to many others. But which theme has the 
largest number of individual sets?"""

set_theme_count = sets["theme_id"].value_counts()
print(set_theme_count[:7])

"""**Challenge** Use what you know about HTML markup and tags to display the database schema: <img 
src="https://i.imgur.com/Sg4lcjx.png">

### Database Schemas, Foreign Keys and Merging DataFrames

The themes.csv file has the actual theme names. The sets .csv has <code>theme_ids</code> which link to the 
<code>id</code> column in the themes.csv.

**Challenge**: Explore the themes.csv. How is it structured? Search for the name 'Star Wars'. How many 
<code>id</code>s correspond to this name in the themes.csv? Now use these <code>id</code>s and find the corresponding 
the sets in the sets.csv (Hint: you'll need to look for matches in the <code>theme_id</code> column)"""

themes = pd.read_csv("data/themes.csv")
print(themes[themes.name == "Star Wars"])

print(sets[sets.theme_id == 18])

print(sets[sets.theme_id == 209])

"""### Merging (i.e., Combining) DataFrames based on a Key

"""

set_theme_count = pd.DataFrame({"id": set_theme_count.index, "set_count": set_theme_count.values})
print(set_theme_count.head())

merged_df = pd.merge(left=set_theme_count, right=themes, on="id")
print(merged_df.head())

plt.bar(x=merged_df.name[:10], height=merged_df.set_count[:10])

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.xlabel("Theme Name", fontsize=14)
plt.ylabel("Number of Sets", fontsize=14)

plt.bar(x=merged_df.name[:10], height=merged_df.set_count[:10])
plt.show()
