# Hardware, Networks & Behaviourist AI — Stage 1 Project Plan

## 1. Project Overview

**Project:** Hardware, Networks & Behaviourist AI  
**Stage:** Stage 1 — Project planning, Markdown V1.0, PPT presentation, and video materials  
**Repository:** https://github.com/nsdmlk/bit-ai-and-cs  
**Revision date:** 26 October 2026  
**Target snapshot:** 30 October 2026, 23:59 Beijing time  
**Project coordinator:** Emir Babayev (`@Jerssy-h`) — CEO / planning and Hardware module  
**Repository and technical workflow:** Emelyanov Ilya — repository organisation, README, and initial Behaviourist AI work  
**Communication:** GitHub Issues, pull requests, and team meetings. No live chat or online account is required during the classroom report.

The project develops beginner-friendly learning materials explaining how computer hardware supports computing, how networks move information, and how Behaviourist AI learns through actions, rewards, and feedback. The three modules are developed separately and then connected into one Study Guide sequence.

The plan responds to the team's earlier evaluation. On the evening of 25 October 2026, the team met in B1 and identified that the previous version concentrated on topic content but did not present the project framework, continuation plan, review evidence, and supporting architecture clearly enough. The current revision therefore treats both educational content and project evidence as required deliverables.

## 2. Project Objectives

By the end of the learning materials, beginners should be able to:

- Define the main hardware components of a computer and explain how the CPU, memory, storage, buses, and input/output devices cooperate.
- Distinguish temporary working memory from persistent storage and explain why a program may use both.
- Trace a simple network request, identifying devices, addressing, packets, protocols, and the role of reliability and security.
- Explain the difference between a local network and communication across the Internet using an accessible example.
- Define Behaviourist AI in the context of agents, actions, states, rewards, policies, and learning from interaction.
- Follow a small Q-learning example and explain how a reward changes the value of an action.
- Connect hardware, networks, and Behaviourist AI in one system-level example, such as a robot or game agent receiving sensor data, communicating with a service, and selecting an action.
- Identify limitations and risks, including slow or unreliable hardware, network delay or failure, poor reward design, unsafe exploration, and overconfident conclusions.
- Use diagrams, worked examples, activities, and source references to learn and check understanding independently.

## 3. Scope and Chapter Structure

The project keeps the three module areas separate for drafting and review. They will be integrated into a coherent Study Guide after the individual explanations and examples have been checked.

| Area | Main files | Planned content | Current status |
|---|---|---|---|
| Hardware | `content/Hardware/OUTLINE.md`, `content/Hardware/ANSWER-KEY.md`, and the Hardware chapter files | Computer components, CPU and memory, storage, buses, input/output, performance trade-offs, and a worked ADD/LOAD trace | Drafted and revised; final independent content review pending |
| Networks | `content/Networks/OUTLINE.md`, `content/Networks/ANSWER-KEY.md`, and the Networks chapter files | Devices, addressing, packets, protocols, a step-by-step HTTPS request, reliability, security, and troubleshooting | Drafted and revised; final independent content review pending |
| Behaviourist AI | `content/Behaviorist AI/OUTLINE.md`, `content/Behaviorist AI/ANSWER-KEY.md`, and the Behaviourist AI chapter files | Agents, states, actions, rewards, policies, Q-learning, exploration, and responsible use | Drafted and revised; final independent content review pending |
| Integration | Shared examples and Study Guide mapping | A robot or interactive system combines hardware sensors, network communication, and a reward-driven decision loop | Planned and partially represented through cross-module links |

The shared examples are deliberately small and traceable: an ADD/LOAD hardware trace, an HTTPS request, a Q-learning update, and a final system diagram showing how the three areas interact. Each developed topic should contain definitions, an explanation, a worked example, a meaningful visual where useful, a learner activity, an answer or expected outcome, and identifiable references.

