import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

def create_report():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Neo-Brutalist Palette (Oxblood, Mustard, Slate)
    COLOR_PRIMARY = RGBColor(91, 35, 33)      # Oxblood Maroon
    COLOR_MUSTARD = RGBColor(232, 154, 60)    # Mustard Yellow
    COLOR_MUTED = RGBColor(123, 79, 77)

    def set_heading_style(p, size=18, color=COLOR_PRIMARY, bold=True, space_before=16, space_after=6):
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        for run in p.runs:
            run.font.name = 'Calibri'
            run.font.size = Pt(size)
            run.font.bold = bold
            run.font.color.rgb = color

    def add_p(text, bold=False, italic=False, color=COLOR_PRIMARY, size=11, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
        return p

    # =========================================================================
    # COVER PAGE
    # =========================================================================
    p_org = doc.add_paragraph()
    p_org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_org = p_org.add_run("NAVIOTECH SOLUTION PVT. LTD.")
    r_org.font.size = Pt(13)
    r_org.font.bold = True
    r_org.font.color.rgb = COLOR_MUSTARD

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("INTERNSHIP PROJECT EVALUATION REPORT")
    r_sub.font.size = Pt(11)
    r_sub.font.color.rgb = COLOR_MUTED
    p_sub.paragraph_format.space_after = Pt(40)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("LIKE A BLOGGER")
    r_title.font.size = Pt(30)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY

    p_tag = doc.add_paragraph()
    p_tag.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_tag = p_tag.add_run("A Full-Stack Neo-Brutalist Web Application with CRUD Operations, Marquee Ticker, Search Filtering & Cloud Deployment")
    r_tag.font.size = Pt(13)
    r_tag.font.italic = True
    r_tag.font.color.rgb = COLOR_MUTED
    p_tag.paragraph_format.space_after = Pt(120)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.line_spacing = 1.3
    
    r = p_meta.add_run("Submitted By: ")
    r.bold = True
    p_meta.add_run("Software Engineering Intern\n")

    r = p_meta.add_run("GitHub Repository: ")
    r.bold = True
    p_meta.add_run("https://github.com/Ryzen2310/Blog\n")

    r = p_meta.add_run("Live Deployed URL: ")
    r.bold = True
    p_meta.add_run("https://like-a-blogger.vercel.app/\n")

    r = p_meta.add_run("Submission Deadline: ")
    r.bold = True
    p_meta.add_run("30th November 2026\n")

    r = p_meta.add_run("Submission To: ")
    r.bold = True
    p_meta.add_run("Academic Team, Naviotech Solution Pvt. Ltd. (info@naviotechsolution.com)")

    doc.add_page_break()

    # =========================================================================
    # EXECUTIVE SUMMARY
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("Executive Summary")
    set_heading_style(p, size=20, color=COLOR_PRIMARY)

    add_p(
        "This project report details the design, engineering, and deployment of the Like a Blogger Web Application, "
        "developed to fulfill the internship curriculum requirements prescribed by Naviotech Solution Pvt. Ltd. "
        "The project demonstrates practical proficiency across full-stack software development, architectural design patterns, "
        "relational data persistence, neo-brutalist tactile UI design, and cloud production deployment."
    )
    add_p(
        "The application strictly implements all assigned functional requirements: allowing users to compose and publish articles (Title + Content), "
        "view all publications chronologically in a responsive dual-column feed on the homepage, and perform full lifecycle modifications "
        "including editing and secure deletion. In addition to core CRUD capabilities, the platform integrates live keyword search filtering, "
        "author attribution, category classification, dynamic read-time estimations, view counter tracking, interactive like heart toggles, "
        "automated unit test verification, and neo-brutalist 3D offset drop-shadow aesthetics with an infinite marquee ticker."
    )

    # =========================================================================
    # CHAPTER 1: INTRODUCTION & PROJECT OBJECTIVES
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("1. Project Introduction & Objectives")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p("The project scope is driven by three foundational milestones specified in the internship brief:")
    add_p("1. Users can write posts (Title + Content): An interactive, validated form allowing content creators to publish structured articles.")
    add_p("2. Display all posts on homepage: A dynamic feed presenting all published records in reverse chronological order with excerpts, stats, and metadata.")
    add_p("3. Later add editing & deletion: Complete lifecycle management enabling authors to revise existing entries or safely delete outdated posts.")

    # =========================================================================
    # CHAPTER 2: TECHNOLOGY STACK & JUSTIFICATION
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("2. Technology Stack & Technical Justification")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Layer"
    hdr_cells[1].text = "Technology"
    hdr_cells[2].text = "Justification"
    for cell in hdr_cells:
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = COLOR_PRIMARY

    tech_data = [
        ("Backend Language", "Python 3.12", "Clean syntax, exceptional standard library support, and industry standard for web services."),
        ("Web Framework", "Flask 3.x", "Lightweight micro-framework offering explicit routing and request handling without restrictive boilerplate."),
        ("Database Engine", "SQLite 3", "Serverless, ACID-compliant relational database requiring zero external daemons while supporting robust SQL."),
        ("Templating Engine", "Jinja2", "Server-side HTML template inheritance, dynamic loops, and built-in contextual XSS escaping."),
        ("Frontend Styles", "Neo-Brutalist CSS3", "Tactile 3D offset drop-shadows, marquee ticker ribbon, floating capsule navbar, and responsive CSS Grid."),
        ("Automated Testing", "Python unittest", "Standard verification suite ensuring continuous integration and regression protection across 7 tests."),
        ("Cloud Deployment", "Vercel Serverless", "High-availability edge hosting connected directly to GitHub with instant automated redeployments.")
    ]

    for layer, tech, just in tech_data:
        row_cells = table.add_row().cells
        row_cells[0].text = layer
        row_cells[1].text = tech
        row_cells[2].text = just

    # =========================================================================
    # CHAPTER 3: SYSTEM ARCHITECTURE & DATABASE DESIGN
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("3. System Architecture & Database Design")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p(
        "The project implements a decoupled Model-View-Controller (MVC) architecture:\n"
        "• Model (database.py): Manages SQLite connections, schema migrations, view counts, like counters, and parameterized database queries.\n"
        "• Controller (app.py): Handles HTTP endpoints (GET, POST), validates user input payloads, manages like toggles, session flash feedback, and routes execution flow.\n"
        "• View (templates/ & static/style.css): Jinja2 templates and custom neo-brutalist CSS delivering an editorial zine layout."
    )

    add_p("Relational Database Schema (posts table):", bold=True)
    db_table = doc.add_table(rows=1, cols=4)
    db_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    d_hdr = db_table.rows[0].cells
    d_hdr[0].text = "Column"
    d_hdr[1].text = "Data Type"
    d_hdr[2].text = "Constraints"
    d_hdr[3].text = "Description"
    for cell in d_hdr:
        for p in cell.paragraphs:
            for run in p.runs:
                run.font.bold = True
                run.font.color.rgb = COLOR_PRIMARY

    schema_data = [
        ("id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique post identifier"),
        ("title", "TEXT", "NOT NULL", "Headline of the article"),
        ("content", "TEXT", "NOT NULL", "Full body text of the article"),
        ("author", "TEXT", "DEFAULT 'Author'", "Author signature or attribution"),
        ("tag", "TEXT", "DEFAULT 'General'", "Category classification (Content Creation, etc.)"),
        ("views", "INTEGER", "DEFAULT 1", "Total article view counter"),
        ("likes", "INTEGER", "DEFAULT 0", "Interactive heart likes counter"),
        ("created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Initial publishing timestamp"),
        ("updated_at", "TIMESTAMP", "NULLABLE", "Timestamp of most recent revision")
    ]

    for col, dtype, constr, desc in schema_data:
        row = db_table.add_row().cells
        row[0].text = col
        row[1].text = dtype
        row[2].text = constr
        row[3].text = desc

    # =========================================================================
    # CHAPTER 4: IMPLEMENTATION & APPLICATION ROUTES
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("4. Implementation Details & Application Routes")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p("The web application exposes RESTful endpoints supporting full CRUD operations:")
    add_p("• GET / : Fetches all posts sorted newest to oldest. Supports optional query parameter (?q=keyword) to filter posts across title, content, author, or category.")
    add_p("• GET & POST /create : Renders creation form (GET) and processes new post submissions (POST) with server-side validation rejecting empty titles or content.")
    add_p("• GET /post/<id> : Displays the full article, metadata, author avatar badge, view counter, interactive like button, and management actions.")
    add_p("• GET & POST /post/<id>/edit : Renders pre-populated edit form (GET) and saves revisions (POST) with updated_at timestamping.")
    add_p("• POST /post/<id>/delete : Protected endpoint executing permanent record deletion with interactive browser confirmation dialogs.")
    add_p("• POST /post/<id>/like : Increments post likes dynamically.")

    # =========================================================================
    # CHAPTER 5: TESTING & VERIFICATION
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("5. Automated Testing & Verification")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p(
        "A formal test suite (test_app.py) was developed using Python's standard unittest library. "
        "The test harness configures a temporary in-memory/test database environment to validate all endpoints before deployment."
    )
    add_p("Test Suite Results (7 tests passing):", bold=True)
    add_p("✓ test_empty_homepage: Verifies proper zero-state handling when no posts exist in the database.")
    add_p("✓ test_create_and_view_post_with_author_and_tag: Confirms complete author attribution and post creation flow.")
    add_p("✓ test_search_functionality: Tests multi-field keyword query matching across titles and author names.")
    add_p("✓ test_like_post_functionality: Tests the like counter incrementation upon submission.")
    add_p("✓ test_edit_post: Verifies field pre-population, content revision, and database record mutation.")
    add_p("✓ test_delete_post: Tests record deletion and removal confirmation from the database.")
    add_p("✓ test_validation_empty_fields: Asserts that blank titles or empty content are strictly rejected with error banners.")
    add_p("Summary: 7 passed in 0.164 seconds (100% Pass Rate).", bold=True, color=COLOR_MUSTARD)

    # =========================================================================
    # CHAPTER 6: CLOUD DEPLOYMENT & PRODUCTION URLS
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("6. Cloud Deployment & Public URLs")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p("Production Links for Evaluation:", bold=True)
    add_p("• Live Application URL: https://like-a-blogger.vercel.app/")
    add_p("• GitHub Source Repository: https://github.com/Ryzen2310/Blog")
    add_p("• PowerPoint Presentation: presentation.pptx (10 slides with comprehensive architecture overview)")
    add_p("• Presentation Script: PRESENTATION_SCRIPT.md (word-for-word speaker notes)")

    # =========================================================================
    # CHAPTER 7: KEY FINDINGS & CONCLUSION
    # =========================================================================
    p = doc.add_paragraph()
    p.add_run("7. Key Findings, Challenges & Conclusion")
    set_heading_style(p, size=18, color=COLOR_PRIMARY)

    add_p(
        "Key Learnings:\n"
        "1. Full-Stack Lifecycle: Acquired deep practical insight into HTTP client-server interactions, payload serialization, and status codes.\n"
        "2. Database Integrity: Mastered non-destructive schema migrations and parameterized query security to eliminate injection threats.\n"
        "3. Tactile Neo-Brutalist UI: Learned how 3D offset drop shadows, pill capsules, marquee ribbons, and high-contrast typography create a memorable physical zine feel.\n"
        "4. CI/CD & Deployment: Successfully diagnosed and resolved cloud serverless root directory mappings on Vercel."
    )
    add_p(
        "Conclusion: The Like a Blogger project successfully fulfills all curriculum expectations set by Naviotech Solution Pvt. Ltd., "
        "providing a solid, professionally documented foundation ready for evaluation and internship certification."
    )

    output_path = os.path.join(os.path.dirname(__file__), 'Project_Report.docx')
    doc.save(output_path)
    print(f"Project report successfully created at: {output_path}")

if __name__ == '__main__':
    create_report()
