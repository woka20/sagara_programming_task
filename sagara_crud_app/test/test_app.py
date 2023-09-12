import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.secret_key = 'test_secret_key'
        self.username = 'testuser'
        self.password = 'testpassword'

    def test_login_and_post_blog(self):
        # Simulate a login by sending a POST request to /login
        self.app.post('/register', data={'username': self.username, 'password':self.password, 'name':"test",'email':"test@ini.com"})
        login_response = self.app.post('/login', data={'username': self.username, 'password':self.password})

      
        self.assertEqual(login_response.status_code, 200)

        # Simulate posting a blog by sending a POST request to /post
        blog_post = 'This is a test blog post'
        content="nt"
        post_response = self.app.post('/add', data={'title': content, 'post': blog_post})

        # Check that the blog post was successful (status code 200)
        self.assertEqual(post_response.status_code, 200)


    def tearDown(self):
        # Clean up after each test by logging out
        self.app.get('/logout')

if __name__ == '__main__':
    unittest.main()
