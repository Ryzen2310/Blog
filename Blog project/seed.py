import database

def seed_database():
    """Populates the database with stylish 'Like a Blogger' sample stories."""
    database.init_db()
    conn = database.get_db_connection()
    conn.execute('DELETE FROM posts')
    conn.commit()
    conn.close()

    database.create_post(
        title="The Modern Guide to Content Creation & Digital Storytelling",
        content="In an era of fleeting attention spans, creating content that resonates requires intentionality and authentic perspective. Whether writing technical breakdowns, design teardowns, or personal dispatches, finding your distinctive voice is the ultimate differentiator.\n\nGreat blogs don't just broadcast information—they build intimate intellectual conversations with curious readers. Start with clarity, embrace unique visual aesthetics, and publish with conviction.",
        author="Admin",
        tag="Content Creation",
        views=142,
        likes=28
    )
    database.create_post(
        title="Design Systems: Why Neo-Brutalism & Tactile Shadows are Back",
        content="For the past decade, web design was dominated by flat minimalism and ethereal blurred dropshadows. Today, a bold counter-revolution is taking over: Neo-Brutalism.\n\nWith high-contrast borders, solid 3D offset drop shadows, pill-shaped tags, and expressive display typography, modern interfaces feel tangible and tactile once again. When every website looks the same, bold design is your superpower.",
        author="Studio Lead",
        tag="Design & Style",
        views=98,
        likes=19
    )
    database.create_post(
        title="Building Full-Stack Web Apps: From Concept to Production",
        content="Taking an idea from a blank text editor to a live globally-deployed URL is one of the most rewarding journeys in software engineering. By mastering foundational architectural patterns like Model-View-Controller (MVC) and understanding database normalization, complex workflows become manageable.\n\nPython, Flask, and SQLite provide the ultimate developer experience: zero boilerplate, instant feedback loops, and complete transparency.",
        author="Intern Dev",
        tag="Technology",
        views=215,
        likes=43
    )
    database.create_post(
        title="The Habit of Daily Editorial Writing & Creative Output",
        content="Consistency is the mother of mastery. Setting aside just thirty minutes each morning to articulate ideas forces intellectual rigor and reveals subtle nuances you might otherwise miss.\n\nDocument your process, share what you are learning in public, and treat every article as a stepping stone toward deeper expertise.",
        author="Editorial",
        tag="Writing Tips",
        views=86,
        likes=15
    )
    print("Successfully seeded 'Like a Blogger' sample posts!")

if __name__ == '__main__':
    seed_database()
