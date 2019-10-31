import unittest

from informations_tests import *

from ls import print_size
from ls import format_size

class TestFormatSize(unittest.TestCase):

    def test_format_size(self):
        """ Test the size formatter function """

        expected_format = {
            1  :  "1 B",
            1e1:  "10 B",
            1e2:  "100 B",
            1e3:  "1 kB",
            1e4:  "10 kB",
            1e5:  "100 kB",
            1e6:  "1 MB",
            1e7:  "10 MB",
            1e8:  "100 MB",
            1e9:  "1 GB",
            1e10: "10 GB",
            1e11: "100 GB",
            1e12:  "1 TB",
            1e13: "10 TB",
            1e14: "100 TB",
            1e15: "1000 TB",
        }

        for size, format in expected_format.items():
            self.assertEqual(format_size(size), format)


if __name__ == '__main__':
    unittest.main()
