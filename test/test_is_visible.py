import unittest

from test.information import *

from ls import is_visible

class TestIsVisible(unittest.TestCase):

    def test_is_visible(self):
        """ Test the visibility of all visible files and directories """

        args = { "all": False }
        for file_info in file_information:
            self.assertEqual(is_visible(file_info["name"], args), not file_info["hidden"])

        for dir_info in directory_information:
            if not dir_info["name"]:
                self.assertRaises(ValueError, is_visible, dir_info["name"], args)
            else:
                self.assertEqual(is_visible(dir_info["name"], args), not dir_info["hidden"])


    def test_is_visible_all(self):
        """ Test the visibility of all files and directories when all option is given """

        args = { "all": True }
        for file_info in file_information:
            self.assertEqual(is_visible(file_info["name"], args), True)

        for dir_info in directory_information:
            if not dir_info["name"]:
                self.assertRaises(ValueError, is_visible, dir_info["name"], args)
            else:
                self.assertEqual(is_visible(dir_info["name"], args), True)


if __name__ == '__main__':
    unittest.main()
