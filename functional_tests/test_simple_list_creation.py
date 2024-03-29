from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVistorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Agatha has heard about the new GEBR site
        # She goes to its homepage
        self.browser.get(self.live_server_url)

        # She notices the page title and header mention Bulldog Rescue
        self.assertIn('Bulldog Rescue', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Start a new To-Do list', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
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
        self.wait_for_row_in_list_table('1: Look for food')

        # There is still a text box inviting her to add another item. She
        # enters "Sit near food bowl and wait" (Agatha is very
        # methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Sit near food bowl and wait')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_list_table('1: Look for food')
        self.wait_for_row_in_list_table('2: Sit near food bowl and wait')

        # Satisfied, she goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Agatha starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Look for food')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Look for food')

        # She notices that her list has a unique URL
        Agatha_list_url = self.browser.current_url
        self.assertRegex(Agatha_list_url, '/lists/.+')

        # Now a new user, Bruno, comes along to the site.

        # # We use a new browser session to make sure that no information
        # # of Agatha's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Bruno visits the home page.  There is no sign of Agatha's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Look for food', page_text)
        self.assertNotIn('bowl and wait', page_text)

        # Bruno starts a new list by entering a new item. He
        # is less interesting than Agatha...
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Take a nap')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Take a nap')

        # Bruno gets his own unique URL
        Bruno_list_url = self.browser.current_url
        self.assertRegex(Bruno_list_url, '/lists/.+')
        self.assertNotEqual(Bruno_list_url, Agatha_list_url)

        # Again, there is no trace of Agatha's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Look for food', page_text)
        self.assertIn('Take a nap', page_text)

        # Satisfied, they both go back to sleep
