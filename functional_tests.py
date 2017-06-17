import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_starting_a_new_todo_list(self):
        # Agatha has heard about the new gebr site
        # She goes to its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention Bulldog Rescue
        self.assertIn('Bulldog Rescue', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your To-Do list', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Look for food" into a text box (Agatha's hobby
        # is eating)
        inputbox.send_keys('Look for food')

        # When she hits enter, the page updates, and now the page lists
        # "1: Look for food" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Look for food', [row.text for row in rows])

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Agatha is very
        # methodical)
        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