The intended audience is first-year university students with little or no previous knowledge of hardware, computer networks, or reinforcement-style learning. Explanations should require no mathematics beyond school-level arithmetic and should define technical terms when they first appear.

## 4. Deliverables

### Stage 1 planning and evidence

- `project-management/PROJECT-PLAN.md` — this scope, role, schedule, risk, and completion plan.
- `project-management/TASKS.md` — concrete tasks, owners, statuses, dependencies, and review requirements.
- `project-management/project-log.md` — verified activities, decisions, meetings, and evidence links.
- `project-management/qa-log.md` — review findings, corrections, and unresolved issues.
- `CONTENT-OUTLINE.md` and `QUALITYCHECKLIST.md` — module mapping and submission checks.

### Educational content

- Substantive Markdown V1.0 content for Hardware, Networks, and Behaviourist AI.
- Learning outcomes and mapping between objectives, chapters, examples, and activities.
- Worked examples, diagrams or tables where they improve understanding, learner questions, and explained answers.
- In-text citations and a consolidated source/reference record.
- Local supporting assets and `docs/ASSET-PROVENANCE.md` so the offline copy remains readable and borrowed material is identifiable.

### Presentation and video deliverables

- A completed first-stage PPT presentation in `slides/`, together with the slide outline, narrative plan, and presentation plan. The slides must present the three modules, shared learning sequence, examples, and current project status.
- Video materials in `videos/`, including the production plan and module storyboards for Hardware, Networks, Behaviourist AI, and integration. The video work must include prepared narration, visuals, timing, learner activities, and review points.
- A first-stage video export or recorded presentation by 30 October if the team has the required recording tools. If the course accepts a production-ready Stage 1 package instead of a final export, the corresponding script, storyboard, visuals, and recording plan must still be complete and clearly labelled.

### Submission package

- The classroom submission contains only the files needed for the report: the final prerecorded MP4 and any supporting PPT, images, fonts, or media needed for offline playback.
- Put multiple files in one clearly named folder: `TeamName_Stage1_StatusReport`. Submit one ZIP of that folder; submit a single file directly if the teacher accepts the MP4 alone.
- The project plan, task list, Markdown source, GitHub evidence, review record, and AI-use records remain internal project evidence. The current classroom instructions do not require a separate written report, presentation plan, or evidence document.
- The final submitted package must match the version played in class and must be tested after extraction on the classroom computer or equivalent offline environment.

### Classroom progress report format

The team will submit a prerecorded progress report that will be played on the classroom screen. It is not a complete lecture on Hardware, Networks, and Behaviourist AI. It is a concise report showing what the team is developing, what has been completed, what was learned from the earlier weakness, and what will be done next.

- **Maximum duration:** 4 minutes, including any introduction or closing.
- **Opening:** begin immediately with an attention-grabbing question or concrete system example, such as: “What happens between a sensor reading and an agent's action?”
- **Project direction:** identify the team, intended beginners, three modules, and learning goal in no more than a few seconds.
- **Current progress:** show the actual module structure, selected Markdown pages, local diagrams, and the current PPT/video work. Label completed, in progress, and planned work honestly.
- **GitHub and Markdown evidence:** show readable offline screenshots or screen recordings of the repository organisation, a meaningful change, and one substantive Markdown example. Do not depend on Internet access during class.
- **Representative example:** demonstrate one strong beginner-facing example, preferably the Hardware ADD/LOAD trace connected to the Network request and Q-learning/integration path.
- **Problem and next steps:** explain that the earlier version focused on topic content but did not present the project framework clearly, then state the priorities for Stage 2 due 7 November 2026.
- **Ending:** finish with the strongest evidence, not a long thank-you or a separate Q&A segment.

The complete report video will be rehearsed to finish slightly before four minutes. The team will place the final MP4 and any required supporting media in the named folder, copy the extracted folder to a USB drive, and test playback, sound, screenshots, and fonts on the classroom computer before the presentation session. No downloading, sign-in, cloud storage, or messaging app should be needed during class.

