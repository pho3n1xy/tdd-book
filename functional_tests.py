from selenium import webdriver
import unittest 


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_todo_list(self):
        # She notices the page title and header mention to-do lists
        assert "To-Do" in browser.title

        # She is invited to enter a to-do item straight away

        # She types "reach englightment" into a text box
        # Lane's hobby is ascending past the spiritual plane

        # When she hits enter, the page updates, and now the page lists
        # "1: Reach Enlightenment" as an item in a to-do list

        # There is still a text box inviting her to add another item
        # She enters "Escape from all Karmic debt" 

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep

if __name__ == "__main__":
    unittest.main()
