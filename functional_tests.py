import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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
        self.check_for_row_in_list_table('1: Look for food')

        # There is still a text box inviting her to add another item. She
        # enters "Sit near food bowl and wait" (Agatha is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Sit near food bowl and wait')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Look for food')
        self.check_for_row_in_list_table('2: Sit near food bowl and wait')

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        self.fail('Finish the test!')

        # She visits that URL - her to-do list is still there.

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
