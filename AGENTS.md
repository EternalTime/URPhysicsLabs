# Project agent memory

This file is the project's committed home for project-intrinsic agent knowledge: build, test, release, architecture, and sharp-edge notes that should travel with the code.

- Add durable project-specific notes here as they are discovered through real work.

## Lab PDFs

`assets/docs/LabNN*.pdf` are build outputs.
Their LaTeX sources live outside version control, in the untracked `localOnly/` tree at the repo root, under `localOnly/UofR_Lab_Documentation/Lab NN: <Title>/` (`writeup.pdf` is the combined `LabNN.pdf`).
That tree stays local and read-only to agents; publish by copying built PDFs in, not by recompiling (it was built with TeX Live 2025).

Each lab publishes four PDFs - combined (`LabNN.pdf`, linked only from the TA/TI page via `_data/labs.yml`) plus `-manual`, `-prelab`, `-postlab`.
Publish all four from the same build so their PDF `CreationDate` values agree.

## Maintaining this file

Keep this file for knowledge useful to almost every future agent session in this project.
Do not repeat what the codebase already shows; point to the authoritative file or command instead.
Prefer rewriting or pruning existing entries over appending new ones.
When updating this file, preserve this bar for all agents and keep entries concise.
