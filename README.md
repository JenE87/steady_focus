# Steady Focus
A lightweight productivity web application featuring a public blog, visitor idea submissions, personal task management, and a built-in Pomodoro timer.

[Live Demo](https://steady-focus-bc183b5c3b1f.herokuapp.com/)

## Project purpose
Steady Focus aims to help users **plan and complete focused work sessions**, manage tasks, and optionally browse or contribute productivity ideas through a simple, distraction-free interface. The project is intentionally minimalist and neurodivergent-friendly, focusing on clarity, predictability, and ease of use.

## Features
### Core Functionality
- **Public Blog:**
    * Clean card grid layout with pagination and dedicated detail views.
    * Content published by authenticated admin users.
- **Idea Submission:**
    * Anyone (logged in or out) can submit productivity ideas via a dedicated form.
    * Submissions are stored for admin review, promoting content curation.
- **User Accounts (Auth):**
    * Registration, login, and secure session management via **django-allauth**.
- **Task Management (CRUD):**
    * Private task lists (each user sees only their own).
    * Full CRUD functionality for creating, updating, and deleting tasks.
    * Quick-toggle completion directly from the task list.
- **Pomodoro Timer:**
    * Built-in client-side timer with audio notifications on cycle completion.
    * Supports popular presets (25/5 and 50/10) and auto-switches between work/break cycles.

### Advanced Features & UX Improvements
- **Task Prioritization & Organization:** Users can filter tasks by completion status and sort by Due Date, Title, or Created Date.
- **Status Visualization:** Tasks display clear urgency badges (**Overdue**, **Due Today**, **Done**).
- **Accessibility (A11y):** Use of semantic HTML and `aria-label` attributes on all interactive elements (buttons, forms) and `aria-current` on navigation links.
- **Error Handling:** Implemented custom, user-friendly `404 Not Found` and `403 Permission Denied` pages.

### Future Features (optional)
- Editable Pomodoro presets stored per user
- Themes (dark/light)
- Categories/tags for blog posts
- Task prioritisation or drag-and-drop reordering
- Implement Focus Session model that connects task to the Pomodoro timer

## User Stories
A GitHub Kanban board captures all user stories and tracks the development progress using an Agile approach.

Project Board:
https://github.com/users/JenE87/projects/10

Columns:
**Backlog → In Progress → In Review/QA → Done**

## ERD
<img width="1052" height="662" alt="ERD_Steady_Focus" src="https://github.com/user-attachments/assets/376b48c2-6d84-4a05-84f4-176891baafa1" />

## Technologies
The following tools and technologies were used to build this project:

### Languages
- **Python 3.12**
- **CSS**
- **JavaScript** (vanilla)

### Frameworks & Libraries 
- **Django 5.2.8** (primary web framework)
- **Bootstrap 5.3** (responsive design and UI components)
- **django-allauth** (for authentication)  
- **django-summernote** (for rich text editor in admin)
- **gunicorn** (WSGI HTTP Server for production)
- **psycopg2** )PostgreSQL database adapter)

### Databases
- **PostgreSQL** (production on Heroku)
- **SQLite** (local development)

### Tools & Services 
- **VS Code** - IDE, code editor
- **Python virtual Environment (venv)**
- **SmartDraw / LucidChart** (ERD creation)
- **LanguageTool** - for grammar, spelling, paraphrasing support in code strings and documentation
- **ChatGPT + Google Gemini** - for planning, debugging, and documentation support

### Deployment & Hosting
- **Heroku**
- **Whitenoise** (static file serving)

## Development vs Production Databases
Steady Focus uses **SQLite** for local development and **PostgreSQL** for production on Heroku.

- **SQLite (development)**
  Lightweight, file-based database suitable for rapid local development and testing.

- **PostgreSQL (production)**
  A robust, scalable relational database used by Heroku for production deployments.

This setup follows Django best practices and allows fast iteration locally while ensuring reliability and data integrity in production.

### Database Migrations (Local & Heroku)
Because development and production use different database engines, migrations must be handled explicitly.

**Local migrations (development):**
`python manage.py makemigrations`
`python manage.py migrate`
Migration files must be committed to Git so they are available in production.

**Applying migrations on Heroku (production):**
Migrations can be run in two ways:

**Option 1: Heroku CLI**
`heroku run python manage.py migrate`

**Option 2: Heroku Dashboard**
1. Open the app in the Heroku Dashboard
2. Navigate to **More (top right) → Run console**
3. Run:
`python manage.py migrate`
This approach was used during development to apply the `Idea` model migration after deployment.

### Important Notes for Developers
- Migration files must always be committed — Heroku does not generate them automatically.
- SQLite is more permissive than PostgreSQL; models that work locally may fail in production if constraints are incorrect.
- The local SQLite database file (`db.sqlite3`) must **not** be committed to Git, and therefore included in the `.gitignore` file.

## Design & Layout
Steady Focus follows a **minimalist, accessibility-first** design approach:

- Limited colour palette for reduced cognitive load
- Bootstrap 5.3 grid structure
- Cards with consistent height for polished visual rhythm
- No post images to avoid distraction
- Lexend font for improved readability (ongoing refinement)
- Reduced hover animations on detail pages for neurodivergent comfort
- Semantic HTML + aria labels where beneficial
- 
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
  - Fix: Added a `.no-hover-lift` class and updated the CSS selector to `:not(.no-hover-lift)` to exclude single-view cards from the animation. 
- **Django template tags failing inside external JavaScript file**
  - Cause: Attempting to use {% static %} tags directly inside pomodoro.js to define file paths, which Django template engine does not process for static files.
  - Fix: Integrated the audio element directly into the `pomodoro.html` template using Django tags and referenced the element in JavaScript via its ID.
