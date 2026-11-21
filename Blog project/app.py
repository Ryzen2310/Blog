import os
from flask import Flask, render_template, request, url_for, flash, redirect, abort
import database

# Ensure Flask always finds the templates and static folders on cloud deployments
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'static')
)
app.config['SECRET_KEY'] = 'nexus-blue-purple-blog-key-2026'

# Initialize database tables and migrations on startup
database.init_db()

@app.route('/')
def index():
    """Homepage: Displays all posts side-by-side with live search filtering."""
    search_query = request.args.get('q', '').strip()
    posts = database.get_all_posts(search_query=search_query if search_query else None)
    return render_template('index.html', posts=posts, search_query=search_query)

@app.route('/create', methods=('GET', 'POST'))
def create():
    """Create: Form for writing a new post (title, content, author, tag)."""
    if request.method == 'POST':
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        author = request.form.get('author', 'Author')
        tag = request.form.get('tag', 'Tech')

        if not title.strip():
            flash('Title is required!', 'error')
        elif not content.strip():
            flash('Content cannot be empty!', 'error')
        else:
            database.create_post(title, content, author=author, tag=tag)
            flash('✨ Post published successfully!', 'success')
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    """View: Displays a single full blog post."""
    post = database.get_post(post_id)
    if post is None:
        abort(404)
    return render_template('post.html', post=post)

@app.route('/post/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    """Edit: Form to edit an existing post's details."""
    post = database.get_post(post_id)
    if post is None:
        abort(404)

    if request.method == 'POST':
        title = request.form.get('title', '')
        content = request.form.get('content', '')
        author = request.form.get('author', 'Author')
        tag = request.form.get('tag', 'Tech')

        if not title.strip():
            flash('Title is required!', 'error')
        elif not content.strip():
            flash('Content cannot be empty!', 'error')
        else:
            database.update_post(post_id, title, content, author=author, tag=tag)
            flash('✨ Post updated successfully!', 'success')
            return redirect(url_for('post_detail', post_id=post_id))

    return render_template('edit.html', post=post)

@app.route('/post/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    """Delete: Removes a post from the database."""
    post = database.get_post(post_id)
    if post is None:
        abort(404)

    database.delete_post(post_id)
    flash(f'🗑️ Post "{post["title"]}" was deleted.', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
