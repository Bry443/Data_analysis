# Overview

I am on a mission to learn about about databases! This program was written to enlighten my understanding upon Python's place in datasets. Using Python to acess large datasets is something I've never done before so I hopped on to this opportunity to interact with one. I want to compare and contrast how this experience using Python code compares to using an language made specifically for this, such as SQL.

To acess the dataset, extract all of the files in the zipped folder: "stack-overflow-developer-survey-2022.zip" inside of the folder:"stackoverflowdata"

This dataset was taken from a StackOverflow annual survey distributed freely online. The Survey offered an array of questions targeting coders, such as languages used, education, workplace environments, etc. A link to the download can be found at 
* [stackoverflow](https://insights.stackoverflow.com/survey)

This program was written to list how many coders had Bachelors/Masters degrees, amount of coders per programming language, and how many coders had mental health issues.

# Data Analysis Results

How many coders had Bachelors/Masters degrees? 30276 coders with Bachelor's degrees and 15486 coders with Master's degrees.

What are some of the most popular coding languages that people know? Firstly is JavaScript, having 46443 coders. Followed by HTML/CSS, with 39142. And taking third,SQL having 35127 coders. 

What are some counts of age groups and their sexualities? In 18-24 year olds, there were 863 people who reported themselves as straight. Among Under 18 year olds there were 2378 who reported themselves as straight.

# Development Environment

This program was made using Visual Studio Code and the pandas python module for browsing datasets.

Python was used for this program's functioning. The pandas module was a necessity in interacting with the datasets as it allowed turning the csv files into data that python code could acess. Jypiter was used to view the data in a easier to access manner.

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [pandas](https://pandas.pydata.org/docs/getting_started/overview.html)
* [Python Simplified](https://pythonsimplified.com/how-to-handle-large-datasets-in-python-with-pandas/)

# Future Work

* Make the 3rd respons formatted to take less space, possibly by limiting amount of data returned.
* The answer for finding age and count only returns values that are not left empty. Edit to compensate for that possibility.