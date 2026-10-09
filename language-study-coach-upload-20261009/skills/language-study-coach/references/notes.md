# Notes and storage

Generate Obsidian-compatible Markdown without requiring Obsidian. Use the user's approved template when supplied; otherwise adapt the layouts below. Clear ordinary Markdown must remain readable even when a viewer does not render callouts or wikilinks.

## Writing boundary

If a save destination is unknown, ask once when saving is requested and provide the note in the conversation meanwhile. Do not silently choose a directory. Reuse an explicitly configured destination within its authorized scope; do not repeatedly ask. Do not infer permission to save a learner profile from permission to save a lesson note.

Inspect an existing target before editing. Preserve unrelated content and user folder structure. Do not force migration, rename historical files, create empty placeholders, or overwrite a same-title note belonging to a different source. Make provenance and uncertainty visible. Link only to real notes or explicitly label proposed future notes.

## Self-contained layouts

These are adaptable architectures, not external dependencies:

- Text: overview → actual sources → preview points → natural paragraph quote and translation → numbered sentence analysis immediately below the paragraph → sentence network → useful phrase review → plot/argument and expression → existing related notes.
- Dialogue: overview → sources → each complete turn, translation and relevant analysis → reusable structures and phrases → related exercises when in scope.
- Exercises: chapter core grammar → per-exercise tested points → complete stressed answer set and translations → whole-sentence item explanations and alternatives → reusable decision cue.
- Vocabulary: source-order intake if requested → thematic detailed entries preserving traceability → useful forms, morphology, meanings, collocations, examples and contrasts → sources and links.
- Grammar review: triggering example → core rule → formation and syntax → usage and minimal contrasts → transfer task.
- Test: verified scope → all questions → folded answer and explanation section. Interactive testing may withhold the key instead.

For Chinese lesson labels, suggested names are 第X课课文文本解析, 第X课对话文本解析, 第X课课文习题, 第X课对话习题, 第X课语法练习, and 第X课重点词汇解析. Follow explicit user names instead; English tasks may use natural task-specific titles. Do not hardcode a textbook or lesson into tags.

## Formatting and quality

Use minimal nonempty YAML fields for type, lesson when known, status and tags. Keep provenance and relationships in body text. Use callouts for summaries, warnings, uncertainty, and folded answers; tables for true comparisons, not every entry. Add diagrams only when they materially explain branching relationships.

Before saving, verify source-turn/sentence/item coverage, answer completeness, uncertain portions, stress, real link targets, filename validity, and intended destination. Coverage checks do not by themselves prove linguistic accuracy.
