# 📘 Internship Project Report: Like a Blogger Web Application

**Company:** Naviotech Solution Pvt. Ltd.  
**Department:** Academic & Evaluation Team  
**Project:** Like a Blogger (Full-Stack Python/Flask Web Application)  
**Submission Deadline:** 30th November 2026  
**Repository:** [https://github.com/Ryzen2310/Blog](https://github.com/Ryzen2310/Blog)  
**Live Production URL:** [https://like-a-blogger.vercel.app/](https://like-a-blogger.vercel.app/)  

---

## Executive Summary

This project report documents the design, implementation, testing, and deployment of **Like a Blogger**, an interactive full-stack web application developed to fulfill the internship curriculum requirements prescribed by **Naviotech Solution Pvt. Ltd.**

The project demonstrates practical mastery of the **Model-View-Controller (MVC)** architectural pattern, relational database persistence with SQLite, comprehensive CRUD lifecycle management, a neo-brutalist retro-editorial zine design, live keyword search filtering, view count tracking, interactive like counters, automated test verification, and production cloud deployment on Vercel.

---

## 1. Project Objectives & Core Requirements

The project satisfies all three mandatory taglines outlined in the internship project allocation:
1. **Users can write posts (Title + Content):** An intuitive, validated submission form allowing users to publish structured articles.
2. **Display all posts on homepage:** A dynamic, reverse-chronological feed showcasing all articles in a responsive dual-column grid with excerpts, author attribution, read-time estimates, view counts, and likes.
3. **Later add editing & deletion:** Full administrative lifecycle control enabling authors to revise existing entries or safely remove outdated articles with confirmation prompts.

### Key Technical Goals:
- **Modularity:** Strict separation of data persistence (`database.py`), server routing logic (`app.py`), and presentation (`templates/` and `static/style.css`).
- **Security:** 100% parameterized SQL queries protecting against SQL Injection attacks.
- **Verification:** An automated unit testing suite (`test_app.py`) verifying all endpoints, like toggles, and error states with a 100% pass rate.
- **Neo-Brutalist User Experience:** Tactile 3D offset drop-shadows, powder-sage and oxblood burgundy aesthetic, animated continuous marquee ticker, and floating capsule navbar.

---

## 2. Technology Stack & Justification

| Component | Technology | Technical Justification |
| :--- | :--- | :--- |
| **Backend Language** | Python 3.12 | Industry standard for readability, reliability, and rich standard library ecosystems. |
| **Web Framework** | Flask 3.x | Lightweight micro-framework enabling clean, explicit URL routing, like counters, and session flash feedback. |
| **Database** | SQLite 3 | Serverless, ACID-compliant relational database engine requiring zero external configuration. |
| **Templating** | Jinja2 | Dynamic HTML rendering with template inheritance and automatic XSS escaping. |
| **Frontend UI** | Neo-Brutalist CSS3 | Custom CSS Grid, 3D offset drop shadows, continuous marquee ticker, and floating pill capsule header. |
| **Testing** | `unittest` | Python's standard test framework guaranteeing regression protection across 7 automated tests. |
| **Cloud Hosting** | Vercel Serverless | Production edge hosting providing automated GitHub CI/CD deployments and live global availability. |

---

## 3. System Architecture & Database Design

### Model-View-Controller (MVC) Pattern:
- **Model (`database.py`):** Manages SQLite connections, dynamic cloud environment detection, view increments, like toggles, and execution of parameterized queries.
- **Controller (`app.py`):** Parses incoming HTTP requests (GET, POST), executes input validation rules, handles like counters, emits flash feedback banners, and controls view rendering.
- **View (`templates/` & `static/style.css`):** Jinja2 templates and custom neo-brutalist CSS delivering an editorial zine layout.

### Relational Database Schema (`posts` Table):
```sql
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author TEXT DEFAULT 'Author',
    tag TEXT DEFAULT 'General',
    views INTEGER DEFAULT 1,
    likes INTEGER DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);
```

---

## 4. Application Routes & Functionality

| Route Endpoint | HTTP Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Homepage: fetches all articles ordered by date descending; supports `?q=...` keyword search. |
| `/create` | `GET`, `POST` | Renders creation form (`GET`) and saves new post (`POST`) with input validation. |
| `/post/<id>` | `GET` | Single article view displaying full content, author avatar badge, view counter, like button, and actions. |
| `/post/<id>/edit` | `GET`, `POST` | Pre-populates existing article data (`GET`) and saves revisions (`POST`). |
| `/post/<id>/delete` | `POST` | Safely removes post `<id>` with interactive confirmation prompt. |
| `/post/<id>/like` | `POST` | Increments article like counter dynamically. |

---

## 5. Automated Testing & Verification

A dedicated test suite was built in `test_app.py` using Python's standard `unittest` framework:
- **`test_empty_homepage`**: Asserts proper empty-state UI when no articles exist.
- **`test_create_and_view_post_with_author_and_tag`**: Confirms full post publishing flow and data presentation.
- **`test_search_functionality`**: Validates multi-field keyword filtering across titles and author names.
- **`test_like_post_functionality`**: Asserts that liking a post increments the like counter in the database.
- **`test_edit_post`**: Verifies pre-population and database mutation upon editing.
- **`test_delete_post`**: Confirms permanent record removal from the database.
- **`test_validation_empty_fields`**: Validates that blank titles or empty content are strictly rejected with user warning alerts.

**Result:** `Ran 7 tests in 0.164s — OK (100% Pass Rate)`.

---

## 6. Cloud Deployment & Public URLs

The application has been deployed live to Vercel's serverless production cloud:
- **Live URL:** [https://like-a-blogger.vercel.app/](https://like-a-blogger.vercel.app/)
- **GitHub Repository:** [https://github.com/Ryzen2310/Blog](https://github.com/Ryzen2310/Blog)
- **PowerPoint Presentation:** `presentation.pptx` (10-slide widescreen presentation deck)
- **Presentation Script:** `PRESENTATION_SCRIPT.md` (word-for-word talking points)

---

## 7. Key Findings & Conclusion

Throughout this internship project, the following core software engineering competencies were achieved:
1. **Full-Stack Competence:** Mastered the end-to-end request-response lifecycle from browser forms to relational tables.
2. **Database Integrity & Migrations:** Implemented automated schema evolution techniques without risking data corruption.
3. **Defensive Programming:** Enforced parameterized SQL execution to protect data against injection vulnerabilities.
4. **Cloud DevOps:** Successfully diagnosed and resolved cloud serverless root directory mappings on Vercel.

**Conclusion:** The Like a Blogger project is complete, verified, documented, and ready for formal evaluation by the Naviotech Solution Academic Team.
