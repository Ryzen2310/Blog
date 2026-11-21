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
        self.assertIn(b'No articles found', response.data)

    def test_create_and_view_post_with_author_and_tag(self):
        """Test creating a post with author and tag, viewing it in grid and detail view."""
        # 1. Create Post
        response = self.client.post('/create', data={
            'title': 'Building Scalable APIs',
            'content': 'A comprehensive guide to designing RESTful endpoints.',
            'author': 'Alex Chen',
            'tag': 'Tech'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Building Scalable APIs', response.data)
        self.assertIn(b'Alex Chen', response.data)
        self.assertIn(b'Tech', response.data)

        # 2. View detail page
        posts = database.get_all_posts()
        self.assertEqual(len(posts), 1)
        post_id = posts[0]['id']

        detail_res = self.client.get(f'/post/{post_id}')
        self.assertEqual(detail_res.status_code, 200)
        self.assertIn(b'Building Scalable APIs', detail_res.data)
        self.assertIn(b'Alex Chen', detail_res.data)

    def test_search_functionality(self):
        """Test search filtering by keyword across title, content, and author."""
        database.create_post('Python Asyncio Guide', 'Learn asynchronous programming.', author='Jordan Lee', tag='Tech')
        database.create_post('Modern Typography System', 'Designing readable interfaces.', author='Morgan Reed', tag='Design')

        # Search for 'Asyncio'
        search_res = self.client.get('/?q=Asyncio')
        self.assertEqual(search_res.status_code, 200)
        self.assertIn(b'Python Asyncio Guide', search_res.data)
        self.assertNotIn(b'Modern Typography System', search_res.data)

        # Search for author 'Morgan'
        search_res2 = self.client.get('/?q=Morgan')
        self.assertEqual(search_res2.status_code, 200)
        self.assertIn(b'Modern Typography System', search_res2.data)
        self.assertNotIn(b'Python Asyncio Guide', search_res2.data)

    def test_edit_post(self):
        """Test editing an existing post's title, content, author, and tag."""
        post_id = database.create_post('Old Title', 'Old Content', author='Old Author', tag='General')

        response = self.client.post(f'/post/{post_id}/edit', data={
            'title': 'Updated Modern Title',
            'content': 'Updated Modern Content',
            'author': 'Alex Chen',
            'tag': 'Tech'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Updated Modern Title', response.data)

        # Verify in database
        post = database.get_post(post_id)
        self.assertEqual(post['title'], 'Updated Modern Title')
        self.assertEqual(post['author'], 'Alex Chen')

    def test_delete_post(self):
        """Test deleting a post."""
        post_id = database.create_post('Post to Delete', 'Some content')

        response = self.client.post(f'/post/{post_id}/delete', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'was deleted', response.data)

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
