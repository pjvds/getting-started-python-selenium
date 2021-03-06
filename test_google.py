#!/usr/bin/env python

import unittest
from pyvirtualdisplay import Display
from selenium import webdriver


class TestUbuntuHomepage(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def testTitle(self):
        self.browser.get('http://wercker.com/')
        self.assertIn('wercker', self.browser.title)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    # Run the code this process inside a virtual framebuffer
    display = Display(visible=0, size=(800, 600))
    display.start()
    unittest.main(verbosity=2)
    display.stop()
