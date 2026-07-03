@.ai-instructions/profiles/tier-b-course.md @.ai-instructions/modules/pytask.md

# Effective Programming Practices for Economists: Topics

Source for the topic pages at https://effective-programming-practices.vercel.app/, built
via https://github.com/OpenSourceEconomics/effective-programming-practices. Each topic
lives under `src/epp_topics/<area>/<topic>/` and holds its objectives, materials, and,
where relevant, a `screencast/` (Slidev slides) and an `example/` project.

## Build and test

```bash
# Set up the environment (uses Pixi, not conda or pip)
pixi install
npm install

# Build every topic page
pixi run pytask
```

## Conventions

- Slides are written in Slidev (`screencast/slides.md`); static export goes through
  `npx slidev export` and needs the npm packages installed.
- Example projects under a topic's `example/` directory carry their own `pyproject.toml`
  and pixi environment; run them with an explicit `--manifest-path`, never with the
  working directory inside the example.