## 5. Team Roles and Responsibilities

| Member | Role | Main responsibilities |
|---|---|---|
| Emir Babayev (`@Jerssy-h`) | CEO / Project Coordinator; Hardware Lead | Maintain the plan and task list, coordinate the revised project structure, develop and revise Hardware content, track blockers, and prepare milestone readiness checks. |
| Emelyanov Ilya | CIO / Repository and Technical Workflow | Maintain repository organisation and README material, support branches and pull requests, preserve evidence, and coordinate the technical workflow and Behaviourist AI foundation. |
| Dmitrii | Content and Networks Lead | Develop and revise Networks explanations, worked traces, diagrams, planning documents, and source integration; coordinate consistency across the three modules. |
| Ivan | Hardware Research and Visual Support | Contribute Hardware research and diagrams, check the clarity of hardware demonstrations, and support visual consistency. |
| Adil | Video and Networks Support | Contribute the introductory Networks material, coordinate video planning, and align narration and demonstrations with the reviewed Markdown. |
| Alimzhan Nurpeissov (`@Alimbeeeeeek`) | Quality Lead / Reviewer | Review factual accuracy, citations, beginner accessibility, consistency, evidence, and corrections; record concrete findings in the QA log. |

All members must make identifiable, substantive contributions and be able to explain the sections they contributed. If someone uploads a change on behalf of another member, the author and uploader must be recorded accurately.

## 6. Work Process and Coordination

The team will use the following workflow:

1. Define a concrete task in GitHub Issues or the task list and identify its owner.
2. Create a branch for changes where appropriate; keep structural revisions separate until they are reviewed.
3. Make focused edits to Markdown, diagrams, slides, or scripts and use descriptive commit messages.
4. Check links, local assets, citations, examples, and answers before requesting review.
5. Open a pull request linked to the relevant issue when the work is ready.
6. Request review from the Quality Lead or another relevant team member and record the finding, correction, or confirmation.
7. Update the project log with the actual date, contributors, decision, and evidence link. Do not create artificial commits or retroactive meeting outcomes.
8. Before the final snapshot, verify the clean package independently by extracting it into a different folder.

The historical architecture review occurred on 25 October 2026 in B1. The team concluded that the earlier version over-emphasised topic content and did not make the project framework and continuation architecture clear. Other members revised their module structures in parallel. The revised learning material still requires a final independent content-level review before it is declared complete.

## 7. Milestones and Schedule

The dates below are the team's working schedule. A date marked **proposed** must be confirmed against the instructor's current instructions.

| Milestone | Target | Completion criteria |
|---|---|---|
| Architecture review and project-structure decision | 25 October 2026 — completed | Full-team review recorded; the missing framework, evidence, and continuation structure identified. |
| Revised project architecture and module plans | 26 October 2026 — in progress | This plan, task list, module outline, QA checklist, and supporting production folders are aligned. |
| Hardware review | 27 October 2026 — proposed | Hardware explanations, ADD/LOAD trace, diagrams, activities, answers, and references checked. |
| Networks and Behaviourist AI review | 28 October 2026 — proposed | Network trace, Q-learning example, activities, answers, references, and beginner accessibility checked. |
| Slides, report structure, and integration pass | 29 October 2026 — proposed | The selected 4-minute report sequence is complete; PPT visuals, Markdown evidence, and the shared system example agree. |
| Report recording, playback test, and rehearsal | 29 October 2026 — proposed | The prerecorded report is under four minutes, narration is clear, evidence is readable, and the video has been watched from beginning to end. |
| Final package and USB check | 30 October 2026 — proposed team target | `TeamName_Stage1_StatusReport` contains the final MP4 and required supporting files; the extracted folder and USB copy are tested offline. |
| Stage 1 submission and classroom readiness | 30 October 2026 — proposed team target | Files are submitted before the presentation, the final version matches the classroom version, and the team is ready before being called. |

