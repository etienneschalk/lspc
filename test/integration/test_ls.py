
# -c and -l options are not tested in this integration test

import io
import re
import sys
import unittest

from test.information import *

from util import *
from ls import ls

format.enable(False)


def find_args(string_args):
    """
    Parse args

    We consider the case where we pass 1 directory arg to ls
    so we fill the directories array with one item : root ("./sample/")
    """

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


def ls_lines_to_dict(lines):
    """
    Convert an array of lines containing the ls recursive output to a nice
    organized dict.
    """

    dict_lines = {}

    # Convert the ls' output to a nice organized dict of directories
    # name and ordered list of contained files
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

    return dict_lines


def format_directory_predicted_line(predicted_line, directory_information, show_all):
    """ Format the ls -d output (adding number of files) """

    # Search for directory information
    dir_info = [dir_info_ for dir_info_ in directory_information
                if dir_info_["name"] == predicted_line]
    if dir_info:
        dir_info = dir_info[0]
        nb_files = dir_info["nb_files_all"] if show_all else dir_info["nb_files"]
        return str(nb_files) + "\t" + predicted_line

    # If we fail to retrieve directory information, we give back the original name
    return predicted_line


def format_directory_predicted_lines(lines, directory_information, show_all):
    """ Plurial version of the same singular function """

    return [format_directory_predicted_line(line, directory_information, show_all)
            for line in lines]


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

            # Compare directory name and number of files contained
            for line, predicted_line in zip(lines, predicted_list):
                self.assertEqual(
                    line,
                    format_directory_predicted_line(predicted_line,
                        directory_information, args["all"])
                )

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

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            ls(root, args)
            lines = capturedOutput.getvalue().splitlines()

            dict_lines = ls_lines_to_dict(lines)
            current_folder = ""

            # Compare the obtained list of directories titles and list of files
            # to the expected one
            for obtained_list, expected_list in zip(
                dict_lines.items(), predicted_list.items()):

                # Compare the directory name obtained to the expected one
                self.assertEqual(obtained_list[0], root + expected_list[0] + ":")

                # Compare the lists of files associated to this directory
                self.assertEqual(obtained_list[1], expected_list[1])

        sys.stdout = sys.__stdout__


    def test_ls_recursive_directories(self):
        """
        Test ls on sample folder with:
        - combinations on {r, a}
        - d=True, R=True
        """

        # Iterate over the dict of predicted outputs
        for string_args, predicted_list in predicted_lists_recursive_directories.items():
            args = find_args(string_args)

            # Capture the standard output
            capturedOutput = io.StringIO()
            sys.stdout = capturedOutput
            ls(root, args)
            lines = capturedOutput.getvalue().splitlines()

            dict_lines = ls_lines_to_dict(lines)
            current_folder = ""

            # Compare the obtained list of directories titles and list of files
            # to the expected one
            for obtained_list, expected_list in zip(dict_lines.items(),
                predicted_list.items()):

                # Compare the directory name obtained to the expected one
                self.assertEqual(obtained_list[0], root + expected_list[0] + ":")

                # Compare the lists of files associated to this directory
                self.assertEqual(
                    obtained_list[1],
                    format_directory_predicted_lines(expected_list[1],
                        directory_information, args["all"])
                )

        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
    sys.stdout = sys.__stdout__
