# Script: (Armchair) Psychology of debugging

I like Agan's rules and think they cover most of what I will cover here to some extent.
The idea of this screencast is to paint more vivid pictures and help students to
discover when they are not debugging efficiently.

This is not based on a source but on the things I need to fight while debugging

Each slide starts with a problem description and then describes what to do

# The urge to blame libraries

- Strongest example was a guy in Stanford who at some point was pretty sure that numpy's
  `dot` method must be wrong, so he wrote his own. Turned out, it wasn't :D

- In 8 years of programming I have only found one major bug in a library (jax while
  working on lcm)
