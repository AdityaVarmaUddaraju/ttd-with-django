from tkinter import BROWSE
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_id_list_table(self, row_text):
        start = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return 
            except Exception as e:
                if time.time() - start > MAX_WAIT:
                    raise e
                time.sleep(0.5)

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

        self.wait_for_row_in_id_list_table('1. watch one piece anime')
        
        # There is still a text box inviting him to add another item.
        input_box = self.browser.find_element_by_id('add_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He enters "read ttd with python book"
        input_box.send_keys('read ttd with python book')
        input_box.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.wait_for_row_in_id_list_table('1. watch one piece anime')
        self.wait_for_row_in_id_list_table('2. read ttd with python book')        
        
        # Satisfied, he goes back to sleep

    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Roark starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('add_new_item')
        inputbox.send_keys('watch one piece anime')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_id_list_table('1. watch one piece anime')

        # he notices that her list has a unique URL
        roark_list_url = self.browser.current_url
        self.assertRegex(roark_list_url, '/lists/.+')

        # now a new user, rand comes along to the site.

        ## we use a new browser session to make sure that
        ## no information of roark is coming through from
        ## cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # rand visits the home page. There is no sign of roark's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('watch one piece anime', page_text)

        # rand starts a new list by entering a new line. She
        # is less interesting than roark...
        inputbox = self.browser.find_element_by_id('add_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_id_list_table('1. buy milk')

        # rand gets his own unique url
        rand_list_url = self.browser.current_url
        self.assertRegex(rand_list_url, '/lists/.+')
        self.assertNotEqual(roark_list_url, rand_list_url)

        # again, there is no trace of roarks list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('buy milk', page_text)
        self.assertNotIn('watch one piece anime', page_text)

        # satisfied they both go back to sleep

    def test_layout_and_styling(self):
        # roark goes to homepage
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # he notices that input box is nicely centered
        # inputbox = self.browser.find_element_by_id('add_new_item')
        # inputbox.send_keys('testing')
        # inputbox.send_keys(Keys.ENTER)
        # self.wait_for_row_in_id_list_table('1. testing')
        # self.assertAlmostEquals(
        #     inputbox.location['x'] + inputbox.size['width'] / 2,
        #     512,
        #     delta=10
        # )



