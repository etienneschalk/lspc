<!--
Readme template taken from
https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
-->

# lspc

Making a simple version of the ```ls``` command

## Getting Started

### Prerequisites

python3 is required to run this project properly.

### Installing

You must first clone the repositery.
Then, to make the execution of the script easier, you can add this line to your ```.bashrc```, in order to create an alias:

```
alias lspc="[Your installation folder]/lspc/ls.py"
```

(you can also type it directly in the terminal, then the alias will be active for the current session)

With this, typing ```$ lspc``` in the terminal will run the script.


## Running lspc

You can run the ```$ lspc``` command with several options. The description of these options can be retrieved by typing ```$ lspc -h```.

```
usage: ls.py [-a] [-R] [-l] [-c] [-d] [-r] [-h]
             [directories [directories ...]]

ls avec python

arguments positionnels:
  directories      chemins des dossiers à lister

arguments optionnels:
  -a, --all        inclut les fichiers et dossiers cachés
  -R, --recursive  recherche récursive, descend dans les dossiers
  -l               affiche la taille des fichiers
  -c               indique le nombre de lignes des fichiers
  -d, --directory  n'affiche que les dossiers et le nombre de fichiers
                   contenus
  -r, --reverse    inverser l'ordre d'affichage
  -h, --help       affiche ce message d'aide et termine le programme

```


## Running the tests

You can run the tests by executing the script:

```
$ ./scripts/run_tests.sh
```

This will first generate the sample folder used by unit tests, and then run the unit tests.

You can also just create the test folder (it is already created, but you can recreate it), with:

```
$ ./scripts/make_test_folders.sh
```

and then running the unittest module:

```
$ python3 -m unittest discover
```


### Running unit and integration tests

For testing the whole ls program:

```
$ python3 -m unittest discover -s test/integration
```

For running only unit tests:

```
$ python3 -m unittest discover -s test/unit
```
