# ⚡ Nexus Blog — Modern Full-Stack Web Application

A sleek, responsive, and animated web application built with **Python**, **Flask**, and **SQLite**. Featuring an obsidian dark aesthetic accented with **electric blue and neon purple gradients**, this project was developed as an internship evaluation assignment focusing on clean **MVC** architecture, full **CRUD** operations, a **multi-column card grid**, and a **real-time search bar**.

---

## 📌 Project Overview

This application fulfills all core requirements from the internship specification, along with rich modern design enhancements:
1. **Write Posts:** Users can compose articles with a title, body content, author signature, and category tag.
2. **Homepage Feed:** All posts are displayed on a **side-by-side 2-column card grid** with excerpts, read-time estimates, and timestamps.
3. **Edit & Delete:** Full lifecycle management allowing authors to revise articles or safely remove them.
4. **Keyword Search Bar:** Live search functionality filtering articles across titles, body content, author names, and category tags.

---

## 🎨 Design Theme: Blue, Purple & Obsidian Dark

- **Palette:** Deep obsidian midnight black (`#090D16`), elevated dark cards (`#131D31`), electric blue accents (`#3B82F6`), and neon purple highlights (`#8B5CF6`).
- **Smooth Animations:**
  - `@keyframes fadeInUp`: Staggered card entrance animations as you load the page.
  - Glowing hover elevations (`box-shadow: 0 10px 30px -10px rgba(139, 92, 246, 0.35)`).
  - Animated top gradient glow strip with infinite background flow.
  - Interactive focus glow on search and form inputs.
- **Side-by-Side Cards:** Modern CSS Grid layout displaying stories in dual columns on desktop and cleanly adapting to single-column on mobile.
- **Glassmorphism:** Navigation bar featuring backdrop-filter blur (`backdrop-filter: blur(16px)`).

---

## 🚀 Key Features

- **Side-by-Side Card Grid:** 2-column responsive layout showcasing posts side-by-side.
- **Keyword Search Filter:** Search posts by any keyword across title, content, author, or tag with match counts and a quick clear button.
- **Author Attribution & Badges:** Displays who wrote the post (e.g. *Alex Chen*, *Jordan Lee*) and clean category tags (e.g. *Tech*, *Design*, *Coding*, *Career*, *Thoughts*).
- **Read-Time Calculator:** Automatically calculates estimated reading minutes based on word count.
- **Interactive Deletion Safeguards:** Browser confirmation prevents accidental notice removal.
- **Automated Test Suite:** 6 comprehensive unit tests verifying routing, CRUD operations, input validation, and search filtering.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Language** | Python 3.12 | Core programming language |
| **Web Framework** | Flask 3.x | Lightweight framework for routing, query parsing, and session flash alerts |
| **Database** | SQLite 3 | Embedded, file-based relational database with automated schema migration |
| **Templating** | Jinja2 | Dynamic HTML rendering with loop filters and XSS protection |
| **Frontend** | HTML5 & CSS3 | Custom CSS Grid, Flexbox, Keyframe Animations, Glassmorphism (no heavy JS libraries) |
| **Testing** | `unittest` | Python's standard automated testing suite |

---

## 📂 Project Structure

```text
Blog project/
├── app.py                   # Main Flask application and URL routing
├── database.py              # SQLite connection manager, migration, and CRUD queries
├── seed.py                  # Script to populate sample articles
├── test_app.py              # Automated unit test suite (6 passing tests)
├── generate_presentation.py # Script generating the 10-slide PowerPoint presentation
├── presentation.pptx        # 10-slide presentation deck for internship evaluation
├── PRESENTATION_SCRIPT.md   # Word-for-word presentation speech and speaker notes
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignored version control files
├── README.md                # Project documentation
├── static/
│   └── style.css            # Custom Blue, Purple & Obsidian animated stylesheet
└── templates/
    ├── base.html            # Master layout with animated glow trim, glassmorphic navbar, and flash alerts
    ├── index.html           # Feed with search bar and 2-column animated cards
    ├── post.html            # Single article detail view
    ├── create.html          # New post form with author & tag inputs
    ├── edit.html            # Edit post form with pre-populated values
    └── 404.html             # Custom 404 error page
```

---

## 🚦 Getting Started

### 1. Run the Application
Make sure you are in the project folder and run:
```powershell
D:\Code\Python\python.exe app.py
```
Open your browser and navigate to: **`http://127.0.0.1:5000/`**

### 2. (Optional) Run Automated Tests
```powershell
D:\Code\Python\python.exe -m unittest test_app.py
```
Output:
```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.137s

OK
```

---

## 🗄️ Database Schema

The database uses a relational table named `posts`:

| Column Name | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique post ID |
| `title` | `TEXT` | `NOT NULL` | Article headline |
| `content` | `TEXT` | `NOT NULL` | Full article text |
| `author` | `TEXT` | `DEFAULT 'Author'` | Name of the author |
| `tag` | `TEXT` | `DEFAULT 'General'` | Category tag (Tech, Design, etc.) |
| `created_at` | `TIMESTAMP` | `DEFAULT CURRENT_TIMESTAMP` | Publishing timestamp |
| `updated_at` | `TIMESTAMP` | `NULLABLE` | Timestamp of last modification |

---

## 🌐 Application Endpoints

| Endpoint | HTTP Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Homepage: shows all posts or filtered search results (`?q=...`) |
| `/create` | `GET`, `POST` | Renders creation form (`GET`) and publishes new post (`POST`) |
| `/post/<id>` | `GET` | Displays full content, metadata, and actions for post `<id>` |
| `/post/<id>/edit` | `GET`, `POST` | Renders edit sheet (`GET`) and saves revisions (`POST`) |
| `/post/<id>/delete` | `POST` | Safely removes post `<id>` with confirmation prompt |

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
