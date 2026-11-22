import unittest
import app
import database

class BlogTestCase(unittest.TestCase):
    def setUp(self):
        # Configure app for testing
        app.app.config['TESTING'] = True
        app.app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.app.test_client()

        # Ensure database is clean
        database.init_db()
        conn = database.get_db_connection()
        conn.execute('DELETE FROM posts')
        conn.commit()
        conn.close()

    def tearDown(self):
        conn = database.get_db_connection()
        conn.execute('DELETE FROM posts')
        conn.commit()
        conn.close()

    def test_empty_homepage(self):
        """Test that the homepage loads with empty state."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No dispatches found', response.data)

    def test_create_and_view_post_with_author_and_tag(self):
        """Test creating a post with author and tag, viewing it in grid and detail view."""
        # 1. Create Post
        response = self.client.post('/create', data={
            'title': 'The Editorial Process',
            'content': 'A comprehensive breakdown of content curation.',
            'author': 'Editorial Lead',
            'tag': 'Content Creation'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The Editorial Process', response.data)
        self.assertIn(b'Editorial Lead', response.data)
        self.assertIn(b'Content Creation', response.data)

        # 2. View detail page (increments views)
        posts = database.get_all_posts()
        self.assertEqual(len(posts), 1)
        post_id = posts[0]['id']

        detail_res = self.client.get(f'/post/{post_id}')
        self.assertEqual(detail_res.status_code, 200)
        self.assertIn(b'The Editorial Process', detail_res.data)
        self.assertIn(b'Editorial Lead', detail_res.data)

    def test_search_functionality(self):
        """Test search filtering by keyword across title, content, and author."""
        database.create_post('Python Asyncio Guide', 'Learn asynchronous programming.', author='Jordan Lee', tag='Technology')
        database.create_post('Neo-Brutalist Typography', 'Designing readable interfaces.', author='Morgan Reed', tag='Design & Style')

        # Search for 'Asyncio'
        search_res = self.client.get('/?q=Asyncio')
        self.assertEqual(search_res.status_code, 200)
        self.assertIn(b'Python Asyncio Guide', search_res.data)
        self.assertNotIn(b'Neo-Brutalist Typography', search_res.data)

        # Search for author 'Morgan'
        search_res2 = self.client.get('/?q=Morgan')
        self.assertEqual(search_res2.status_code, 200)
        self.assertIn(b'Neo-Brutalist Typography', search_res2.data)
        self.assertNotIn(b'Python Asyncio Guide', search_res2.data)

    def test_like_post_functionality(self):
        """Test toggling/incrementing likes on a post."""
        post_id = database.create_post('Likeable Story', 'Story content here.')
        post_before = database.get_post(post_id)
        self.assertEqual(post_before['likes'], 0)

        # Like the post
        response = self.client.post(f'/post/{post_id}/like', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        post_after = database.get_post(post_id)
        self.assertEqual(post_after['likes'], 1)

    def test_edit_post(self):
        """Test editing an existing post's title, content, author, and tag."""
        post_id = database.create_post('Old Title', 'Old Content', author='Old Author', tag='General')

        response = self.client.post(f'/post/{post_id}/edit', data={
            'title': 'Updated Neo-Brutalist Title',
            'content': 'Updated Editorial Content',
            'author': 'Admin',
            'tag': 'Writing Tips'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Neo-Brutalist Title', response.data)

        # Verify in database
        post = database.get_post(post_id)
        self.assertEqual(post['title'], 'Updated Neo-Brutalist Title')
        self.assertEqual(post['author'], 'Admin')

    def test_delete_post(self):
        """Test deleting a post."""
        post_id = database.create_post('Post to Delete', 'Some content')

        response = self.client.post(f'/post/{post_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'was removed', response.data)

        post = database.get_post(post_id)
        self.assertIsNone(post)

    def test_validation_empty_fields(self):
        """Test validation rejects empty title or content."""
        response = self.client.post('/create', data={
            'title': '',
            'content': 'Some content'
        }, follow_redirects=True)
        self.assertIn(b'Title is required!', response.data)

if __name__ == '__main__':
    unittest.main()
