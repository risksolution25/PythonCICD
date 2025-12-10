import unittest
from app import app

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Simple Flask Calculator", response.data)

    def test_add_route(self):
        response = self.client.post("/", data={
            "a": "2",
            "b": "3",
            "operation": "add"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"5", response.data)

if __name__ == "__main__":
    unittest.main()
