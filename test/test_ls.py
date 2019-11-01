
# -c and -l options are not tested since they are alredy unit-tested

import io
import re
import sys
import unittest

from test.information import *

from util import *
from ls import ls

format.enable(False)

# We consider the case where we pass 1 directory arg to ls
# so we fill the directories array with one item : root ("./sample/")
def find_args(string_args):
    args = {
        "directories": [root],
        "recursive": False,
        "all": False,
        "c": False,
        "l": False,
        "directory": False,
        "reverse": False
    }

    for char in string_args:
        if char == 'R':
            args["recursive"] = True
        elif char == 'a':
            args["all"] = True
        elif char == 'c':
            args["c"] = True
        elif char == 'l':
            args["l"] = True
        elif char == 'd':
            args["directory"] = True
        elif char == 'r':
            args["reverse"] = True
    return args

class TestLs(unittest.TestCase):

    def test_ls_simple(self):
        """
        Test ls on sample folder with:
        - combinations on {r, a}
        - d=False, R=False
        """

        # Iterate over the dict of predicted outputs
        for string_args, predicted_list in predicted_lists_simple.items():
            args = find_args(string_args)

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            ls(root, args)
            lines = capturedOutput.getvalue().splitlines()
            lines.pop() # remove the last newline

            for line, predicted_line in zip(lines, predicted_list):
                self.assertEqual(line, predicted_line)

        sys.stdout = sys.__stdout__


    def test_ls_simple_directories(self):
        """
        Test ls on sample folder with:
        - combinations on {r, a}
        - d=True, R=False
        """

        # Iterate over the dict of predicted outputs
        for string_args, predicted_list in predicted_lists_simple_directories.items():
            args = find_args(string_args)

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            ls(root, args)
            lines = capturedOutput.getvalue().splitlines()
            lines.pop() # remove the last newline
            # sys.stdout = sys.__stdout__
            # print(lines)
            # print(predicted_list)
            for line, predicted_line in zip(lines, predicted_list):
                dir_info = [dir_info_ for dir_info_ in directory_information if dir_info_["name"] == predicted_line]
                dir_info = dir_info[0]
                nb_files = dir_info["nb_files_all"] if args["all"] else dir_info["nb_files"]
                predicted_line_complete = str(nb_files) + "\t" + predicted_line
                self.assertEqual(line, predicted_line_complete)

        sys.stdout = sys.__stdout__


    def test_ls_recursive(self):
        """
        Test ls on sample folder with:
        - combinations on {r, a}
        - d=False, R=True
        """

        # Iterate over the dict of predicted outputs
        for string_args, predicted_list in predicted_lists_recursive.items():
            args = find_args(string_args)
            print(str(args) + " ==============")
            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            ls(root, args)
            lines = capturedOutput.getvalue().splitlines()
            lines.pop() # remove the last newline

            sys.stdout = sys.__stdout__

            print()
            print(root)
            print(lines)
            print(predicted_list)
            horizontal_line()

            dict_lines = {}
            current_folder = ""
            for line in lines:
                # Newline separation between folders
                if line == '':
                    continue

                # Directory title printed
                elif line[-1] == ':':
                    current_folder = line
                    dict_lines[current_folder] = []

                # Content of a directory
                else:
                    dict_lines[current_folder].append(line)
            print(dict_lines)


            # Checking all the sub-folders contents
            for sub_folder_obtained, sub_folder_expected in zip(dict_lines, predicted_list):
                self.assertEqual(
                    sub_folder_obtained,
                    root + sub_folder_expected + ":"
                )
                print("sub_folder_obtained", sub_folder_obtained)
                print("sub_folder_expected", root + sub_folder_expected + ":")

                # TODO Iterate on the content on dict, not the string itself !
                for file_obtained, file_expected in zip(sub_folder_obtained, sub_folder_expected):

                    print("file_obtained", file_obtained)
                    print("file_expected", file_expected)
                    self.assertEqual(file_obtained, file_expected)

            # for line, predicted_line in zip(lines, predicted_list):
            #     # Newline separation between folders
            #     if line == '':
            #         continue
            #
            #     # Directory title printed
            #     elif line[-1] == ':':
            #         self.assertEqual(
            #             line,
            #             root + predicted_line + ":"
            #         )
            #
            #     # Content of a directory
            #     else:
            #         self.assertEqual(line, predicted_line)

        sys.stdout = sys.__stdout__


    # def test_ls_recursive_directories(self):
    #     """
    #     Test ls on sample folder with:
    #     - combinations on {r, a}
    #     - d=True, R=True
    #     """
    #
    #     # Iterate over the dict of predicted outputs
    #     for string_args, predicted_list in predicted_lists_recursive_directories.items():
    #         args = find_args(string_args)
    #
    #         # Capture the standard output
    #         capturedOutput = io.StringIO()
    #         sys.stdout = capturedOutput
    #         ls(root, args)
    #         lines = capturedOutput.getvalue().splitlines()
    #         lines.pop() # remove the last newline
    #
    #         for line, predicted_line in zip(lines, predicted_list):
    #             self.assertEqual(line, predicted_line)
    #
    #     sys.stdout = sys.__stdout__

if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
