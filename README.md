# Steady Focus
A lightweight productivity web application featuring a public blog, visitor idea submissions, personal task management, and a built-in Pomodoro timer.

[Live Demo](https://steady-focus-bc183b5c3b1f.herokuapp.com/) <br>
[Repository](https://github.com/JenE87/steady_focus)

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

## ERD & Wireframes
### ERD
<img width="1052" height="662" alt="ERD_Steady_Focus" src="https://github.com/user-attachments/assets/376b48c2-6d84-4a05-84f4-176891baafa1" />

### Wireframes
#### Homepage (Mobile & Desktop)
<img width="1522" height="1001" alt="Screenshot 2025-12-16 182626" src="https://github.com/user-attachments/assets/2386f753-b719-40de-a45d-fa0d6f8ac5f2" />
<img width="1882" height="608" alt="Screenshot 2025-12-16 183034" src="https://github.com/user-attachments/assets/a3f413ea-ea62-4d9f-bcbb-4bbc8d7c6557" />
**Purpose**
The homepage introduces *Steady Focus* and communicates its core goal: helping users find focus through mindful task management and timed work sessions, while offering access to a public productivity blog.

**Layout & Responsiveness**
- **Mobile**
   - Content is stacked vertically for easy scrolling.
   - Primary call-to-action buttons (*Log In*, *Sign Up*, *Browse Blog*) are placed prominently near the top.
   - Blog posts appear as full-width cards to maximise readability on small screens.
- **Desktop**
   - Layout expands horizontally to make better use of screen space.
   - Blog posts are displayed in a multi-column grid for quick scanning.
   - Navigation links and authentication buttons are always visible in the top bar.

**Key Elements**
- Clear hero section with tagline and short explanatory text.
- Prominent call-to-action buttons to guide new users.
- *Latest Posts* section showcasing recent blog content.
- Blog cards include:
   - Title
   - Publication date
   - Short excerpt (or first 140 characters)
   - *Read more* button
- Pagination controls allow users to browse older posts.
- *Submit a Blog Idea* option encourages community participation.

**User Experience Considerations**
- Consistent visual hierarchy across devices reduces cognitive load.
- Minimalist layout supports focus and readability.
- Navigation remains predictable and accessible on both mobile and desktop.
- Responsive design ensures no loss of functionality on smaller screens.

#### Homepage Authenticated State (Mobile)
<img width="823" height="390" alt="Screenshot 2025-12-16 191034" src="https://github.com/user-attachments/assets/c54ae5b8-e63a-4ca5-ac4f-7c49086e4817" />
These wireframes illustrate how the homepage adapts once a user is logged in.

**Key Differences from Guest View**
- A success message confirms successful login, providing clear user feedback.
- Call-to-action buttons change to user-relevant actions (*View Tasks*, *Use Timer*, *Browse Blog*).
- The navigation menu expands to include authenticated-only links (*Tasks*, *Logout*).
- The username is displayed in the header to reinforce user context.

**Design Rationale**
- Immediate feedback builds user confidence after authentication.
- Navigation prioritises core productivity features for returning users.
- Menu toggle ensures functionality remains accessible on small screens without clutter

#### The Blog List (Mobile & Desktop)
<img width="1167" height="755" alt="Screenshot 2025-12-16 191711" src="https://github.com/user-attachments/assets/9c3d3c8e-27fc-4835-b68d-9fcb876ba2fb" />
<img width="1874" height="595" alt="Screenshot 2025-12-16 191735" src="https://github.com/user-attachments/assets/0233f951-af59-46ab-a3b2-fce016c9ab9f" />
**Purpose**
**Layout & Responsiveness**
- **Mobile**
   - 
- **Desktop**
**Key Elements**
**User Experience Considerations**

#### The Blog Detail Page (Mobile & Desktop)
<img width="1370" height="669" alt="Screenshot 2025-12-16 192544" src="https://github.com/user-attachments/assets/470ed6b2-e640-41fe-93ac-354932c37e5d" />
**Purpose**
**Layout & Responsiveness**
- **Mobile**
   - 
- **Desktop**
**Key Elements**
**User Experience Considerations**

#### Pomodoro Timer (Focus Timer) (Mobile & Desktop)
<img width="1355" height="670" alt="Screenshot 2025-12-16 191824" src="https://github.com/user-attachments/assets/0a71c5e5-0681-47d9-b275-05026576813f" />
<img width="980" height="597" alt="Screenshot 2025-12-16 191832" src="https://github.com/user-attachments/assets/e4a8aecc-bfcf-496f-a743-6ac78218c8e1" />
**Purpose**
**Layout & Responsiveness**
- **Mobile**
   - 
- **Desktop**
**Key Elements**
**User Experience Considerations**

#### Task List (Mobile & Desktop)
<img width="1358" height="658" alt="Screenshot 2025-12-16 191911" src="https://github.com/user-attachments/assets/b938838a-ef6b-4a6e-9477-94db4342b791" />
<img width="946" height="586" alt="Screenshot 2025-12-16 191918" src="https://github.com/user-attachments/assets/d6d91fee-e054-4e76-8eb2-5530dd75d412" />
**Purpose**
**Layout & Responsiveness**
- **Mobile**
   - 
- **Desktop**
**Key Elements**
**User Experience Considerations**

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
| Validator | Result |
|----------|--------|
| HTML Validator (W3C) | Pass (no critical errors)* |
| CSS Validator (W3C Jigsaw) | Pass |
| JSHint JavaScript | Pass |
| WAVE® Evaluation Tool (Web Accessibility) | No major contrast/errors |
| PEP8 Python Validator| Pass |

*Note: The deployed application was validated using the W3C Markup Validation Service.
Initial validation errors were caused by multi-line anchor tags in Django templates, which the validator interpreted as malformed attributes.
These were resolved by restructuring anchor elements so that all attributes appear on a single line, resulting in a successful validation.

### Fixed Bug
**1. Server error (500) when submitting blog ideas in production**
- **Problem:** Submitting a blog idea worked locally but caused a server error on the deployed Heroku app.
- **Cause:** The database migration for the `Idea` model had not been applied to the production PostgreSQL database.
- **Fix:** The migration files were committed and database migrations were run manually on Heroku using the Heroku Dashboard console.
- **Learning:** Local database changes must always be migrated separately in production. Heroku does not automatically apply migrations.

**2. `{% static %}` template tag throwing errors**
- **Problem:** Some pages failed to load static files such as CSS and JavaScript.
- **Cause:** The `{% load static %}` tag was missing at the top of affected templates.
- **Fix:** Added `{% load static %}` directly below `{% extends "base.html" %}` in all templates that use static assets.
- **Learning:** Django template tags must be explicitly loaded in each template where they are used.

**3. `post_list()` got unexpected keyword argument template_name**
- **Problem:** The homepage caused an error when routing to the blog list view.
- **Cause:** Function-based views were incorrectly passed parameters intended for class-based views.
- **Fix:** Created a dedicated `home()` function-based view instead of reusing `post_list()`.
- **Learning:** Function-based and class-based views use different configuration patterns and should not be mixed.

**4. Navbar link not routing to homepage**
- **Problem:** Clicking the site logo did not reliably route to the homepage.
- **Cause:** The link pointed to / without a dedicated homepage view.
- **Fix:** Created a named home URL and updated the navbar link to use `{% url 'home' %}`.
- **Learning:** Named URLs are safer and clearer than hardcoded paths.

**5. Pagination not working in function-based views**
- **Problem:** Pagination links displayed but did not work correctly.
- **Cause:** Required pagination context variables were missing from the view or misspelled.
- **Fix:** Added (corrected) `page_obj`, `is_paginated`, and consistent context names.
- **Learning:** Pagination logic must be implemented explicitly when using function-based views.

**6. Audio notification not playing when Pomodoro timer completed**
- **Problem:** The bell sound did not play when the timer reached zero.
- **Cause:** The audio element ID in the HTML did not match the JavaScript reference.
- **Fix:** Standardised the ID between the template and JavaScript file.
- **Learning:** Front-end bugs often come from small mismatches between HTML and JavaScript.

**7. Pomodoro timer crashing at zero**
- **Problem:** The timer stopped working when it reached zero.
- **Cause:** JavaScript attempted to access DOM elements before the page had fully loaded.
- **Fix:** Wrapped DOM element selection inside a DOMContentLoaded event listener.
- **Learning:** JavaScript that interacts with HTML elements must wait until the DOM is ready.

**8. Django template tags failing inside external JavaScript files**
- **Problem:** Static paths defined inside `pomodoro.js` caused errors.
- **Cause:** Django does not process template tags inside static JavaScript files.
- **Fix:** Moved the audio element into the HTML template and referenced it via its DOM ID.
- **Learning:** Django template logic must remain in templates, not static files.

**9. CSS hover effects causing confusion on detail pages**
- **Problem:** Entire detail views visually “lifted” on hover.
- **Cause:** A global `.card:hover` rule applied to all cards, including single-item views.
- **Fix:** Introduced a `.no-hover-lift` class to selectively disable hover animations.
- **Learning:** Global CSS rules should be scoped carefully to avoid unintended side effects.

**10. Custom CSS not loading on deployed site**
- **Problem:** The deployed site appeared unstyled.
- **Cause:** The `staticfiles/` directory (generated by `collectstatic`) was mistakenly committed to Git.
- **Fix:** Removed the directory from version control, added it to `.gitignore`, and redeployed.
- **Learning:** Generated production folders should never be committed.

**11. Words breaking mid-letter inside Bootstrap cards**
- **Problem:** Long words split awkwardly across lines.
- **Cause:** Default browser word-breaking behaviour.
- **Fix:** Added CSS rules to prevent mid-word breaking and improve readability.
- **Learning:** Small CSS adjustments can significantly improve accessibility and readability.

**12. Inconsistent Lexend font and primary color across headings**
- **Problem:** Some headings and card titles did not consistently display the Lexend font or the primary color.
- **Cause:** Bootstrap’s default CSS had higher specificity on certain heading and card classes, which overrode global font-family and color rules.
- **Fix:** Increased CSS specificity by targeting nested elements through their parent classes, ensuring the Lexend font and primary color are applied consistently.
- **Learning:** CSS specificity can override global styles; carefully targeting elements ensures consistent branding and typography.

**13. Timer display wrapping onto two lines on very small screens**
- **Problem:** On very small mobile devies (≈ 2360px width), the Pomodoro timer digits wrapped onto two lines.
- **Cause:** The timer font size (`6rem`) was too large fofr narrow viewports.
- **Fix:** Added responsive CSS media queries to reduce the timer font size on smaller screens.
- **Learning:** Large typographic elements should be tested on the smallest common viewport sizes to ensure readability and layout stability.

**14. Filter and sort icons misaligned on desktop task list**
- **Problem:** Filter and sort icon appeared above their labels on desktop screens.
- **Cause:** A global CSS rule forced Font Awesome icons to `display: inline`, breaking alignment inside flex containers.
- **Fix:** Removed the global icon display override, allowing Font Awesome's inline-block behavior.
- **Learning:** Global CSS overrides can have unintended side effects across breakpoints and layouts.

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



