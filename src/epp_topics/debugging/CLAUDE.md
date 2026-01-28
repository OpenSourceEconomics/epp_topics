# Debugging Guidelines for AI Coding Agents

This document provides guidance for AI coding agents on writing good code and debugging
effectively, based on the "Effective Programming Practices for Economists" course
materials.

## Core Philosophy

Debugging is a learnable skill that accounts for 25-50% of programming time. There are
two complementary modes of debugging:

1. **Inspeculation** - A hybrid of inspection, simulation, and speculation. No
   experimentation, but "thinking about" the code.
1. **Data Gathering** - Collecting information about program state to confirm or refute
   hypotheses.

Both modes parallel the scientific method: inspeculation corresponds to theory building,
while data gathering corresponds to experimentation.

______________________________________________________________________

## Bug Prevention (Avoiding Debugging)

Prevention is better than cure. The best debugging is the debugging you never have to
do.

### DO: Write Preventive Code

- **Write comprehensive unit tests**

  - Test all code paths, not just the happy path
  - Cover edge cases explicitly
  - One test per function is usually NOT enough
  - Thoroughly tested functions can be skipped during debugging

- **Implement thorough error handling**

  - Validate inputs at function boundaries
  - Write clear, informative error messages
  - Error handling helps locate where things go wrong
  - Reserve error handling for public interfaces, not private helper functions

- **Write readable, modular code**

  - Give functions a clear, single purpose
  - Use informative variable names that describe content
  - Make code easy to mentally simulate
  - Keep functions small enough to understand at a glance

### DON'T: Skip Prevention Steps

- Don't skip writing tests because "it's simple code"
- Don't write vague error messages like "invalid input"
- Don't use cryptic variable names like `x`, `temp`, or `data` without context
- Don't write functions that do multiple unrelated things

______________________________________________________________________

## Psychology of Debugging

Effective debugging requires the right mindset. Avoid these common psychological
pitfalls:

### DON'T: Give in to Counterproductive Urges

1. **The urge to skip reading**

   - Tracebacks contain valuable information
   - Always identify: the line where the error occurred, the error type, and the error
     message
   - When narrowed to ~30 lines, read every line and explain what it does

1. **The urge to just run it again**

   - Computers are deterministic
   - The same code produces the same result
   - If it fails once but works the second time, you have a bigger problem

1. **The urge to tell yourself it should work**

   - If you are debugging, something clearly did not work
   - Don't rationalize why code should work when it does not
   - Accept reality and investigate

1. **The urge to try random things**

   - Random changes rarely fix bugs
   - Changes without reason make things worse
   - You lose track of what you tried

1. **The urge to blame libraries**

   - Most libraries are well-tested and written by experienced programmers
   - Bugs in your code are far more likely than bugs in libraries
   - Assume libraries are correct until you have strong evidence otherwise

### DO: Maintain the Right Mindset

- Read error messages and tracebacks thoroughly
- Accept that the bug is in your code
- Stay calm and methodical
- Take breaks when frustrated
- Use rubber duck debugging - explain the code to someone (or something)

______________________________________________________________________

## Debugging Strategies (Agans' Rules)

Follow these systematic rules when debugging:

### Rule 0: Get It Right the First Time

**DO:**

- Invest in unit testing
- Implement proper error handling
- Write readable, modular code

**DON'T:**

- Skip prevention because debugging seems faster
- Assume you'll write bug-free code without safeguards

### Rule 1: What Is It Supposed to Do?

**DO:**

- Define exactly what is going wrong
- Know how you determined something is wrong
- Anticipate what the program should do at each step

**DON'T:**

- Accept "it doesn't work" as a problem description
- Start debugging without understanding expected behavior

### Rule 2: Is It Plugged In?

**DO:**

- Verify you're running the code you think you're running
- Check test data is correct
- Confirm configuration is as expected
- Verify the correct version and environment is active

**DON'T:**

- Assume the setup is correct
- Spend hours debugging code that isn't even being executed

