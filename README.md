# Steady Focus
A lightweight productivity web app: public blog with visitor idea submissions, user task CRUD and a Pomodoro timer.

## Project purpose
Steady Focus helps users plan and run focused work sessions and collect/curate productivity content from visitors.

## Live demo
Heroku URL after deployment

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
<img width="1294" height="644" alt="ERD_Steady_Focus" src="https://github.com/user-attachments/assets/d135b172-f5c1-4189-9678-293390ac86f4" />

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
- **ChatGPT** - for planning, debugging, and documentation support

### Development & Services
- **VS Code** - IDE, code editor
- **Python virtual Environment (venv)**


## Design & Layout

## Testing
### Manual Testing
| Feature                           | Test Input                     | Expected Result               | Pass/Fail |
|-----------------------------------|--------------------------------|-------------------------------|-----------|
|      |                   |      |       |


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

### Unfixed Bugs
- **Words breaking mid-letter inside Bootsrap cards**
  - Cause: Browser default word splitting behaviour.
  - Initial Fix (does not solve bug entirely yet): Tried adding CSS `word-break: normal; overflow-wrap: break-word;` and refined clamping styles.
  - Bug improved, but not fixed yet

## Deployment
### Local Setup
### Version Control
### Heroku Deployment

## Credits
### Code
### Content & Media