The earlier course text supplied by the team listed a Markdown V1.0 deadline of 24 October 2026 at 23:55 UTC+8. The current classroom progress-report instruction sets the submission deadline as 30 October 2026 at 23:59 Beijing time and requires a maximum four-minute report video.

## 8. Dependencies and Risks

| Dependency or risk | Required action |
|---|---|
| The team may focus on content while neglecting structure | Keep the plan, task list, README, evidence, review records, and continuation path in the same release checklist as the Markdown. |
| AI-assisted explanations may contain errors or invented sources | Verify claims against reliable sources, record significant AI use, and have the Quality Lead review the result. |
| Hardware, Networks, and Behaviourist AI may become three disconnected topics | Use the shared robot/interactive-system example and maintain explicit cross-links and a final integration diagram. |
| Review may be informal or impossible to audit | Record reviewer, date, material checked, concrete outcome, and correction or confirmation in `qa-log.md`. |
| Missing or remote images may break the submitted copy | Prefer local assets, record provenance, validate relative paths, and test the extracted package offline. |
| Slides or videos may drift from the educational content | Freeze the reviewed explanation before finalising narration or visuals; link every storyboard section to a source Markdown topic. |
| Member contribution evidence may be unclear | Preserve meaningful commit history, issue/PR links, personal logs, and an accurate contribution table. |
| The Shared Assignment Rules and media requirements are unavailable or unclear | Obtain the rules, especially AI-use and personal-log requirements, and keep unresolved items in Section 10 rather than inventing compliance. |
| Deadline pressure may leave the final review incomplete | Prioritise factual and citation review, then package and rehearse only after the minimum evidence and content checks pass. |

## 9. Definition of Done

The Stage 1 planning and project package is ready for review when:

- The project purpose, audience, scope, module sequence, and integration example are documented.
- Each member has a clear responsibility and identifiable substantive work.
- The task list contains owners, statuses, dependencies, deadlines, and review requirements.
- Hardware, Networks, and Behaviourist AI contain substantive beginner-facing Markdown rather than headings or placeholders.
- Each developed topic includes accurate explanations, defined terminology, a worked example, a learner activity, an answer or expected outcome, and supporting references.
- Diagrams, images, links, and local assets work in the submitted copy.
- The 25 October architecture review and its concrete outcome are recorded, and the revised material has a separate final content review or an explicitly tracked remaining action.
- The project log contains only verified activities and decisions.
- Significant AI assistance, verification, and relevant personal/project records are documented according to the applicable rules.
- The PPT presentation is complete and aligned with the reviewed teaching content.
- The prerecorded progress report is complete, no longer than four minutes, and clearly covers direction, progress, GitHub/Markdown evidence, one representative example, the main problem, and Stage 2 next steps.
- The report video opens and plays offline from the named folder/USB copy with readable visuals and clear audio; supporting files are included when needed.
- The report identifies the repository snapshot and latest commit, explains contributions, and includes readable repository evidence.
- The source snapshot, rendered copy, report, logs, and assets are included in the final package.
- The package has been extracted into a different folder and checked before submission.

## 10. Pending Confirmations

- The complete Shared Assignment Rules, especially Section 6 requirements for AI-use records, personal logs, source attribution, and individual contributions.
- The exact team name to replace the `TeamName` part of `TeamName_Stage1_StatusReport`.
- The classroom computer's preferred MP4 codec/resolution, if the instructor provides one; the report is otherwise prepared as a standard offline MP4.
- The final independent content review date and reviewer sign-off for all three modules.
- The final member-to-file contribution mapping and any missing GitHub usernames.
- Confirmation that every member has the necessary repository access and can create identifiable commits.
- The final commit identifier to be cited in the report and package.
- The final rendered-content and ZIP extraction checks after all last-minute edits.

These items remain pending until the team or instructor confirms them. They must not be presented as completed requirements merely because they appear in the plan.
