import io
import sys
import unittest

from test.information import *

from util import *
from ls import print_nb_lines

format.enable(False)


class TestPrintNbLines(unittest.TestCase):

    def test_print_nb_lines_files(self):
        """ Test that the number of lines of a file can be obtained """

        for file_info in file_information:
            # The "big" file is generated randomly, thus the lines are not known in advance.
            if file_info["name"] == "dir2_B_filebig":
                continue

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            print_nb_lines(root, file_info["path"])
            expectedPrint = str(file_info["lines"]) + "\t"
            self.assertEqual(capturedOutput.getvalue(), expectedPrint)

        sys.stdout = sys.__stdout__


    def test_print_nb_lines_directories(self):
        """ Test the print nb lines function on directories """

        for dir_info in directory_information:
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            self.assertRaises(IsADirectoryError, print_nb_lines, root, dir_info["path"])

        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
