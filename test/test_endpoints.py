from app import app
from flask import url_for
import unittest


class FlaskTodosTest(unittest.TestCase):
    # ..... setup section.....

    def test_home_status_code(self):
         """Assert that user successfully lands on homepage"""

        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_todo_creation(self):
        """Assert that user is redirected with status 302 after creating a todo item"""
        response = self.app.post('/new',
                                 data=dict(name="First todo",
                                           description="Test todo")
                                 )
        self.assertEqual(response.status_code, 302)


if __name__ == '__main__':
    unittest.main()