#!/usr/bin/env python3
# coding=utf-8

"""
//============================================================================//
|| lspc - python's ls for polyconseil                                         ||
//============================================================================//

Functions:

parse_args()
ls(start_path, args)
print_file(root, name, args):
print_directory(root, name, args):
print_directory_titles(root, start_path, args)
T is_visible(name, args)
T print_size(root, name)
T print_nb_lines(root, name)
T print_nb_files(root, name, args)
T format_size(size)

--------------------------------------------------------------------------------
"""


import argparse
import logging
import os
import re
import sys

from util import *


log = logging.getLogger(__name__)
loglevel = logging.WARNING

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)


def parse_args():
    """ Parse options given to the script (flags and directories) """

    parser = argparse.ArgumentParser(description="ls avec python",
        add_help=False)

    parser.add_argument("directories", metavar="directories", type=str, nargs="*",
        help="chemins des dossiers à lister")

    parser.add_argument("-a", "--all",
        help="inclut les fichiers et dossiers cachés",
        action="store_const", const=True, default=False)
    parser.add_argument("-R", "--recursive",
        help="recherche récursive, descend dans les dossiers",
        action="store_const", const=True, default=False)
    parser.add_argument("-l",
        help="affiche la taille des fichiers",
        action="store_const", const=True, default=False)
    parser.add_argument("-c",
        help="indique le nombre de lignes des fichiers",
        action="store_const", const=True, default=False)
    parser.add_argument("-d", "--directory",
        help="n'affiche que les dossiers et le nombre de fichiers contenus",
        action="store_const", const=True, default=False)
    parser.add_argument("-r", "--reverse",
        help="inverser l'ordre d'affichage",
        action="store_const", const=True, default=False)

    parser.add_argument('-h', '--help',
        help="affiche ce message d'aide et termine le programme",
        action='help', default=argparse.SUPPRESS)
    parser._positionals.title = 'arguments positionnels'
    parser._optionals.title = 'arguments optionnels'

    args = vars(parser.parse_args())

    return args


def ls(start_path, args):
    """ Main ls function """

    # Browsing directories top down
    for root, dirs, files in os.walk(start_path, topdown=True):

        # Continue to browse, if recursive browsing or top level folder
        if args["recursive"] or root == start_path:

            # Print the title of the folder being browsed
            if args["recursive"]:
                print_directory_title(root, start_path, args)

            # Removing hidden files and folder from the list
            if not args["all"]:
                files = [f for f in files if f[0] != '.']
                dirs[:] = [d for d in dirs if d[0] != '.']
                
            dirs[:] = sorted(dirs, reverse=args["reverse"])

            # Print the list of directories
            for name in sorted(dirs, reverse=args["reverse"]):
                print_directory(root, name, args)

            # Print the list of files, if the directory flag is not present
            if not args["directory"]:
                for name in sorted(files, reverse=args["reverse"]):
                    print_file(root, name, args)

            print()

        else:
            break # Exit the loop to prevent exploring lower-level directories


def print_file(root, name, args):
    """ Printing a file """

    if(args["c"]):
        print_nb_lines(root, name)
    if args["l"]:
        print_size(root, name)
    print(name)


def print_directory(root, name, args):
    """ Printing a directory """

    if args["directory"]:
        print_nb_files(root, name, args)
    else:
        if args["l"]:
            print("-\t", end='')
        if args["c"]:
            print("-\t", end='')
    print(Color.BOLD + Color.OKBLUE + name + Color.ENDC)


def print_directory_title(root, start_path, args):
    """
    Print directory titles before listing their content, if the recursive option
    is given.
    If no directories are given to the script, the prefix is a point
    Otherwise, the directories names are printed
    """

    print(Color.YELLOW, end='')
    if args["directories"]:
        print(root+":")
    else:
        print("."+re.sub(r'%s' % (start_path), '', root, 1)+":")
    print(Color.ENDC, end='')


def is_visible(name, args):
    """ Indicates if the file or folder must be displayed """
    if not name:
        raise ValueError("Cannot determine the visibility of an empty name.")
    return args["all"] or name[0] != '.'


def print_size(root, name):
    """ Tries to get the size of a file (in bytes) """

    statinfo = os.stat(os.path.join(root, name))
    size = statinfo.st_size

    print(Color.OKGREEN + format_size(size) + Color.ENDC + "\t", end='')


def format_size(size):
    """ Format the big size numbers """

    prefix = ""

    if size >= 1e12:
        prefix = "T"
        size /= 1e12
    elif size >= 1e9:
        prefix = "G"
        size /= 1e9
    elif size >= 1e6:
        prefix = "M"
        size /= 1e6
    elif size >= 1e3:
        prefix = "k"
        size /= 1e3

    return str(ff0.format(size)) + " " + prefix + "B"


def print_nb_lines(root, name):
    """ Tries to get the number of lines of a file, by scanning it """

    try:
        file = open(os.path.join(root, name), "r")
        length = len(file.readlines())
        file.close()
        print(Color.WARNING + str(length) + Color.ENDC + "\t", end='')
    except UnicodeDecodeError:
        log.info("Echec du décodage du fichier " + name)
        print("-\t", end='')


def print_nb_files(root, name, args):
    """ Tries to get the number of files contained in a folder """

    directory = os.path.join(root, name)
    try:
        print(len([f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
            and is_visible(f, args)]), end='\t')
    except PermissionError:
        log.info("Impossible de parcourir le contenu du dossier : "
                    + directory)
        print("-\t", end='')


def main():
    """ Entry point for the script """

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=loglevel,
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    log.info("ls started")
    log.info("[dirpath: " + dirpath + "]")

    args = parse_args()

    # Execute ls for the current folder
    if not args["directories"]:
        ls(dirpath, args)

    # Execute ls for all given directories
    else:
        for dir in args["directories"]:
            ls(dir, args)

    log.info("ls finished")


if __name__ == "__main__":
    main()
