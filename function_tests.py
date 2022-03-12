from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Roark has heard about a new to-do app.
        # He tried to access the app in the browser
        
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "watch one piece anime" into the text box

        # When he hits enter, the page updates and lists
        # 1. watch one piece anime

        # There is still a text box inviting him to add another item.
        # He enters "read ttd with python book"

        # The page updates again, and now shows both items on her list

        # Roark sees that the site generates a unique URl for him

        # he visits the url and his to-do lists is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()
