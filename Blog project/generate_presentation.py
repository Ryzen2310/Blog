import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Sleek Blue, Purple & Black Palette
    COLOR_PRIMARY = RGBColor(9, 13, 22)       # Deep Obsidian Black
    COLOR_BLUE = RGBColor(59, 130, 246)       # Electric Blue
    COLOR_PURPLE = RGBColor(139, 92, 246)     # Neon Purple
    COLOR_DARK = RGBColor(15, 23, 42)         # Deep Slate
    COLOR_MUTED = RGBColor(148, 163, 184)     # Medium Slate
    COLOR_BG_CARD = RGBColor(248, 250, 252)   # Card Fill
    COLOR_TEXT = RGBColor(15, 23, 42)

    blank_layout = prs.slide_layouts[6]

    def add_header(slide, title_text, category_text="INTERNSHIP PROJECT PRESENTATION"):
        cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11), Inches(0.4))
        tf_cat = cat_box.text_frame
        tf_cat.word_wrap = True
        p_cat = tf_cat.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = COLOR_PURPLE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.7), Inches(11.5), Inches(0.8))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(26)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_BLUE

    # =========================================================================
    # SLIDE 1: Title Slide
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    
    # Left decorative bar
    bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.4), Inches(7.5))
    bar.fill.solid()
    bar.fill.fore_color.rgb = COLOR_PURPLE
    bar.line.fill.background()

    t_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(11), Inches(4.5))
    tf1 = t_box.text_frame
    tf1.word_wrap = True
    
    p = tf1.paragraphs[0]
    p.text = "NEXUS BLOG: WEB APPLICATION"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p2 = tf1.add_paragraph()
    p2.text = "Full-Stack Development, Dual-Column Card Grid, Live Search & Modern Animations"
    p2.font.size = Pt(20)
    p2.font.color.rgb = COLOR_BLUE
    p2.space_before = Pt(12)

    p3 = tf1.add_paragraph()
    p3.text = "Internship Project Review & Key Findings  •  Blue, Purple & Obsidian Palette"
    p3.font.size = Pt(15)
    p3.font.color.rgb = COLOR_MUTED
    p3.space_before = Pt(24)

    p4 = tf1.add_paragraph()
    p4.text = "Presenter: Software Engineering Intern  |  Technology: Python 3.12 • Flask • SQLite • Modern CSS"
    p4.font.size = Pt(13)
    p4.font.bold = True
    p4.font.color.rgb = COLOR_DARK
    p4.space_before = Pt(30)

    # =========================================================================
    # SLIDE 2: Project Objectives & Core Requirements
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_header(slide2, "Project Objectives & Core Requirements", "01 / CONTEXT & GOALS")

    cards_data = [
        ("Requirement 1: Content Creation", "Users can compose and publish articles with a title, author name, category tag, and body content.", "✓ Author attribution\n✓ Category taxonomy\n✓ Instant feed publication"),
        ("Requirement 2: Side-by-Side Feed", "Display all posts in a responsive 2-column side-by-side card grid with animated entrances and live search.", "✓ Dual-column card grid\n✓ Live keyword search\n✓ Read-time estimates"),
        ("Requirement 3: Lifecycle Management", "Provide full administrative control allowing existing posts to be updated or permanently deleted.", "✓ Pre-populated edit forms\n✓ Deletion safety prompts\n✓ Status feedback alerts")
    ]

    for i, (title, desc, bullets) in enumerate(cards_data):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        width = Inches(3.7)
        height = Inches(4.8)

        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = COLOR_PURPLE
        card.line.width = Pt(1.5)

        tb = slide2.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p_ct = tf.paragraphs[0]
        p_ct.text = title
        p_ct.font.size = Pt(16)
        p_ct.font.bold = True
        p_ct.font.color.rgb = COLOR_PRIMARY

        p_cd = tf.add_paragraph()
        p_cd.text = desc
        p_cd.font.size = Pt(13)
        p_cd.font.color.rgb = COLOR_DARK
        p_cd.space_before = Pt(10)

        p_cb = tf.add_paragraph()
        p_cb.text = bullets
        p_cb.font.size = Pt(12)
        p_cb.font.color.rgb = COLOR_MUTED
        p_cb.space_before = Pt(16)

    # =========================================================================
    # SLIDE 3: Technology Stack & Justification
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_header(slide3, "Technology Stack & Technical Justification", "02 / TECH STACK")

    tech_items = [
        ("Python 3.12 (Core Language)", "Standard high-level backend language offering exceptional readability, speed, and standard libraries."),
        ("Flask 3.x (Web Framework)", "Lightweight micro-framework enabling flexible routing, query parameter handling, and session flash alerts."),
        ("SQLite 3 (Relational Storage)", "Zero-setup embedded database engine with automated schema migration and parameterized query safety."),
        ("Jinja2 (Dynamic Templating)", "Renders dynamic HTML views, loops, and conditional search banners with automatic XSS protection."),
        ("Semantic HTML5 & Modern CSS3", "Custom CSS Grid, Flexbox, glassmorphic blurs, and keyframe animations without external bloat."),
        ("Python Unittest (Verification)", "Automated test suite guaranteeing 100% test pass rate across routing, search filters, and CRUD logic.")
    ]

    for i, (title, reason) in enumerate(tech_items):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.8 + row * 1.65)
        width = Inches(5.6)
        height = Inches(1.4)

        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = RGBColor(226, 232, 240)
        card.line.width = Pt(1)

        tb = slide3.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(15)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_BLUE

        pr = tf.add_paragraph()
        pr.text = reason
        pr.font.size = Pt(12.5)
        pr.font.color.rgb = COLOR_DARK
        pr.space_before = Pt(4)

    # =========================================================================
    # SLIDE 4: System Architecture (MVC Pattern)
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_header(slide4, "System Architecture: MVC Design Pattern", "03 / ARCHITECTURE")

    mvc_blocks = [
        ("MODEL (database.py)", "Data Layer", "• Manages SQLite database connection\n• Executes SQL queries with LIKE filters for search\n• Performs non-destructive schema migrations\n• Enforces parameterized SQL safety"),
        ("CONTROLLER (app.py)", "Application Logic", "• Flask routing system mapping URLs to handlers\n• Parses search query parameter (?q=...)\n• Validates title & content constraints\n• Emits feedback flash banners"),
        ("VIEW (templates/ & style.css)", "Animated Interface", "• 2-column responsive card grid\n• Keyframe entrance & hover animations\n• Glassmorphic dark navbar & hero styling\n• Fully responsive mobile & tablet design")
    ]

    for i, (name, role, details) in enumerate(mvc_blocks):
        left = Inches(0.8 + i * 3.95)
        top = Inches(1.8)
        width = Inches(3.7)
        height = Inches(4.8)

        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = COLOR_BLUE
        card.line.width = Pt(1.5)

        tb = slide4.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = tb.text_frame
        tf.word_wrap = True

        pn = tf.paragraphs[0]
        pn.text = name
        pn.font.size = Pt(16)
        pn.font.bold = True
        pn.font.color.rgb = COLOR_PRIMARY

        prole = tf.add_paragraph()
        prole.text = role.upper()
        prole.font.size = Pt(11)
        prole.font.bold = True
        prole.font.color.rgb = COLOR_PURPLE
        prole.space_before = Pt(2)

        pdet = tf.add_paragraph()
        pdet.text = details
        pdet.font.size = Pt(12.5)
        pdet.font.color.rgb = COLOR_DARK
        pdet.space_before = Pt(14)

    # =========================================================================
    # SLIDE 5: Database Design & Schema
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_header(slide5, "Database Schema & Migration", "04 / DATABASE DESIGN")

    left_tb = slide5.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(6.5), Inches(4.8))
    tf5_l = left_tb.text_frame
    tf5_l.word_wrap = True

    p = tf5_l.paragraphs[0]
    p.text = "Relational Table: 'posts'"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    schema_rows = [
        ("id", "INTEGER", "PRIMARY KEY AUTOINCREMENT", "Unique post identifier"),
        ("title", "TEXT", "NOT NULL", "Headline of the article"),
        ("content", "TEXT", "NOT NULL", "Full body text of the post"),
        ("author", "TEXT", "DEFAULT 'Author'", "Author or writer attribution"),
        ("tag", "TEXT", "DEFAULT 'General'", "Category tag (Tech, Design, etc.)"),
        ("created_at", "TIMESTAMP", "DEFAULT CURRENT_TIMESTAMP", "Initial publishing timestamp"),
        ("updated_at", "TIMESTAMP", "NULLABLE", "Timestamp of most recent revision")
    ]

    for col, ctype, constr, desc in schema_rows:
        p_row = tf5_l.add_paragraph()
        p_row.text = f"• {col} ({ctype}) — {constr}\n   {desc}"
        p_row.font.size = Pt(12)
        p_row.font.color.rgb = COLOR_DARK
        p_row.space_before = Pt(5)

    right_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.7), Inches(1.8), Inches(4.8), Inches(4.8))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = COLOR_BG_CARD
    right_card.line.color.rgb = COLOR_PURPLE
    right_card.line.width = Pt(1.5)

    right_tb = slide5.shapes.add_textbox(Inches(8.0), Inches(2.0), Inches(4.2), Inches(4.4))
    tf5_r = right_tb.text_frame
    tf5_r.word_wrap = True

    p_rt = tf5_r.paragraphs[0]
    p_rt.text = "Persistence & Migration Highlights"
    p_rt.font.size = Pt(17)
    p_rt.font.bold = True
    p_rt.font.color.rgb = COLOR_PRIMARY

    bullets = [
        ("Automated Migration", "The application runs PRAGMA table_info to safely add 'author' and 'tag' columns to existing databases."),
        ("Multi-Field Search Query", "Parameterized LIKE query searches across title, content, author, and category tag concurrently."),
        ("Parameterized SQL Protection", "All variables bound through ? syntax to protect against SQL injection."),
        ("sqlite3.Row Dictionary Mapping", "Enables clean column access row['author'] throughout controllers and templates.")
    ]

    for b_title, b_desc in bullets:
        pb = tf5_r.add_paragraph()
        pb.text = f"✓ {b_title}:\n   {b_desc}"
        pb.font.size = Pt(11.5)
        pb.font.color.rgb = COLOR_DARK
        pb.space_before = Pt(8)

    # =========================================================================
    # SLIDE 6: Core Features: Writing & Viewing Posts
    # =========================================================================
    slide6 = prs.slides.add_slide(blank_layout)
    add_header(slide6, "Core Features: Writing & Searchable Feed", "05 / CORE FEATURES")

    f1 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    f1.fill.solid()
    f1.fill.fore_color.rgb = COLOR_BG_CARD
    f1.line.color.rgb = RGBColor(226, 232, 240)
    f1.line.width = Pt(1)

    tb_f1 = slide6.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_f1 = tb_f1.text_frame
    tf_f1.word_wrap = True

    p = tf_f1.paragraphs[0]
    p.text = "Article Creation & Authorship"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    f1_points = [
        ("Author & Tag Inputs", "Authors specify their signature and select categories (Tech, Design, Coding, Career, Thoughts)."),
        ("Server Validation", "Safeguards reject empty title or content submissions with immediate user warning alerts."),
        ("Dynamic Read Time", "Calculates reading duration automatically from total word count."),
        ("Feedback Redirection", "Routes back to feed with a cheerful confirmation notification.")
    ]
    for pt, pd in f1_points:
        p_pt = tf_f1.add_paragraph()
        p_pt.text = f"• {pt}: {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(8)

    f2 = slide6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    f2.fill.solid()
    f2.fill.fore_color.rgb = COLOR_BG_CARD
    f2.line.color.rgb = RGBColor(226, 232, 240)
    f2.line.width = Pt(1)

    tb_f2 = slide6.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.2))
    tf_f2 = tb_f2.text_frame
    tf_f2.word_wrap = True

    p = tf_f2.paragraphs[0]
    p.text = "Side-by-Side Feed & Search Bar"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    f2_points = [
        ("Dual-Column Grid", "Articles render side-by-side using CSS Grid (repeat(auto-fill, minmax(340px, 1fr)))."),
        ("Live Keyword Search", "Instantly filters articles by typing any keyword from title, content, author, or tag."),
        ("Results Status Indicator", "Displays search matches with a one-click 'Clear' button to restore the full board."),
        ("Card Information Hierarchy", "Each card displays author avatar, category pill, excerpt, date, and reading time.")
    ]
    for pt, pd in f2_points:
        p_pt = tf_f2.add_paragraph()
        p_pt.text = f"• {pt}: {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(8)

    # =========================================================================
    # SLIDE 7: Advanced Feature: Editing & Deletion
    # =========================================================================
    slide7 = prs.slides.add_slide(blank_layout)
    add_header(slide7, "Lifecycle Control: Editing & Deletion", "06 / CRUD COMPLETION")

    f3 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    f3.fill.solid()
    f3.fill.fore_color.rgb = COLOR_BG_CARD
    f3.line.color.rgb = RGBColor(226, 232, 240)
    f3.line.width = Pt(1)

    tb_f3 = slide7.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_f3 = tb_f3.text_frame
    tf_f3.word_wrap = True

    p = tf_f3.paragraphs[0]
    p.text = "Article Editing (Update)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    f3_points = [
        ("Pre-Populated Form", "Loads existing title, content, author, and category tag so authors don't re-type data."),
        ("Revision Timestamp", "Updates the updated_at timestamp to mark when the article was revised."),
        ("Immediate Inspection", "Saves and returns directly to the full article view so revisions can be inspected.")
    ]
    for pt, pd in f3_points:
        p_pt = tf_f3.add_paragraph()
        p_pt.text = f"• {pt}: {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(10)

    f4 = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    f4.fill.solid()
    f4.fill.fore_color.rgb = COLOR_BG_CARD
    f4.line.color.rgb = RGBColor(226, 232, 240)
    f4.line.width = Pt(1)

    tb_f4 = slide7.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.2))
    tf_f4 = tb_f4.text_frame
    tf_f4.word_wrap = True

    p = tf_f4.paragraphs[0]
    p.text = "Article Removal (Delete)"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    f4_points = [
        ("POST Method Constraint", "Enforces HTTP POST for deletions to avoid accidental removal via web crawlers."),
        ("Interactive Confirmation", "Browser prompt 'Are you sure you want to delete this post?' prevents accidents."),
        ("Flash Notification", "Flashes a clear confirmation notice citing the specific removed headline.")
    ]
    for pt, pd in f4_points:
        p_pt = tf_f4.add_paragraph()
        p_pt.text = f"• {pt}: {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(10)

    # =========================================================================
    # SLIDE 8: UI & UX Design Decisions
    # =========================================================================
    slide8 = prs.slides.add_slide(blank_layout)
    add_header(slide8, "User Interface & Experience (UI/UX)", "07 / INTERFACE DESIGN")

    ux_cards = [
        ("Blue, Purple & Obsidian Palette", "Deep obsidian background (#090D16), glowing electric blue (#3B82F6), and neon purple (#8B5CF6).", "• Animated gradient glow strip\n• Glassmorphic dark navbar\n• Smooth gradient buttons"),
        ("2-Column Side-by-Side Grid", "Cards arranged in side-by-side dual columns with subtle elevation on hover.", "• Multi-column desktop layout\n• Author avatars & tag badges\n• Estimated read times"),
        ("Smooth CSS Keyframe Animations", "Staggered card fade-in-up animations and glowing hover elevation.", "• @keyframes fadeInUp entrance\n• Flowing gradient animation\n• Focus glow transitions"),
        ("Responsive Layout", "Flexbox and CSS Grid adapt gracefully from wide desktop monitors to mobile phones.", "• Auto-stacking form fields\n• Mobile-friendly touch targets\n• Zero horizontal scroll")
    ]

    for i, (title, desc, bullets) in enumerate(ux_cards):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.9)
        top = Inches(1.8 + row * 2.5)
        width = Inches(5.6)
        height = Inches(2.25)

        card = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = RGBColor(226, 232, 240)
        card.line.width = Pt(1)

        tb = slide8.shapes.add_textbox(left + Inches(0.2), top + Inches(0.15), width - Inches(0.4), height - Inches(0.3))
        tf = tb.text_frame
        tf.word_wrap = True

        pt = tf.paragraphs[0]
        pt.text = title
        pt.font.size = Pt(15)
        pt.font.bold = True
        pt.font.color.rgb = COLOR_BLUE

        pr = tf.add_paragraph()
        pr.text = desc
        pr.font.size = Pt(12)
        pr.font.color.rgb = COLOR_DARK
        pr.space_before = Pt(4)

        pb = tf.add_paragraph()
        pb.text = bullets
        pb.font.size = Pt(11)
        pb.font.color.rgb = COLOR_MUTED
        pb.space_before = Pt(6)

    # =========================================================================
    # SLIDE 9: Key Findings & Technical Learnings
    # =========================================================================
    slide9 = prs.slides.add_slide(blank_layout)
    add_header(slide9, "Key Findings & Technical Learnings", "08 / EVALUATION & LEARNINGS")

    learnings = [
        ("Database Schema Migrations in Production", "Gained practical experience implementing non-destructive schema migrations (using PRAGMA table_info and ALTER TABLE) to add author and tag fields without losing existing data."),
        ("Building Flexible Search Filters", "Mastered multi-field SQL LIKE queries with wildcards (%...%) and learned how URL query parameters (?q=...) enable bookmarkable and shareable search states."),
        ("Modern Animation Systems & Micro-Interactions", "Discovered how CSS keyframe animations, staggered delays, and electric gradient accents turn a simple application into a visually engaging product."),
        ("Automated Testing for Regression Protection", "Expanded the test suite to 6 unit tests covering author attribution, search filters, and CRUD integrity, proving that tests give confidence when refactoring.")
    ]

    for i, (head, body) in enumerate(learnings):
        left = Inches(0.8)
        top = Inches(1.8 + i * 1.25)
        width = Inches(11.7)
        height = Inches(1.1)

        card = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_BG_CARD
        card.line.color.rgb = COLOR_PURPLE
        card.line.width = Pt(1)

        tb = slide9.shapes.add_textbox(left + Inches(0.2), top + Inches(0.1), width - Inches(0.4), height - Inches(0.2))
        tf = tb.text_frame
        tf.word_wrap = True

        ph = tf.paragraphs[0]
        ph.text = f"{i+1}. {head}"
        ph.font.size = Pt(15)
        ph.font.bold = True
        ph.font.color.rgb = COLOR_PRIMARY

        pb = tf.add_paragraph()
        pb.text = body
        pb.font.size = Pt(12)
        pb.font.color.rgb = COLOR_DARK
        pb.space_before = Pt(3)

    # =========================================================================
    # SLIDE 10: Future Roadmap & Conclusion
    # =========================================================================
    slide10 = prs.slides.add_slide(blank_layout)
    add_header(slide10, "Challenges, Future Roadmap & Conclusion", "09 / SUMMARY & ROADMAP")

    c_card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
    c_card.fill.solid()
    c_card.fill.fore_color.rgb = COLOR_BG_CARD
    c_card.line.color.rgb = RGBColor(226, 232, 240)
    c_card.line.width = Pt(1)

    tb_c = slide10.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
    tf_c = tb_c.text_frame
    tf_c.word_wrap = True

    p = tf_c.paragraphs[0]
    p.text = "Challenges Overcome"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    chal_points = [
        ("Clean Schema Evolution", "Adapted the SQLite database with new columns while preserving existing post data."),
        ("Multi-Field Search Logic", "Engineered SQL LIKE queries that match keywords across title, content, author, and category tag simultaneously."),
        ("Fluid CSS Animation Performance", "Engineered GPU-accelerated keyframe animations that run at 60fps across mobile and desktop.")
    ]
    for pt, pd in chal_points:
        p_pt = tf_c.add_paragraph()
        p_pt.text = f"• {pt}:\n  {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(10)

    r_card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8))
    r_card.fill.solid()
    r_card.fill.fore_color.rgb = COLOR_BG_CARD
    r_card.line.color.rgb = RGBColor(226, 232, 240)
    r_card.line.width = Pt(1)

    tb_r = slide10.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.1), Inches(4.2))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "Future Roadmap"
    p.font.size = Pt(17)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    road_points = [
        ("User Accounts & Authentication", "Introduce login with bcrypt password hashing for individual author accounts."),
        ("Markdown Support", "Support markdown formatting and code syntax highlighting."),
        ("Comments Section", "Enable readers to leave feedback on individual articles."),
        ("Cloud Hosting", "Deploy to cloud platforms (Render, Railway, or AWS) with a live public URL.")
    ]
    for pt, pd in road_points:
        p_pt = tf_r.add_paragraph()
        p_pt.text = f"→ {pt}: {pd}"
        p_pt.font.size = Pt(12.5)
        p_pt.font.color.rgb = COLOR_DARK
        p_pt.space_before = Pt(8)

    output_path = os.path.join(os.path.dirname(__file__), 'presentation.pptx')
    prs.save(output_path)
    print(f"Presentation updated at: {output_path}")

if __name__ == '__main__':
    create_presentation()
