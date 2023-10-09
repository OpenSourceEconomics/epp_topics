# Script: Pure functions

Anecdote: R. once was there when I explained to someone how to define functions and
said: "Since I am not writing packages, the good thing is I rarely have to write code in
functions". Then I realized that for me it is the opposite. "Since I am mostly writing
packages I have the luxury that most of my code can be in (pure) functions".

I hope we can transmit this idea, that a function is not something you have to write but
something you want to write for all the benefit it brings

## Definition of pure functions

- Mention that functions in math are pure functions

## Benefits of pure functions

- Last bullet point: Mention how important jax has become for us

## Push impurities to the boundaries

- Note that 99 % of our code will be in `clean_data` and the functions that get called
  in clean_data. They can all be pure.
