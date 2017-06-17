import unittest
from selenium import webdriver


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Agatha has heard about the new gebr site
        # She goes to its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention bulldogrescue
        self.assertIn('Bulldog Rescue', self.browser.title)

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