### Rule 3: Make It Fail

**DO:**

- Find a test case that reproduces the failure
- Simplify the test case as much as possible
- Use the scientific method: hypothesis, prediction, experiment
- Turn each experiment into a permanent test case

**DON'T:**

- Debug intermittent failures without a reproduction case
- Use complex test cases when simple ones would suffice

### Rule 4: Divide and Conquer

**DO:**

- Narrow the gap between cause and effect
- Start with the simplest failing test case
- Step through with a debugger
- Write tests for untested functions that are called
- Add error handling where necessary
- Iterate: simplify, test, repeat

**DON'T:**

- Try to understand the entire codebase at once
- Skip intermediate validation steps

### Rule 5: Change One Thing at a Time, for a Reason

**DO:**

- Make a git commit BEFORE starting to debug
- Have a hypothesis before making any change
- Re-run all tests after every change
- Undo changes that were not helpful (git reset --hard is your friend)

**DON'T:**

- Make multiple changes simultaneously
- Replace random chunks of code hoping something works
- Work on new features while debugging
- Skip committing because the code is broken

### Rule 6: Write It Down

**DO:**

- Keep records of what you tried
- Document parameter combinations tested
- Track which changes had which effects
- Prepare clear explanations when asking for help

**DON'T:**

- Rely on memory for complex debugging sessions
- Ask for help without being able to explain what you tried

### Rule 7: Be Humble

**DO:**

- Ask for help after 15 minutes of being stuck
- Explain the problem aloud (rubber duck debugging)
- Take your time - rushing makes things worse
- Track your common mistakes to learn from them

**DON'T:**

- Keep insisting the code should work
- Debug while frustrated or rushed
- Ignore patterns in your past mistakes

______________________________________________________________________

## Data Gathering Techniques

When inspeculation is not enough, gather data systematically.

### DO: Use Debuggers Over Print Statements

- Debuggers are interactive and show only what you need
- Set breakpoints with `import pdbp; breakpoint()`
- Use conditional breakpoints for specific scenarios
- Essential debugger commands:
  - `n` - execute **n**ext line
  - `s` - execute next **s**tep (steps into functions)
  - `c` - **c**ontinue until next breakpoint
  - `u` - go one frame **u**p
  - `d` - go one frame **d**own
  - `exit` or `ctrl+d` - stop debugging

### DON'T: Rely Solely on Print Statements

- Print statements are time-consuming to write well
- They produce either too much output or risk missing important information
- They require code modification and cleanup
- They cannot be adjusted interactively

### Breakpoint Variations

```python
# Simple breakpoint
import pdbp

breakpoint()

# Conditional breakpoint (only triggers when condition is met)
if gamma1 <= 0.5:
    import pdbp

    breakpoint()
```

### Context-Specific Usage

- **Plain Python files**: Use `import pdbp; breakpoint()`
- **pytest**: Use `breakpoint()` (no import needed if configured)
- **pytask**: Use `breakpoint()` (no import needed if configured)

______________________________________________________________________

## Summary Checklist for AI Agents

When writing code:

- [ ] Write unit tests covering all paths and edge cases
- [ ] Add error handling with clear messages at public interfaces
- [ ] Use descriptive variable and function names
- [ ] Keep functions focused on a single purpose
- [ ] Commit working code frequently

When debugging:

- [ ] Read the full traceback and error message
- [ ] Commit current state before making changes
- [ ] Define exactly what is wrong and how you know
- [ ] Verify the environment and configuration
- [ ] Create a minimal reproduction case
- [ ] Form a hypothesis before each change
- [ ] Change one thing at a time
- [ ] Re-run tests after each change
- [ ] Undo unhelpful changes
- [ ] Document what you tried
- [ ] Ask for help if stuck for more than 15 minutes

When gathering data:

- [ ] Prefer debuggers over print statements
- [ ] Use conditional breakpoints for specific scenarios
- [ ] Inspect variables at each step to verify assumptions
- [ ] Narrow down the problem location systematically
