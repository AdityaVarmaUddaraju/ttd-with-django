from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_id_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Roark has heard about a new to-do app.
        # He tried to access the app in the browser
        
        self.browser.get(self.live_server_url)

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('add_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # He types "watch one piece anime" into the text box
        input_box.send_keys('watch one piece anime')

        # When he hits enter, the page updates and lists
        # 1. watch one piece anime
        input_box.send_keys(Keys.ENTER)
        time.sleep(1.0)

        self.check_for_row_in_id_list_table('1. watch one piece anime')
        
        # There is still a text box inviting him to add another item.
        input_box = self.browser.find_element_by_id('add_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # He enters "read ttd with python book"
        input_box.send_keys('read ttd with python book')
        input_box.send_keys(Keys.ENTER)
        time.sleep(1.0)
        # The page updates again, and now shows both items on her list
        self.check_for_row_in_id_list_table('1. watch one piece anime')
        self.check_for_row_in_id_list_table('2. read ttd with python book')        
        
        self.fail('Finish the test!')
        # Roark sees that the site generates a unique URl for him

        # he visits the url and his to-do lists is still there

        # Satisfied, he goes back to sleep

