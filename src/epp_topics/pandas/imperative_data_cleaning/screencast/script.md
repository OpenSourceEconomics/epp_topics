# Script: Imperative data cleaning

## Introduction

- This screencast introduces a typical imperative approach to data cleaning
- We'll see what most people do when they start with data management
- Then we'll identify the problems with this approach

## Survey dataset

- Show the survey data from the slide
- Mention that this is made up, but the steps needed for obtaining clean variables are
  quite realistic
- Explain the metadata: Q001, Q002, Q003 and the missing value codes

## Switch to `imperative_cleaning.ipynb`

Walk through the notebook showing:

1. The imperative approach (the code example)
1. The problems with the imperative way

You might want to execute the code live and show some of the problems, especially:

- How the DataFrame changes multiple times
- How helper variables clutter the namespace
- How hard it would be to reuse parts of the code
