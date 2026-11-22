import sqlite3
import os
import shutil

# In cloud serverless environments like Vercel, the root directory is read-only.
# We store the dynamic SQLite database in /tmp/ when running on Vercel.
if os.environ.get('VERCEL'):
    DATABASE_PATH = '/tmp/blog.db'
    bundled_db = os.path.join(os.path.dirname(__file__), 'blog.db')
    if not os.path.exists(DATABASE_PATH) and os.path.exists(bundled_db):
        try:
            shutil.copyfile(bundled_db, DATABASE_PATH)
        except Exception:
            pass
else:
    DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'blog.db')

def get_db_connection():
    """Establishes and returns a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database schema and performs migrations if needed."""
    conn = get_db_connection()
    with conn:
        conn.execute('''
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
            )
        ''')
        
        cursor = conn.execute("PRAGMA table_info(posts)")
        columns = [row['name'] for row in cursor.fetchall()]
        if 'author' not in columns:
            conn.execute("ALTER TABLE posts ADD COLUMN author TEXT DEFAULT 'Author'")
        if 'tag' not in columns:
            conn.execute("ALTER TABLE posts ADD COLUMN tag TEXT DEFAULT 'General'")
        if 'views' not in columns:
            conn.execute("ALTER TABLE posts ADD COLUMN views INTEGER DEFAULT 1")
        if 'likes' not in columns:
            conn.execute("ALTER TABLE posts ADD COLUMN likes INTEGER DEFAULT 0")
            
    conn.close()

def get_all_posts(search_query=None):
    """Fetches posts sorted newest to oldest, optionally filtered by a search query."""
    conn = get_db_connection()
    if search_query:
        query = f"%{search_query.strip()}%"
        posts = conn.execute(
            '''
            SELECT * FROM posts 
            WHERE title LIKE ? OR content LIKE ? OR author LIKE ? OR tag LIKE ?
            ORDER BY created_at DESC
            ''',
            (query, query, query, query)
        ).fetchall()
    else:
        posts = conn.execute(
            'SELECT * FROM posts ORDER BY created_at DESC'
        ).fetchall()
    conn.close()
    return posts

def get_post(post_id, increment_views=False):
    """Fetches a single post by its ID, optionally incrementing its view counter."""
    conn = get_db_connection()
    if increment_views:
        conn.execute('UPDATE posts SET views = views + 1 WHERE id = ?', (post_id,))
        conn.commit()

    post = conn.execute(
        'SELECT * FROM posts WHERE id = ?', (post_id,)
    ).fetchone()
    conn.close()
    return post

def create_post(title, content, author="Author", tag="General", likes=0, views=1):
    """Inserts a new blog post with author, tag, views, and likes."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO posts (title, content, author, tag, views, likes) 
        VALUES (?, ?, ?, ?, ?, ?)
        ''',
        (title.strip(), content.strip(), author.strip() or "Author", tag.strip() or "General", views, likes)
    )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    return post_id

def update_post(post_id, title, content, author="Author", tag="General"):
    """Updates an existing post's title, content, author, and tag."""
    conn = get_db_connection()
    conn.execute(
        '''
        UPDATE posts
        SET title = ?, content = ?, author = ?, tag = ?, updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
        ''',
        (title.strip(), content.strip(), author.strip() or "Author", tag.strip() or "General", post_id)
    )
    conn.commit()
    conn.close()

def delete_post(post_id):
    """Deletes a post by its ID."""
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()

def toggle_like_post(post_id):
    """Increments the like counter for a post."""
    conn = get_db_connection()
    conn.execute('UPDATE posts SET likes = likes + 1 WHERE id = ?', (post_id,))
    conn.commit()
    post = conn.execute('SELECT likes FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    return post['likes'] if post else 0
