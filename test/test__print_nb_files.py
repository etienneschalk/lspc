import io
import sys
import unittest

from test.information import *

from util import *
from ls import print_nb_files

class TestPrintNbFiles(unittest.TestCase):

    def test_print_nb_files_files(self):
        """ Test that the number of files of all files fail """

        args = { "all": True }
        for file_info in file_information:
            # The "big" file is generated randomly, thus the lines are not known in advance.
            if file_info["name"] == "dir2_B_filebig":
                continue

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.assertRaises(NotADirectoryError, print_nb_files, root, file_info["path"], args)

        sys.stdout = sys.__stdout__


    def test_print_nb_files_directories(self):
        """ Test number of visible files in directories """

        args = { "all": False }

        for dir_info in directory_information:
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            print_nb_files(root, dir_info["path"], args)
            expectedPrint = str(dir_info["nb_files"]) + "\t"
            self.assertEqual(capturedOutput.getvalue(), expectedPrint)

        sys.stdout = sys.__stdout__

    def test_print_nb_files_directories_all(self):
        """ Test number of all files in directories """

        args = { "all": True }

        for dir_info in directory_information:
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            print_nb_files(root, dir_info["path"], args)
            expectedPrint = str(dir_info["nb_files_all"]) + "\t"
            self.assertEqual(capturedOutput.getvalue(), expectedPrint)

        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
