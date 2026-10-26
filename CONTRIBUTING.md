# Contributing to Hardware, Networks & Behaviourist AI

This repository contains beginner-friendly learning materials for Hardware, Networks,
and Behaviourist AI. Every contribution should improve the content, its evidence, or
the organisation of the project.

## Before starting

1. Check the relevant task in `project-management/TASKS.md` or create a GitHub Issue.
2. Identify the module and files that will be changed.
3. Check `CONTENT-OUTLINE.md` so the new material fits the learning sequence.
4. Assign an owner and, where relevant, a reviewer.

## Branches

Use a separate branch for focused work. Suggested names are:

- `content/hardware-topic`
- `content/networks-topic`
- `content/behaviourist-ai-topic`
- `media/stage1-report`
- `docs/project-structure`
- `qa/review-topic`

Do not make unrelated changes in the same branch. Keep the `main` branch stable and
open a Pull Request before merging substantial work.

## Content requirements

When adding or editing learning material:

- Write for first-year students with little or no previous knowledge.
- Define unfamiliar terms before using them.
- Include a clear explanation, worked example, learner activity, and answer or expected outcome where appropriate.
- State assumptions in numerical examples and diagrams.
- Use accurate, identifiable sources and update the relevant references.
- Use relative links and local assets where possible.
- Keep diagrams readable and record their provenance in `docs/ASSET-PROVENANCE.md`.
- Update the relevant `OUTLINE.md` and `ANSWER-KEY.md` when the module structure or activity answers change.
- Keep Hardware, Networks, and Behaviourist AI examples consistent with the shared integration example.

## Commits

Make focused commits with descriptive messages. Examples:

- `docs: clarify Stage 1 project structure`
- `content: add CPU ADD instruction activity`
- `content: correct HTTPS layer explanation`
- `media: prepare four-minute classroom report`
- `qa: record Networks review outcome`

Use the actual contributor's GitHub account. Do not create artificial commits, backdate
work, or use activity-only changes to inflate the history. If one member uploads another
member's work, record the author and uploader accurately in the project evidence.

## Pull Requests and review

A Pull Request should include:

- a short description of what changed and why;
- the related Issue or task ID, when available;
- the files or module affected;
- the checks already completed;
- any remaining uncertainty or follow-up work.

Request review from a different team member. The reviewer should check factual accuracy,
beginner accessibility, examples, answers, citations, relative links, and visual
readability. Record the date, material checked, finding, and correction or confirmation
in `project-management/qa-log.md`.

## Required checks

Before requesting a merge:

1. Run the source validator described in `tools/README.md`.
2. Check that Markdown links and local images work.
3. Confirm that examples and answer keys use the same numbers and assumptions.
4. Inspect the rendered content where the change affects diagrams or layout.
5. For slides or video, check that the material matches the Markdown source.
6. For the classroom report, check that the final MP4 is no longer than four minutes,
   has clear audio, and works offline from `TeamName_Stage1_StatusReport`.

## Privacy and AI use

Do not commit passwords, access tokens, personal logs, private submission evidence, or
unnecessary student identifiers to the public repository. Significant AI assistance must
be disclosed in the relevant project and personal records, together with verification of
the resulting claims. AI output does not replace a human teammate's review.

## Project records

After completing work, update the appropriate project record with the real date and
evidence:

- `project-management/TASKS.md` for task status;
- `project-management/project-log.md` for verified activities and decisions;
- `project-management/qa-log.md` for review findings and corrections;
- `docs/PROJECT-CHANGES.md` for the current structure/content change summary.

Only record activities that actually occurred. The repository history and project logs
should make it possible to understand who contributed, what changed, and how the work
was checked.
