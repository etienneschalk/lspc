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

    for root, dirs, files in os.walk(dirpath, topdown=True):
        if args["recursive"] or root == dirpath:

            if args["l"] or args["recursive"]:
                if not args["folders"]:
                    print("."+re.sub(r'%s' % (dirpath), '', root, 1)+":")
                else:
                    print(root+":")

            if (not args["all"]):
                files = [f for f in files if f[0] != '.']
                dirs[:] = sorted([d for d in dirs if d[0] != '.'], reverse=args["reverse"])
            for name in sorted(dirs, reverse=args["reverse"]):
                if is_visible(name, args):
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
                            try:
                                length = len(open(os.path.join(root, name), "r").readlines())
                                print(Color.WARNING + str(length) + Color.ENDC + "\t", end='')
                            except IOError:
                                log.error("Problème lors de la lecture du fichier " + name)
                            except UnicodeDecodeError:
                                log.info("Echec du décodage du fichier " + name)
                        if args["l"]:
                            statinfo = os.stat(os.path.join(root, name))
                            print(Color.OKGREEN + str(statinfo.st_size) + Color.ENDC + "\t", end='')
                        print(name)
            print()

def main():
    "Entry point for the ls program"

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG,
        datefmt='%Y/%m/%d %H:%M:%S'
    )

    log.info("ls started")
    log.info("Dirpath " + dirpath)
    horizontal_line()
    args = parse_args()
    horizontal_line()
    ls(dirpath, args)
    horizontal_line()
    # walk(dirpath)

    log.info("ls finished")

if __name__ == "__main__":
    main()
