import database

def seed_database():
    """Populates the database with versatile, realistic sample blog posts."""
    database.init_db()
    conn = database.get_db_connection()
    conn.execute('DELETE FROM posts')
    conn.commit()
    conn.close()

    database.create_post(
        title="Getting Started with Modern Full-Stack Development",
        content="Building modern web applications requires a solid understanding of both frontend presentation and backend architecture. By structuring applications using the Model-View-Controller pattern, developers can cleanly decouple data persistence from business logic.\n\nPython and Flask provide an ideal environment for mastering HTTP routing, parameterized database queries, and dynamic template rendering without unnecessary abstraction.",
        author="Alex Chen",
        tag="Tech"
    )
    database.create_post(
        title="Why Intuitive UI & UX Design Matters",
        content="Great software is not just about clean code—it is about how the end user feels when interacting with your product. Thoughtful color hierarchy, responsive layouts, and immediate visual feedback turn a basic tool into an engaging experience.\n\nMicro-interactions, smooth hover animations, and clear status banners help guide users naturally and prevent frustration.",
        author="Jordan Lee",
        tag="Design"
    )
    database.create_post(
        title="Key Takeaways from My Software Engineering Internship",
        content="During this internship project, I focused on end-to-end CRUD operations, database schema migrations, and writing automated unit tests.\n\nOne of the biggest lessons was learning to prioritize user requirements first, iteratively refining features, and verifying every endpoint with automated test suites before deploying.",
        author="Intern Developer",
        tag="Career"
    )
    database.create_post(
        title="The Habit of Daily Technical Writing & Reflection",
        content="Documenting what you learn every single day is one of the highest-leverage habits any developer can build. Writing forces clarity of thought and reveals gaps in your understanding.\n\nWhether writing architecture decision records, release notes, or personal dev logs, putting thoughts into words solidifies engineering knowledge.",
        author="Morgan Reed",
        tag="Thoughts"
    )
    print("Successfully seeded 4 professional sample posts!")

if __name__ == '__main__':
    seed_database()
