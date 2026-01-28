# CLAUDE.md - AI Agent Guidelines for Documentation and Text Formatting

This file provides guidance for AI coding agents working on documentation and text
formatting tasks. The recommendations are based on the "Texts, Typesetting, and Text
Data" chapter of the Effective Programming Practices for Economists course.

## Table of Contents

1. [Markup Languages Overview](#markup-languages-overview)
1. [Markdown Syntax](#markdown-syntax)
1. [Code Snippets](#code-snippets)
1. [Writing README Files](#writing-readme-files)
1. [General Best Practices](#general-best-practices)

______________________________________________________________________

## Markup Languages Overview

Markup languages allow writing formatted documents in plain text files. The primary
markup language for documentation is **Markdown** due to its simplicity and wide
support.

### DO

- Use Markdown for README files, documentation, and communication (GitHub issues, pull
  requests, chat platforms)
- Focus on structure and content rather than formatting
- Write documents that are readable both in source form and when rendered
- Use markup languages to enable better version control of documentation

### DON'T

- Don't use complex markup languages (like LaTeX or raw HTML) when Markdown suffices
- Don't sacrifice readability in source form for fancy rendering
- Don't mix different markup languages unnecessarily within a single document

______________________________________________________________________

## Markdown Syntax

### Headings

Use hashtags (`#`) to create hierarchical headings. The number of hashtags indicates the
heading level.

```markdown
# Title (Level 1)

## Subtitle (Level 2)

### Section (Level 3)

###### Smallest level (Level 6)
```

### DO

- Use heading levels hierarchically (don't skip levels)
- Keep heading text concise and descriptive
- Use a single Level 1 heading (`#`) per document for the main title

### DON'T

- Don't use hashtags for comments (they create headings in Markdown)
- Don't skip heading levels (e.g., going from `#` directly to `###`)

______________________________________________________________________

### Text Styling

```markdown
**bold**
*italic*
~~strikethrough~~
***bold and italic***
```

### DO

- Use **bold** for emphasis on important terms or warnings
- Use *italic* for introducing new terms or subtle emphasis
- Use styling sparingly to maintain readability

### DON'T

- Don't overuse text styling; it reduces impact
- Don't use styling for entire paragraphs

______________________________________________________________________

### Lists

**Bulleted lists:**

```markdown
- Item one
- Item two
- Item three
```

**Numbered lists:**

```markdown
1. First item
2. Second item
3. Third item
```

**Auto-numbered lists (recommended):**

```markdown
1. First item
1. Second item
1. Third item
```

### DO

- Use bulleted lists for unordered items
- Use numbered lists when sequence matters
- Consider using `1.` for all items in numbered lists (auto-numbering) to make
  reordering easier

### DON'T

- Don't create deeply nested lists (more than 2-3 levels)
- Don't mix list styles inconsistently

______________________________________________________________________

### Links and Quotes

**Links:**

```markdown
[Link text](https://example.com)
```

**Block quotes:**

```markdown
> This is a quote
> spanning multiple lines
```

### DO

- Use descriptive link text that indicates the destination
- Use block quotes for attributions or highlighting external content

### DON'T

- Don't use raw URLs without link text when possible
- Don't use the wrong syntax order (it's `[text](url)`, not `[url](text)`)

______________________________________________________________________

## Code Snippets

This is critical for technical communication. Always use proper code formatting.

### Inline Code

Use backticks for inline code references:

```markdown
Use `x = 10` to assign a value.
```

### Code Blocks

Use triple backticks with language specification for syntax highlighting:

````markdown
```python
def cobb_douglas(labor, capital, alpha):
    return labor**alpha * capital ** (1 - alpha)
```
````

For tracebacks and error messages, use the `pytb` language identifier:

````markdown
```pytb
TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'float'
```
````

### DO

- Always use proper code blocks with language identifiers for syntax highlighting
- Include the language identifier (python, pytb, bash, etc.) after the opening backticks
- Format code snippets properly when asking questions or reporting issues
- Include minimal reproducible examples when reporting bugs
- Attach full tracebacks as separate files if they are long

### DON'T

- Don't take screenshots of code (use text-based code blocks instead)
- Don't paste unformatted code in communications
- Don't omit the language identifier in code blocks
- Don't include unnecessary code in examples; keep them minimal

______________________________________________________________________

## Writing README Files

The README.md is the first thing visitors see when they visit a repository. It must be
well-formatted and informative.

### Core Principles

1. **First impressions matter**: Format nicely using Markdown
1. **Don't Repeat Yourself (DRY)**: For large projects, point to where detailed
   information can be found
1. **Be complete for small projects**: The README might be the only documentation
1. **Show you care**: About both the project and the reader

### Essential Content

Every README should address:

1. **Entry point to the project**

   - What is the goal?
   - How is that being achieved?

1. **How to get it running**

   - For experienced users: Bare minimum requirements and precise commands
   - For less experienced users: Links to background information
   - System assumptions and requirements

1. **Basic purpose of the project**

   - What problem does it solve?
   - Why would someone use it?

### DO

- Write READMEs in Markdown (readable in source, renders nicely)
- Include clear installation/setup instructions
- State assumptions about the system required to run the project
- Provide the basic purpose of the project upfront
- Keep it concise; respect the reader's time
- Include links to additional documentation for complex projects

### DON'T

- Don't make READMEs excessively long
- Don't include detailed API documentation in the README (link to it instead)
- Don't include dependency trees or detailed technical diagrams
- Don't use plain text when Markdown formatting would improve readability
- Don't use overly complex markup (like ReStructuredText) when Markdown suffices

______________________________________________________________________

## General Best Practices

### For AI Agents Writing Documentation

1. **Prioritize readability**: Documents should be clear in both source and rendered
   form

1. **Be consistent**: Use the same formatting conventions throughout a document

1. **Structure matters**: Use headings, lists, and sections to organize content
   logically

1. **Code formatting is essential**: Always use proper code blocks with language
   identifiers

1. **Keep it minimal**: Include only necessary information; link to details elsewhere

1. **Consider the audience**: Provide information appropriate for both experienced and
   novice users

1. **Use previews**: When writing Markdown, check how it renders to improve quality

### Quick Reference: Markdown Syntax

| Element       | Syntax                        |
| ------------- | ----------------------------- |
| Heading       | `# H1` `## H2` `### H3`       |
| Bold          | `**text**`                    |
| Italic        | `*text*`                      |
| Strikethrough | `~~text~~`                    |
| Link          | `[text](url)`                 |
| Inline code   | `` `code` ``                  |
| Code block    | ```` ```language ... ``` ```` |
| Bullet list   | `- item`                      |
| Numbered list | `1. item`                     |
| Quote         | `> text`                      |

______________________________________________________________________

## Summary of Key Points

1. Use Markdown for all documentation tasks
1. Always format code properly with language-specific code blocks
1. Never use screenshots of code; use text-based code blocks
1. README files should be concise but complete
1. Focus on structure and content over complex formatting
1. Keep the reader in mind: both source and rendered forms should be readable
