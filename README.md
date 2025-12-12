# Steady Focus
A lightweight productivity web app: public blog with visitor idea submissions, user task CRUD and a Pomodoro timer.

[Live Demo](https://steady-focus-bc183b5c3b1f.herokuapp.com/)

## Project purpose
Steady Focus helps users plan and run focused work sessions and collect/curate productivity content from visitors.

## Features
- Public blog (posts + admin publishing)  
- Visitor blog submission form (saves as submissions for admin review)  
- User accounts (register/login/logout via allauth)  
- Task CRUD with owner-restrictions (private)  
- Client-side Pomodoro timer (public)

### Existing Features
### Future Features (optional)

## User Stories
A [GitHub Kanban board](https://github.com/users/JenE87/projects/10) was set up in Git projects to capture User Stories and follow an agile development approach. For this purpose and to track the project's development progress the project board consists of four columns: Backlog, In Progress, In Review/QA and Done.

## ERD
<img width="1052" height="662" alt="ERD_Steady_Focus" src="https://github.com/user-attachments/assets/376b48c2-6d84-4a05-84f4-176891baafa1" />

## Technologies
The following tools and technologies were used to build this project:

### Languages
- **Python 3.12**
- **CSS**
- **JavaScript** (vanilla)

### Tools & Services 
- **HTML** 
- **Django 5.2.8**
- **PostgreSQL** (production), **SQLite** (development)  
- **django-allauth** for authentication  
- **django-summernote** for rich text in admin
- **[SmartDraw](https://www.smartdraw.com/)** - for creating and visualizing the ERD
- **LanguageTool** - for grammar, spelling, paraphrasing support in code strings and documentation
- **Lucid Chart** - for drawing the ERD
- **ChatGPT** - for planning, debugging, and documentation support
- **Google Gemini** - for planning, debugging, and documentation support

### Development & Services
- **VS Code** - IDE, code editor
- **Python virtual Environment (venv)**


## Design & Layout

## Testing
### Manual Testing
| Feature                           | Test Input                     | Expected Result               | Pass/Fail |
|-----------------------------------|--------------------------------|-------------------------------|-----------|
| Signup / Registration | Go to Sign up, fill valid email + password, submit | New user account created, redirected / logged in, user appears in admin/users. | Pass |
| Login / Logout        | Login with valid creds, then click Logout | Login succeeds; navbar updates to show username; logout returns to public state. | Pass |
| Protected routes (Tasks) | Access `/tasks/` while not logged in | Redirected to login page (or 403 if configured) | Pass |
| Blog list (home & /blog/) | Visit homepage and /blog/ | Latest posts display, excerpts visible, cards render; pagination present when > page size. | Pass |
| Blog post detail | Click a post card → open detail | Full post body displays, back link works. | Pass |
| Blog idea submission (public) | Fill idea form (name/email/body) and submit (logged out & logged in) | Idea saved in DB (check admin), success message shown, no 500 error in prod. | Pass |
| Blog Card Layout | Visit /blog/ page. | All post cards render at the same height, regardless of title length or excerpt length. | Pass |
| Idea admin moderation | In Django admin, find Idea entry and toggle reviewed / delete | Changes persist, no errors, list view shows new state. | Pass |
| Pagination edge cases | Request `?page=333` and `?page=-1` | Shows last or current page (no 500); pagination links correct. | Pass |
| Excerpt truncation (cards) | Post with long words and long body shown in card grid  | Words do not split mid-letter; truncation/clamp shows ellipsis, readable on mobile. | Pass |
| Task CRUD (create/edit/delete) | Create a task, edit fields, mark completed, delete | Each action saves correctly; list updates; delete removes from DB and UI. | Pass |
| Task ownership / permissions | User A creates task; User B attempts to view/edit/delete task URL | User B gets 403 or is redirected; only owner can edit/delete. | Pass |
| Quick-toggle complete (task list) | Click quick-complete toggle button on task list | Task toggles completed state immediately; UI updates (badge/strike-through). | Pass |
| Task filters & sorting | Use status filter & sort dropdowns | List filters/sorts correctly and follows queryset parameters. | Pass |
| Task list mobile layout | Open task list on narrow viewport (mobile) | Layout stacks vertically, buttons large enough to tap, no overflow. | Pass |
| Pomodoro timer core functionality | Start → let run → reaches 0 → switches to break → bell rings | Timer counts down; on finish mode switches, bell rings, and timer for new mode auto-starts | Pass |
| Pomodoro presets | Click 25/5 and 50/10 presets then Start | Timer uses selected durations; display updates accordingly. | Pass |
| Pomodoro pause / resume / reset | Start, Pause, Resume, Reset | Pause stops ticking; Resume continues; Reset resets remaining time to preset. | Pass |
| Pomodoro sound/auto-switch | Start work timer (25 min preset). Let the timer count down to 0:00. | The bell sound plays, and the timer automatically switches to the 5-minute break session, and back to a 25-minute work session | Pass |
| Static Assets (CSS) | Visit the Pomodoro page on the Heroku URL. | The custom background color loads, and the timer's numeric font size is large and correct. | Pass |
| Migrations on deploy | Deploy new model migration (e.g. Idea) and run `heroku run python manage.py migrate`| Migration runs without error; new model usable in prod (no 500 on usage). | Pass |
| CSRF protection | Attempt POST without CSRF token | Server returns 403; after adding CSRF header the request succeeds. | Pass |
| Admin access | Login to /admin with staff user | Admin login succeeds; Blog, Tasks, Ideas models visible and editable. | Pass |
| Error pages (403/404) | Visit a non-existent URL / force a permission error | Custom 404/403 pages render without exposing stack traces. | Pass |
| Responsive checks (various pages) | Open Home, Blog, Task, Pomodoro on mobile, tablet, desktop | Layout adapts; readable text; buttons accessible; no horizontal scroll. | Pass |
| Task Urgency Badges | 1. Create Task A: Due Date set to yesterday. 2. Create Task B: Due Date set to today. 3. Task A, B are NOT marked complete. | Task A shows the "OVERDUE" badge. Task B shows the "DUE TODAY" badge. | Pass |
| Task Urgency Badges | Mark Task A (Overdue) as complete and refresh the task list. | The "OVERDUE" badge disappears; the task shows the "Done" badge and strikethrough styling. | Pass |

### Lighthouse Testing
### Validator Testing
- HTML Validator (W3C)
- CSS Validator (Jigsaw)
- JavaScript (Jshint)
- WAVE® Evaluation Tool (Web Accessibility)
- PEP8 Python Validator
### Fixed Bug
- **Server error (500) when submitting blog ideas in production**
  - Cause: `Idea` model migrations were not applied on Heroku.
  - Fix: Commit migration files manually on Heroku. 
- **`{% static %}` template tag throwing errors**
  - Cause: Missing `{% load static %}` at top of templates
  - Fix: Added `{% load static %}` directly under `{% extends "base.html" %}`.
- **`post_list()` got unexpected keyword argument `template_name`**
  - Cause: Passing CBV-only kwargs (`template_name`) to a function-based view.
  - Fix: Added a proper `home()` FBV for the root URL instead of misusing `post_list`.
- **Navbar link not routin to homepage**
  -  Cause: Link pointed to `/` which routed to `post_list` instead of `home`.
  -  Fix: Added `{% url 'home' %}` and set root URL to a real homepage view.
- **Pagination not workong in FBV setup**
  - Cause: Missing `is_paginated`, `page_obj`, and consistent context names.
  - Fix: Added these to the FBV and updated templates accordingly.
- **Audio Notification not playing at timer completion**
  - Cause: An ID mismatch in the HTML/JavaScript (`notification sound` vs `notification-sound`).
  - Fix: Standardizef the element ID.
- **Pomodoro timer crashing at zero**
  - Cause: Attempting to call `.play()` on a global audio variable before the DOM had fully loaded, resulting in a `null` reference error.
  - Fix: Wrapped DOM element assignments within a `DOMContentLoaded` event listener. 
- **CSS hover effects causing visual confusion on detail views**
  - Cause: A global `.card:hover` transition was causing the entire task detail view to "lift", which distracted from functional buttons like "Edit" and "Delete".
  - Fix: Added a `.no-hover-lift` class and updated the CSS selector to `:not(-no-hover-lift)` to exclude single-view cards from the animation. 
- **Django template tags failing inside external JavaScript file**
  - Cause: Attempting to use {% static %} tags directly inside pomodoro.js to define file paths, which Django template engine does not process for static files.
  - Fix: Integrated the audio element directly into the `pomodoro.html` template using Django tags and referenced the element in JavaScript via its ID.
- **The custom `stlye.css` (incl. background, color vars, specific timer font size) was not loading on deployed Heroku app, resulting in a plain, unstyled look.**
  - Cause: The `staticfiles/` directory, which is generated by Django's `collectstatic` command and meant for production use by Whitenoise, was accidently tracked and commited to the Git repo. This conflict prevented the WhiteNoise middleware from running clean and correct static file collection during deployment.
  - Fix: The cachhed `staticfiles/` folder was removed from Git tracking (`git rm -r --cached staticfiles`), the directory was added to the `.gitignore` file to prevent future tracking, and a final push was performed to force Heroku to run a clean build and static file collection.
- **Words breaking mid-letter inside Bootsrap cards**
  - Cause: Browser default word splitting behaviour.
  - Fix: Added CSS `word-break: normal; overflow-wrap: break-word;` and refined clamping styles.

### Unfixed Bugs
- **Lexend font and primary color not consistently applying to all headings**
  - Cause: Potential CSS specificity conflicts with Bootstrap's default heading styles or specific card and container classes overriding the global font-family and primary color rule.
  - Status: Parked for future styling refactor; core functionality prioritized.

## Deployment
### Local Setup
### Version Control
### Heroku Deployment

## Credits
### Code
### Content & Media





