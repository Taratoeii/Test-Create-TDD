from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_questions(self):  
        self.browser.get('http://localhost:8000/polls/7')
        
        self.assertIn('7', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("What's time", header_text)
        self.fail('Finish the test!')

    def test_vote(self):
        table = self.browser.find_element_by_id('id_list')
        rows = table.find_elements_by_tag_name('tr')
        radiobox = self.browser.find_element_by_id('choice')
        radiobox.send_keys('1')
        self.assertIn('Afternoon -- 4 votes',rows)
        self.fail('Correct!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')