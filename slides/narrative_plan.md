# Narrative Plan — Stage 1 Teaching Deck

## Audience

First-year computing students with no assumed background in hardware, networks, or
reinforcement learning.

## Objective

Show one coherent route from physical computation to networked information and learned
behaviour, while keeping the important labels, examples, and formulas editable in the
presentation.

## Narrative arc

1. Establish the three-part learning route.
2. Make CPU execution visible with a fetch–decode–execute trace.
3. Explain why performance depends on work and time, not only GHz.
4. Follow a web request through layers, IP, transport, DNS, and HTTP/TLS.
5. Introduce the agent–environment loop and Q-learning.
6. Integrate the parts in a robot observation-to-action example.
7. Close with retrieval questions and the source Markdown path.

## Source plan

- Hardware: `../content/Hardware/`.
- Networks: `../content/Networks/`.
- Behaviourist AI: `../content/Behaviorist AI/`.
- References: `../references.md`.

## Visual system and editability

Use high-contrast backgrounds, short titles, and editable cards for definitions and
steps. Diagram labels, formulas, activities, and captions remain editable PowerPoint
objects. Local SVG teaching diagrams from the Markdown source are available for later
replacement of abstract deck motifs.

## Video connection

Each major slide group has a matching storyboard in `../videos/`. The videos reuse the
same ADD trace, HTTPS trace, and Q-learning update rather than unrelated examples.

## Status

This is a Stage 1 production structure and editable deck. It does not claim that an
MP4 has been recorded, edited, compressed, or independently reviewed.