- **The custom `stlye.css` (incl. background, color vars, specific timer font size) was not loading on deployed Heroku app, resulting in a plain, unstyled look.**
  - Cause: The `staticfiles/` directory, which is generated by Django's `collectstatic` command and meant for production use by Whitenoise, was accidently tracked and commited to the Git repo. This conflict prevented the WhiteNoise middleware from running clean and correct static file collection during deployment.
  - Fix: The cachhed `staticfiles/` folder was removed from Git tracking (`git rm -r --cached staticfiles`), the directory was added to the `.gitignore` file to prevent future tracking, and a final push was performed to force Heroku to run a clean build and static file collection.
- **Words breaking mid-letter inside Bootsrap cards**
  - Cause: Browser default word splitting behaviour.
  - Fix: Added CSS `word-break: normal; overflow-wrap: break-word;` and refined clamping styles.
- **Lexend font and primary color not applying constantly**
  - Cause: Bootstrap specificity issue
  - Fix: Increased CSS specificity by targeting nested elements using their parent classes

### Unfixed Bugs

## Deployment
### Local Setup
To run this project locally, follow the steps below.

### Prerequisites
- Python 3.12+
- Git
- A code editor (e.g. VS Code)

**Steps**
1. **Clone the repository of this project**
2. **Create a virtual environment**
   using venv and a Python version 3.12+ and check that your venv is running. If not, activate the virtual environment, using:
   - Windows:
     `venv\Scripts\activate` OR `.\.venv\Scripts\Activate.ps1`
   - macOS/Linux:
     `source venv/bin/activate`
3. **Install dependencies**
   by selecting ok during set up of the virtual environment of using
   `pip install -r requirements.txt`
   *(Note: If you add new dependencies locally, update the `requirements.txt` file using `pip freeze > requirements.txt` before pushing to GitHub.)*
4. **Add `.venv` to the `.gitignore` file**
   to ensure the virtual environemnt folder is excluded from version control.
5. **Create an environment (`.env`) file**
   in the project root based on `.env.example` and add your own values:
   `SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=sqlite:///db.sqlite3`
6. **Run database migrations**
   `python manage.py makemigrations`
   `python manage.py migrate`
7. **Create a superuser (optional, for admin access)**
   `python manage.py createsuperuser`
8. **Run the development server**
   `python manage.py runserver`
   The app will be available at:
   `http:*//127.0.0.1:8000/*`

### Version Control
This project uses **Git** for version control.

### Heroku Deployment
This project is deployed using **Heroku** with **PostgreSQL** as the production database.

**Deployment Steps**
1. **Create a Heroku app**
   - Log in to Heroku
   - Click New → Create new app
   - Choose a unique app name and (your) region
2. **Attach a PostgreSQL database and configure environment variables**
   In the app dashboard, go to **Settings --> Config Vars** and add
   - `DATABASE_URL` with the value of your PostgreSQL database
   - `SECRET_KEY`
3. **Connect to your GitHub Repository**
   In the app dashboard, go to **Deploy**
   - Select **GitHub** as *Deployment method*
   - Under *App connected to GitHub* search for your repository and connect it
   - *Enable automatic deploys (optional)* or deploy manually
4. **Deploy the application**
   - Trigger a deployment from the Heroku dashboard
5. **Apply database migration**
   After deployment, migrations must be run manually:
   **Via Heroku Dashboard**
   - Open the app in Heroku
   - Click **More (top right) --> Run console**
   - Run:
     `python manage.py migrate`
   **Or via Heroku CLI in your code editor#s terminal:**
     `heroku run python manage.py migrate`
6. **Collect static files**
   Static files are handled automatically by **WhiteNoise** during deployment.
   No manual `collectstatic` command is required.

## Credits
### Code
- Code Institute LMS course materials
- Antionio Melé (2025). *Django 5 By Example*. Packt Publishing Ltd.
- [Django documentation](https://docs.djangoproject.com/en/6.0/) 
- [Bootstrap 5 documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Python.org](https://www.python.org/)
- [W3 schools](https://www.w3schools.com/)
- [Geeksforgeeks - Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
- [freecodecamp](https://www.freecodecamp.org/news/)
- [Stack Overflow](https://stackoverflow.com/questions)
- [Medium - Member Articles](https://medium.com/)
- [testdriven.io](https://testdriven.io/)
- [codecademy](https://www.codecademy.com/)
- [reddit](https://www.reddit.com/)
- [Mozilla Developer Network (MDN)](https://developer.mozilla.org/en-US/)
- [cosaslearning](https://cosaslearning.com/source-code-of-pomodoro-timer/#google_vignette)
- [Valentino Gagliardi](https://www.valentinog.com/)
- [Djangoheroes](https://djangoheroes.org/)
- [Kulturbanause](https://kulturbanause.de/)
- Sololearn (App)
- Programming Hub (App)

### Content & Media
- All written content authored by the project developer
- No third-party images used (text-only interface)
- Bell sound from [Mixkit](https://mixkit.co/free-sound-effects/bell/)
- [Super Productivity](https://super-productivity.com/blog/pomodoro-technique-for-coders/)
- [Flown](https://flown.com/blog/adhd/how-to-focus-when-you-have-adhd)
- [Priory](https://www.priorygroup.com/blog/how-to-focus-and-manage-time-with-adhd)
- [AuDHD Psychiatry](https://www.audhdpsychiatry.co.uk/adhd-study-hacks/)
- [dr.carrie](https://www.drcarriejackson.com/blog/study-tips-for-the-neurodivergent-brain)
- [sunsama](https://www.sunsama.com/blog/how-to-focus-better-with-adhd)




