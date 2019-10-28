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
loglevel = logging.DEBUG

dirpath = os.getcwd()
foldername = os.path.basename(dirpath)
possible_args = "aRlcdr"

args = []

def parse_args():
    "Get options given to the script"

    parser = argparse.ArgumentParser(description="ls with python")
    parser.add_argument("folders", metavar="folders", type=str, nargs="*", help="directory's path(s) to list")
    parser.add_argument("-a", "--all", help="inclut les fichiers et dossiers cachés", action="store_const", const=True, default=False)
    parser.add_argument("-R", "--recursive", help="recherche récursive, descend dans les dossiers", action="store_const", const=True, default=False)
    parser.add_argument("-l", help="affiche la taille des fichiers", action="store_const", const=True, default=False)
    parser.add_argument("-c", help="indique le nombre de lignes des fichiers", action="store_const", const=True, default=False)
    parser.add_argument("-d", "--directory", help="n'affiche que les dossiers et le nombre de fichiers contenus", action="store_const", const=True, default=False)
    parser.add_argument("-r", "--reverse", help="inverser l'ordre d'affichage", action="store_const", const=True, default=False)
    args = vars(parser.parse_args())
    print(args)
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

def is_visible(name, args):
    return args["all"] or name[0] != '.'

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
    horizontal_line()
    args = parse_args()
    horizontal_line()
    if not args["folders"]:
        ls(dirpath, args)
    else:
        for dir in args["folders"]:
            ls(dir, args)
    horizontal_line()
    # walk(dirpath)

    log.info("ls finished")

if __name__ == "__main__":
    main()
