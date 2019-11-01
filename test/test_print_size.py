import io
import sys
import unittest

from test.information import *

from util import *
from ls import print_size
from ls import format_size

format.enable(False)

class TestPrintSize(unittest.TestCase):

    def test_file(self):
        """ Test that the size of a file can be obtained """

        for file_info in file_information:
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            print_size(root, file_info["path"])
            expectedPrint = format_size(file_info["bytes"]) + "\t"
            self.assertEqual(capturedOutput.getvalue(), expectedPrint)

        sys.stdout = sys.__stdout__


    def test_directory(self):
        """ Test that the size of a directory is one block (4 kB) """

        directory_size = "4 kB"

        for dir_info in directory_information:
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            print_size(root, dir_info["path"])
            expectedPrint = directory_size + "\t"
            self.assertEqual(capturedOutput.getvalue(), expectedPrint)

        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
