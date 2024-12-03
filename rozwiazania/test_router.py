import unittest
from router import create_router


class TestRouter(unittest.TestCase):
    def setUp(self):
        self.router = create_router()
    
    def test_add_route(self):
        response = self.router("add", "/test", lambda: "Test page")
        self.assertEqual(response, "Route /test added")


    def test_get_existing_route(self):
        self.router("add", "/home", lambda: "Home page")
        response = self.router("get", "/home")
        self.assertEqual(response, "Home page")

    
    def test_get_non_existing_route(self):
        response = self.router("get", "/nonexisting")
        self.assertEqual(response, "404: Not found")

    def test_invalid_method(self):
        response = self.router("invalid", "/home", lambda: "Home page")
        self.assertEqual(response, "Invalid method: Use 'add' or 'get'")
if __name__ == "__main__":
    unittest.main()
