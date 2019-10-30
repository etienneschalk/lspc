#!/usr/bin/env python3

"""
//==============================================================================
|| ls
//==============================================================================

--------------------------------------------------------------------------------
"""

import argparse
import logging
import os
import sys
import re

from util import *

log = logging.getLogger(__name__)
loglevel = logging.WARNING

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
prefixes = [

args = []

def parse_args():
    """ Parse options given to the script (flags and directories) """

    parser = argparse.ArgumentParser(description="ls with python")

    parser.add_argument("folders", metavar="folders", type=str, nargs="*",
        help="directory's path(s) to list")

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

    args = vars(parser.parse_args())

    return args

def walk(path):
    for root, dirs, files in os.walk(dirpath):
        for name in files:
            print("File:", os.path.join(root, name))
        for name in dirs:
            print("Dir:", os.path.join(root, name))

def simple_ls(path, args):
    if args["l"]:
        for f in sorted(os.listdir(path), reverse=args["reverse"]):
            try:
                length = len(open(f, "r").readlines())
                print(str(length) + " " + f)
            except IOError:
                log.error("Erreur : Problème lors de la lecture du fichier " + f)


    else:
        for f in sorted(os.listdir(path), reverse=args["reverse"]):
            print(f)

def ls_module(path, args):
    """ Main ls function """

    # Browsing directories top down
    for root, dirs, files in os.walk(path, topdown=True):

        # Continue to browse, if recursive browsing or top level folder
        if args["recursive"] or root == path:

            # Print the title of the folder being browsed
            if args["recursive"]:
                print_folder_titles(root, path, args)

            # Removing hidden files and folder from the list
            if not args["all"]:
                files = [f for f in files if f[0] != '.']
                dirs[:] = sorted([d for d in dirs if d[0] != '.'], reverse=args["reverse"])

            # Print the list of directories
            for name in sorted(dirs, reverse=args["reverse"]):
                print_directory(root, name, args)

            # Print the list of files, the directory flag is not present
            if not args["directory"]:
                for name in sorted(files, reverse=args["reverse"]):
                    print_file(root, name, args)

            print()

        else:
            break # Exit the loop to prevent exploring lower-level folders


def is_visible(name, args):
    """ Indicates if the file or folder must be displayed """

    return args["all"] or name[0] != '.'


def print_folder_titles(root, path, args):
    """
    Print folder titles before listing their content,
    if the recursive option is given.
    If no folders are given to the script, the prefix is a point
    Otherwise, the folders names are printed
    """

    if args["folders"]:
        print(root+":")
    else:
        print("."+re.sub(r'%s' % (path), '', root, 1)+":")


def print_file(root, name, args):
    """ Printing a file """

    if(args["c"]):
        print_nb_lines(root, name, args)
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


def print_size(root, name):
    """ Tries to get the size of a file (in bytes) """

    statinfo = os.stat(os.path.join(root, name))
    size = statinfo.st_size
    print(Color.OKGREEN + str(statinfo.st_size) + Color.ENDC + "\t", end='')


def print_nb_lines(root, name, args):
    """ Tries to get the number of lines of a file, by scanning it """
    # TODO : test if we have a text file or not ?
    print(Color.WARNING, end='')
    try:
        length = len(open(os.path.join(root, name), "r").readlines())
        print(Color.WARNING + str(length) + Color.ENDC + "\t", end='')
    except IOError:
        log.warning("Problème lors de la lecture du fichier " + name)
        print("-\t", end='')
    except UnicodeDecodeError:
        log.info("Echec du décodage du fichier " + name)
        print("-\t", end='')
    print(Color.ENDC, end='')

def print_nb_files(root, name, args):
    """ Tries to get the number of files contained in a folder """

    directory = os.path.join(root, name)

    try:
        print(len([f for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f)) and is_visible(f, args)]),
            end='\t')
    except PermissionError:
        log.warning("Impossible de parcourir le contenu du dossier : " + directory)
        print("-\t", end='')


# maybe using an object (with attribute args) could be useful
# args ? prefix ?

def ls(path, args):
    """Main function called by main"""

    for root, dirs, files in os.walk(path, topdown=True):
        if args["recursive"] or root == path:

            if args["recursive"]:
                if not args["folders"]:
                    print("."+re.sub(r'%s' % (path), '', root, 1)+":")
                else:
                    print(root+":")

            if (not args["all"]):
                files = [f for f in files if f[0] != '.']
                dirs[:] = sorted([d for d in dirs if d[0] != '.'], reverse=args["reverse"])
            for name in sorted(dirs, reverse=args["reverse"]):
                if is_visible(name, args):
                    if args["directory"]:
                        directory = os.path.join(root, name)
                        # print(path)
                        # print(name)
                        # print(os.listdir(path))
                        # Display the number of files contained inside the folder
                        try:
                            print(len([f for f in os.listdir(directory)
                                        if os.path.isfile(os.path.join(directory, f)) and is_visible(f, args)]),
                                        end='\t')
                        except PermissionError:
                            log.warning("Impossible de parcourir le contenu du dossier : " + directory)
                            print("-\t", end='')
                    if not args["directory"]:
                        if args["l"]:
                            print("-\t", end='')
                        if args["c"]:
                            print("-\t", end='')
                    print(Color.BOLD + Color.OKBLUE + name + Color.ENDC)
            if not args["directory"]:
                for name in sorted(files, reverse=args["reverse"]):
                    if is_visible(name, args):
                        if args["c"]:
                            # TODO : test if we have a text file or not ?
                            print(Color.WARNING, end='')
                            try:
                                length = len(open(os.path.join(root, name), "r").readlines())
                                print(Color.WARNING + str(length) + Color.ENDC + "\t", end='')
                            except IOError:
                                log.warning("Problème lors de la lecture du fichier " + name)
                                print("-\t", end='')
                            except UnicodeDecodeError:
                                log.info("Echec du décodage du fichier " + name)
                                print("-\t", end='')
                            print(Color.ENDC, end='')

                        if args["l"]:
                            statinfo = os.stat(os.path.join(root, name))
                            print(Color.OKGREEN + str(statinfo.st_size) + Color.ENDC + "\t", end='')
                        print(name)
            print()
        else:
            break

def main():
    "Entry point for the ls program"

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=loglevel,
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    log.info("ls started")
    log.info("Dirpath " + dirpath)
    # horizontal_line()
    args = parse_args()
    # horizontal_line()
    if not args["folders"]:
        # ls(dirpath, args)
        ls_module(dirpath, args)
    else:
        for dir in args["folders"]:
            # ls(dir, args)
            ls_module(dir, args)
    # horizontal_line()
    # walk(dirpath)

    log.info("ls finished")

if __name__ == "__main__":
    main()
