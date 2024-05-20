# -*- coding: utf-8 -*-
"""PyPool_.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1QBHEd0MHzb-zWvRb459B0eqlJWKjpSfQ

Python Analysis of Budget Data
"""

import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('election_data.csv')

# Solution as required
# Total number of vote casted. This is the number or the length of the dataset
total_votes = len(df)

# Vote counts for each candidate
vote_counts = df['Candidate'].value_counts()

# Percentages and format results
results = []
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

# The Winner
winner = vote_counts.idxmax()

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Print out each candidate's name, vote count, and percentage of votes
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Define the election results text
election_results_text = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    election_results_text += f"{candidate}: {percentage:.3f}% ({votes})\n"
election_results_text += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the election results to the terminal
print(election_results_text)

# Save the election results to a text file
election_filename = 'election_results.txt'
with open(election_filename, 'w') as text_file:
    text_file.write(election_results_text)

# Download the file to your local system
from google.colab import files
files.download(election_filename)  # Make sure the filename matches
