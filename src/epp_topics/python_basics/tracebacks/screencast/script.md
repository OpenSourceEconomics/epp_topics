# Script: Tracebacks

## Motivation

- We have told you several times that certain things are not allowed
- Now: what happens when you do them anyway?
- Exception = class of error; traceback = the detailed report Python gives you
- Most important advice: read the traceback!

## Example Traceback

- Walk through the code on the left: creating a dict, then trying to use a list as key
- Line 2 triggers the error — line 3 never runs
- Show the three things to extract: error type, location, message
- Tracebacks can be very long → always start reading from the bottom

## Common sources of errors

- Quick tour — just name each one and the most common trigger
- Students will encounter all of these in the first exercises

## First step: Ask an AI

- Demo live: trigger the Cobb-Douglas TypeError in a notebook cell
- Select all traceback text, copy it (keyboard shortcut, not a screenshot)
- Open chatbot, type the one-sentence context, paste the traceback
- Show the prompt on screen while typing

## What the AI gives you

- Show the AI's response
- Point out: it names the error type, the line, explains the tuple vs. float issue
- In this case the AI will likely spot the trailing comma on `labor = 2.5,`
- This is often enough — no need to ask anyone else

## When AI doesn't resolve it

- Walk through the left column: read the explanation, apply fix, re-run
- If a new traceback appears → paste that one too
- Only if that cycle doesn't resolve it: post to Zulip (course stream, not DM)
- Must show what you tried and what the AI said

## How not to ask for help

- Read each bullet, briefly comment
- Screenshot point: paste text, not an image — this applies to AI too, and AI literally
  cannot read a screenshot

## A better way (for a hypothetical task)

- This is what a good Zulip post looks like
- Note: the person answering does not remember what exercise 2 is → always name it

## A better way (continued)

- Minimal example: stripped down to just what reproduces the error
- The trailing comma on `labor = 2.5,` is the bug — but don't reveal that yet
- Attach the full traceback as copied text
- Mention what the AI suggested and why it didn't help
