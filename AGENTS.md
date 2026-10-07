# AXV Mentor: lesson preparation project

Instructions for any AI coding agent (Claude Code, Codex, Cursor, Gemini CLI, Aider, ...). Read this file first.

## What this project is

A mentor teaches programming to school groups under the programme "Muhammad al-Xorazmiy vorislari". All learner-facing material is written in **Uzbek (Latin script)**. Code, commands and technical terms stay in English. The mentor speaks Russian, so reports to the mentor can be in Russian (or in the language the mentor writes in).

| Folder | Group | Programme | Size |
|---|---|---|---|
| `8-sinf/` | 3 students | Web Full-stack | 102 lessons, 34 weeks |
| `9-sinf/` | group | UX/UI design and Advanced Front-end | 102 lessons, 34 weeks |
| `9-sinf-backend/` | group | Advanced Back-end va DevOps | 102 lessons, 34 weeks |
| `9-sinf-android/` | group | Android dasturlash | 102 lessons, 34 weeks |
| `9-sinf-bi/` | group | Business Intelligence: Ma'lumotlar tahlili | 102 lessons, 34 weeks |
| `9-sinf-game/` | group | Game Design | 102 lessons, 34 weeks |
| `9-sinf-iot/` | group | IoT (Internet of Things) — Buyumlar Interneti | 102 lessons, 34 weeks |
| `10-sinf-python/` | group | Advanced Python Back-end va Prompt Engineering | 102 lessons, 34 weeks |
| `10-sinf-cyber/` | group | Kiberxavfsizlik (Ethical Hacking) | 102 lessons, 34 weeks |
| `10-sinf-uxui/` | group | Advanced UX/UI dizayn va Advanced Front-end | 102 lessons, 34 weeks |
| `10-sinf-android/` | group | Advanced Android dasturlash | 102 lessons, 34 weeks |
| `10-sinf-bi/` | group | BI (Ma'lumotlar muhandisligi va ML) | 102 lessons, 34 weeks |
| `10-sinf-devops/` | group | DevOps | 102 lessons, 34 weeks |
| `11-sinf/` | 1 student | Professional IT development | 51 lessons, 17 weeks |

Every group has 3 lessons per week, 80 minutes each. Week = `ceil(lesson_no / 3)`. Lesson files are `dars-K` with K = 1..3 inside a week; the global lesson number is `3 * (week - 1) + K`.

## Folder map

```
AGENTS.md / CLAUDE.md          this file
<sinf>/karta.md                lesson map: lesson no, week, topic, status (⬜ planned · 📝 prepared · ✅ taught)
<sinf>/_matn/*.txt             plain text of the official programme/guide (.docx already converted)
<sinf>/*.docx                  original official documents
<sinf>/haftalik/hafta-NN/      prepared material per week
shablon/qoidalar.md            SHARED RULES for preparing a lesson (the main instruction file)
shablon/slaydlar.html          sample slides (14 block types), only <section> elements
shablon/slayd-qobiq.html       the shell every slide file is wrapped in
reveal/                        reveal.js 6.0.2, dars.css (theme), tema.js, logo.png, lucide/ (icons), ikonlar.js
sayt_sozlama.json              site wording (organisation name, home texts, footer)
slayd_yigish.py                wraps slides in the shell, builds icons; test files become quiz pages via quiz_yigish.py
quiz_yigish.py                 builds the mobile quiz page (one question per screen) from *-test-slaydlar.html
vitepress_yigish.py            exports content for the student website (sayt-vitepress/)
ikon_yigish.py                 collects used Lucide icons into reveal/ikonlar.js
sayt-vitepress/                VitePress student website (theme + components are hand-written, content under docs/ is generated)
.claude/agents/<sinf>-tayyorlov.md   per-class details (plain Markdown, readable by any model)
.claude/commands/              Claude Code shortcuts (/hafta, /sayt), optional
```

## How to prepare a week (the main task)

Input from the mentor: a class and a week number, for example "9-sinf, week 4". If no week is given, continue from "Keyingi dars" in `<sinf>/karta.md`.

1. Read `shablon/qoidalar.md` completely. It defines the output format, the student page, slide rules and checks.
2. Read `.claude/agents/<sinf>-tayyorlov.md` for class-specific data (sources, group size, subject notes).
3. Read `<sinf>/karta.md`, find the 3 lessons of the week and their topics. Do not re-read earlier weeks; glance at the previous week's `dars-3.md` only to keep continuity.
4. Read the relevant part of `<sinf>/_matn/*.txt`. These files are large: use `grep -n` to find the topic and read only that section.
   - **MANDATORY SOURCE RULE (Qat'iy qoida):** All primary information, theory, official terms, code examples, syllabus progression, and practical tasks MUST be taken exclusively from our official documents (`<sinf>/_matn/*.txt` and `.docx`). Every class and track has its own official document.
   - **Supplementary material from the Internet:** External sources (Internet) are allowed ONLY for secondary, enrichment information: "Bilasizmi?" trivia, interesting real-world analogies, or extra industry context. The foundation, core theory, and teaching material must always come strictly from our document. Never invent concepts that are absent in the official source; note unclear points in your report.
5. For each lesson K = 1..3 create in `<sinf>/haftalik/hafta-NN/`:
   - `dars-K.md` mentor file (plan, notes, code, tasks with `**Yechim:**` solutions, quick check)
   - `dars-K-oquvchi.md` student page (no solutions; at least 10 tasks tagged ` · oson/o'rta/qiyin/bonus`)
   - `dars-K-test-slaydlar.html` lesson test (10 questions, source of the quiz page, see "Tests" below)
   - `dars-K-slaydlar.html` slides: **only `<section>` elements** (20 to 28 slides, big SVG illustrations, fragments, icons via `<i data-ic="name"></i>`, no emoji)
6. Create `uyga-vazifa.md` (homework; its `## Mentor uchun` section is removed from the public site) and `baholash.md` (mentor-only grading template). Homework must match what the student pages say.
7. Run `python3 slayd_yigish.py` (wraps slides, builds icons, reports unknown icon names) and fix any errors.
8. Update `karta.md`: change ⬜ to 📝 for prepared lessons. Set ✅ and the "Joriy holat" block only when the mentor says the lessons were taught.
9. Verify (see below) and report briefly: files created, topics covered, unclear points, whether you verified visually.

Small-context models: do one lesson per run (steps 4 and 5 for a single K), then the week-level files.

## Hard rules

- **Core material source is EXCLUSIVELY our document.** Every class/track has its own official document. All primary lesson contents, concepts, definitions, code samples, and tasks must be taken strictly from `<sinf>/_matn/*.txt` (and `.docx`). Do not fabricate concepts or swap in outside syllabi. Supplementary information (trivia, real-world context for "Bilasizmi?") may be drawn from the Internet, but the primary material must come 100% from our official documents.
- **Never publish anything.** The mentor uploads the built folder `sayt-vitepress/docs/.vitepress/dist` themselves. Do not push, deploy, or send files anywhere.
- **Never edit generated files: `sayt-vitepress/docs/<sinf>/`, `docs/index.md`, `docs/public/*`, `docs/.vitepress/generated.json`, or the generated `dars-K-slayd.html`.** They are regenerated. Change the source instead: wording in `sayt_sozlama.json`, data in `vitepress_yigish.py`, look in `sayt-vitepress/docs/.vitepress/theme/`, slide chrome in `shablon/slayd-qobiq.html`, theme in `reveal/dars.css`, then rebuild.
- Student-facing files (`dars-K-oquvchi.md`, slides, `uyga-vazifa.md` outside `## Mentor uchun`) are public: no solutions, no mentor notes, no passwords or tokens. Solutions go only in `dars-K.md` after `**Yechim:**`.
- Slides: no emoji, no `#hex` or `rgba()` colours (use the CSS classes of `reveal/dars.css`: `fa fb fc fg fn la lb lc lg ln t-head t-accent t-muted ar-*`), no external URLs, no CDN. Use `{{UP}}reveal/...` for asset paths. Mentor notes go in `<aside class="notes">` and are stripped from the site.
- Do not fabricate facts, statistics or quotations. If you invent an illustrative example, label it as such.
- Do not add, delete or rename the course topics; the programme comes from the official documents.

## Build and check

```bash
python3 slayd_yigish.py          # wrap slides, build icons
python3 slayd_lint.py [<sinf>/haftalik/hafta-NN]   # static slide checks (unknown CSS classes, hero, icons, emoji...)
python3 vitepress_yigish.py      # export website content (all weeks)
python3 vitepress_yigish.py --gacha 5   # only weeks 1..5 are open, later weeks are shown as "coming soon"
cd sayt-vitepress && npm run dev        # live preview (exports first)
cd sayt-vitepress && npm run build      # export + build to docs/.vitepress/dist
```

Checks to run after writing slides:

1. Lint: `python3 slayd_lint.py <folder>` must pass (no invented CSS classes). Then the browser audit script `shablon/slayd_audit.js` (see its header) should report no overflow/overlap/clipped text on desktop and phone.
2. Structure: every `<section>` is closed, code uses `&lt;` and `&gt;`, no emoji, `slayd_yigish.py` exits cleanly.
2. Leaks (after `npm run build`): `grep -rli "yechim" sayt-vitepress/docs/.vitepress/dist` must not show task solutions (the plain word may appear in running text), and `grep -rl 'class="notes"' sayt-vitepress/docs/.vitepress/dist` must be empty.
3. Visual (if you have a browser tool): serve the folder with `python3 -m http.server <port>`, open `hafta-NN/dars-K-slayd.html`, step through slides with `Reveal.slide(i, 0, 99)` (shows all fragments), check that nothing leaves the 1280×720 area, check the light theme (`document.documentElement.dataset.theme = 'light'`) and a phone-size viewport (375×812). Screenshots can lag 1 to 2 seconds. Stop the server afterwards.
4. If you cannot view slides, say so in the report ("visual check not done").

## Tests (quiz pages, do not break)

- Source: `dars-K-test-slaydlar.html` (10 questions per lesson) and `hafta-test-slaydlar.html` (20 per week). Only `<section>` elements with `class="quiz"`, 4 options, the right one marked `data-ok`, a short `.explain` for every question (format: see "Testlar" in `shablon/qoidalar.md`).
- Output `*-test-slayd.html` is **not a slideshow**: `slayd_yigish.py` detects `class="quiz"` and delegates to `quiz_yigish.py`, which writes a standalone mobile-first page (one question per screen, big tap targets, green/red feedback + explanation, progress bar, score, review of mistakes, retry, light/dark theme, keys 1-4). Never edit the output; edit the source and rebuild.
- After `python3 slayd_yigish.py` about 240 unrelated `dars-N-slayd.html` files may show diffs. Revert them (`git checkout -- <files>`) and commit only the files you changed.
- The site exporter reuses `wrap()`, so after `/sayt` the site tests are quizzes too.

## Week conventions (keep every new week identical)

- Files per week: 3 x (`dars-K.md`, `dars-K-oquvchi.md`, `dars-K-slaydlar.html`, `dars-K-test-slaydlar.html`) + `hafta-test-slaydlar.html`, `uyga-vazifa.md`, `baholash.md`; generated `*-slayd.html` / `*-test-slayd.html`.
- Badge on slides/pages: `N-hafta · M-dars` (M = global lesson number). `karta.md`: set the 3 rows of the week from ⬜ to 📝.
- Mentor file sections: `Dars rejasi`, `Mentor konspekti`, `Amaliy topshiriqlar va yechimlar`, `Tezkor nazorat savollari`, `Uyga vazifa` (follow the style of the previous week of the same class).
- Slide lint: no 6-digit hex / `rgba()`, no emoji; icons only from `reveal/lucide` (known missing: help-circle, history, bar-chart-3, waves, align-center, filter, function-square, wrap-text, figma, github, use a neighbour icon).
- Primary content only from `_matn`; anything extra is flagged in the report. Check code samples by running them where possible and say what was not verified (e.g. Kotlin, `nginx -t`).
- Before finishing: `python3 slayd_yigish.py`, `python3 slayd_lint.py <hafta>` (0 problems), `shablon/slayd_audit.js` (0), then sync `karta.md`.
- Pushing to GitHub (`Adminuz/axv`) only when the mentor asks. With the GitHub MCP `push_files`, keep each payload file under 1 MiB (chunks of about 850 KB), then `git fetch && git reset --hard origin/main`. The repo is public and contains mentor solutions: recommend making it private.

## Design facts (do not break)

- Default theme is VS Code Dark+, with a Light+ toggle (button top-left on slides, key `T`). Colours come from CSS variables in `reveal/dars.css`.
- Icons are plain line icons from Lucide (`reveal/lucide/<name>.svg`); find a name with `ls reveal/lucide | grep <word>`.
- Everything must work on phones. On portrait phones the slide is laid out at 760 px logical width, blocks stack in one column, wide SVG diagrams scroll horizontally. Do not hard-code pixel widths.
- The organisation name appears once per page (header or hero), the footer text comes from `sayt_sozlama.json`.

## Adding a new class

1. Create `<sinf>/` with the official documents, convert them to text into `<sinf>/_matn/` (`unzip -p file.docx word/document.xml | sed 's/<\/w:p>/\n/g; s/<[^>]*>//g' | grep -v '^\s*$' > _matn/name.txt`).
2. Create `<sinf>/karta.md` in the same format as the existing ones (chapters as `## I-bob. Name (N dars)` and rows `| 1–3 | 1 | Topic | ⬜ |`).
3. Create `.claude/agents/<sinf>-tayyorlov.md` modelled on an existing one (class data only, it points to `shablon/qoidalar.md`).
4. Add the class to `SINFLAR` in `vitepress_yigish.py` (folder, name, subject, icon, quarter ranges or an empty list).

## Claude Code specifics (ignore in other tools)

Agents `8-sinf-tayyorlov`, `9-sinf-tayyorlov`, `11-sinf-tayyorlov` are the same instructions as above, runnable as subagents. Slash commands: `/hafta <sinf> [week]` and `/sayt [last week]` (builds the VitePress site).

## VitePress site (the student website)

`sayt-vitepress/` is a VitePress project. Content is exported from the same sources by `vitepress_yigish.py` (solutions and mentor sections are stripped). Hand-written files: `sayt-vitepress/docs/.vitepress/config.mts` and `docs/.vitepress/theme/*` (VS Code Dark+/Light+ colours). Everything else under `docs/` (pages, `generated.json`, `public/slaydlar`, `public/reveal`) is generated: never edit it by hand.

```bash
cd sayt-vitepress
npm install            # once
npm run dev            # exports content, then live preview
npm run build          # exports content, then builds to docs/.vitepress/dist
npm run preview        # serves the built site (restart it after every rebuild: it caches the file list)
```

Hosting (Vercel / Cloudflare Pages / Netlify): root directory `sayt-vitepress`, build command `npm run build`, output directory `docs/.vitepress/dist`, Node 20. Mentor-only files (`dars-K.md` with solutions) must not be in a public repository: use a private repo or upload only the built folder.

Pitfall: sidebar/nav texts are rendered as HTML by VitePress, so `vitepress_yigish.py` HTML-escapes them; lesson titles may contain `<form>` and similar.

VitePress theme: the default VitePress theme is kept only for the header, search and the dark/light switch. Pages are drawn by our components in `sayt-vitepress/docs/.vitepress/theme/components/` (`PageTop.vue`, `PageBottom.vue`, `Crumbs.vue`, `Icon.vue`) and styled by `theme/custom.css`. Page data (classes, weeks, lessons) is written by `vitepress_yigish.py` into each page's frontmatter (`kind: home|sinf|hafta|dars`); the student text stays Markdown wrapped in `<div class="blk">` cards. Change the look in the theme files, the data in the exporter.
