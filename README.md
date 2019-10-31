<!--
Readme template taken from
https://gist.github.com/PurpleBooth/109311bb0361f32d87a2
-->

# lspc

Making a simple version of the ```ls``` command

## Getting Started

### Prerequisites

python3 is needed to run this project properly.

### Installing

You must first clone the repositery.
Then, to make the execution of the script easier, you can add this line to your ```.bashrc```, in order to create an alias:

```
alias lspc="[Your installation folder]/lspc/ls.py"
```

With this, typing ```$ lspc``` in the terminal will run the script.

## Running the script

You can run the ```$ lspc``` command with several options. The description of these options can be retrieved by typing ```$ lspc -h```.



## Running the tests

You can run the tests by executing the script:

```
$ ./scripts/run_tests.sh
```

This will first generate the sample folder used by unit tests, and then run the unit tests.

You can also just create the test folder, with:

```
$ ./scripts/make_test_folders.sh
```

and then running the unittest module:

```
$ python3 -m unittest discover
```
