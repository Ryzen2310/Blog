# ✦ Like a Blogger — Full-Stack Web Application

A modern, tactile, and responsive editorial zine web application built with **Python**, **Flask**, and **SQLite**. Inspired by the trending **Neo-Brutalist** aesthetic (chunky 3D offset drop-shadows, powder-sage blue background, oxblood typography, and continuous marquee ticker ribbon), this project was developed as an internship evaluation assignment focusing on clean **MVC** architecture, full **CRUD** operations, a **dual-column card grid**, **live keyword search**, **view tracking**, and **interactive likes**.

---

## 📌 Project Overview

This application fulfills all core requirements from the internship specification, along with rich modern design enhancements:
1. **Write Posts:** Users can compose articles with a headline, body content, author signature, and category tag.
2. **Homepage Feed:** All stories are displayed on a **side-by-side 2-column zine card grid** with excerpts, read-time estimates, view counts, and likes.
3. **Edit & Delete:** Full lifecycle management allowing authors to revise stories or safely remove them with confirmation prompts.
4. **Keyword Search Bar:** Live search functionality filtering stories across headlines, body content, author names, and category tags.
5. **Interactive Engagement:** Real-time view count tracking and one-click like heart buttons.

---

## 🎨 Design Theme: Neo-Brutalist Retro-Editorial

- **Palette:** Soft powder-sage duck-egg blue (`#BCD8D8`), warm cream off-white cards (`#FCFAF7`), deep oxblood maroon / burgundy text and borders (`#5B2321`), and warm mustard / ochre yellow CTA buttons (`#E89A3C`).
- **Tactile 3D Details:** Solid dark offset drop-shadows (`4px 4px 0 #5B2321`) that depress when clicked (`1px 1px 0 #5B2321`).
- **Continuous Marquee Ticker:** An infinite scrolling ribbon at the top: `✦ WRITE. POST. REPEAT. ➔ LIKE A BLOGGER ✦`.
- **Floating Capsule Navbar:** A pill-shaped capsule navigation bar anchored near the top with monogram logo badge ("L").
- **Typography:** Expressive display headlines with Google Font *Syne* paired with geometric metadata typography (*Space Grotesk*) and comfortable reading body text (*Plus Jakarta Sans*).

---

## 🚀 Key Features

- **Side-by-Side Zine Card Grid:** 2-column responsive layout showcasing stories side-by-side.
- **Keyword Search Filter:** Search stories by any keyword across title, content, author, or tag with match counts and a quick clear button.
- **Story Stats & Interactions:** Built-in view counter (`👁️`) and interactive heart like button (`❤️`).
- **Author Attribution & Badges:** Displays who wrote the post and category tags with status dots (e.g. `● Content Creation`, `● Design & Style`, `● Technology`).
- **Read-Time Calculator:** Automatically calculates estimated reading minutes based on word count.
- **Interactive Deletion Safeguards:** Browser confirmation prevents accidental notice removal.
- **Automated Test Suite:** 7 comprehensive unit tests verifying routing, CRUD operations, like toggles, input validation, and search filtering.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Backend Language** | Python 3.12 | Core programming language |
| **Web Framework** | Flask 3.x | Lightweight framework for routing, query parsing, like counters, and session flash alerts |
| **Database** | SQLite 3 | Embedded, file-based relational database with automated schema migration |
| **Templating** | Jinja2 | Dynamic HTML rendering with loop filters and XSS protection |
| **Frontend** | Neo-Brutalist CSS3 | Custom CSS Grid, 3D offset drop shadows, marquee ticker, floating capsule header |
| **Testing** | `unittest` | Python's standard automated testing suite (7 tests passing) |

---

## 📂 Project Structure

```text
Blog project/
├── app.py                   # Main Flask application and URL routing
├── database.py              # SQLite connection manager, migration, view & like tracking
├── seed.py                  # Script to populate sample editorial stories
├── test_app.py              # Automated unit test suite (7 passing tests)
├── generate_presentation.py # Script generating the 10-slide PowerPoint presentation
├── presentation.pptx        # 10-slide presentation deck for internship evaluation
├── PRESENTATION_SCRIPT.md   # Word-for-word presentation speech and speaker notes
├── generate_report.py       # Script generating formal Project Report Word document
├── Project_Report.docx      # Formal Project Report for internship evaluation
├── PROJECT_REPORT.md        # Comprehensive Markdown Project Report
├── requirements.txt         # Project dependencies
├── .gitignore               # Ignored version control files
├── README.md                # Project documentation
├── static/
│   └── style.css            # Custom Neo-Brutalist Retro-Editorial stylesheet
└── templates/
    ├── base.html            # Master layout with marquee ticker, capsule navbar, and footer
    ├── index.html           # Feed with search bar and 2-column neo-brutalist cards
    ├── post.html            # Full editorial zine article view
    ├── create.html          # New story form with author & tag inputs
    ├── edit.html            # Edit story form with pre-populated values
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

### 2. Run Automated Tests
```powershell
D:\Code\Python\python.exe -m unittest test_app.py
```
Output:
```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.164s

OK
```

---

## 🗄️ Database Schema

The database uses a relational table named `posts`:

| Column Name | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Unique post ID |
| `title` | `TEXT` | `NOT NULL` | Story headline |
| `content` | `TEXT` | `NOT NULL` | Full story text |
| `author` | `TEXT` | `DEFAULT 'Author'` | Name of the author |
| `tag` | `TEXT` | `DEFAULT 'General'` | Category tag (Content Creation, etc.) |
| `views` | `INTEGER` | `DEFAULT 1` | Article view count |
| `likes` | `INTEGER` | `DEFAULT 0` | Interactive like count |
| `created_at` | `TIMESTAMP` | `DEFAULT CURRENT_TIMESTAMP` | Publishing timestamp |
| `updated_at` | `TIMESTAMP` | `NULLABLE` | Timestamp of last modification |

---

## 🌐 Application Endpoints

| Endpoint | HTTP Method | Description |
| :--- | :--- | :--- |
| `/` | `GET` | Homepage: shows all stories or filtered search results (`?q=...`) |
| `/create` | `GET`, `POST` | Renders creation form (`GET`) and publishes new story (`POST`) |
| `/post/<id>` | `GET` | Displays full content, metadata, view count, like button, and actions |
| `/post/<id>/edit` | `GET`, `POST` | Renders edit sheet (`GET`) and saves revisions (`POST`) |
| `/post/<id>/delete` | `POST` | Safely removes post `<id>` with confirmation prompt |
| `/post/<id>/like` | `POST` | Increments article like counter dynamically |

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
