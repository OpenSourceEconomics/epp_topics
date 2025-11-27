# Script: Imperative data cleaning

## Introduction

- This screencast introduces a typical imperative approach to data cleaning
- We'll see what most people do when they do data management
- Only relevant if this applies to you -- no need to go through this if you have not
  been doing data cleaning in the past
- Then we'll identify the problems with this approach

## Survey dataset

- Show the survey data from the slide
- Made up, but the steps needed for obtaining clean variables are quite realistic
- Explain the metadata: Q001, Q002, Q003 and the missing value codes

## Imperative approach

1. Trace `df`. The variables inside `df` change many times but keep their name
1. Trace `df["coding_genius"]`. There are many invalid intermediate states of df where
   variables already have their final names. This is especially dangerous if code is
   spread across multiple cells, let alone multiple files.
1. The global namespace will have nonsensical stuff like `var`, `categories`, `dtype`.
1. The code has no natural structure. We need comments to get some orientation.
1. The only way to re-use code across variables is to include it in a loop. Hence, the
   two agreement questions have to be cleaned at the same time, whether they are related
   or not.
1. We either had to repeat the name `favorite_language` multiple times or use method
   chaining. Which is hard to read and debug.
