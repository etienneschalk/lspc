# coding=utf-8
#------ Utilitaries ------------------------------------------------------------

import platform
is_linux = platform.system() == "Linux"
format_enabled = True

# easy float formatting. usage: ffn.format(floatNumber)
ff4 = '{:.4f}'
ff3 = '{:.3f}'
ff2 = '{:.2f}'
ff1 = '{:.1f}'
ff0 = '{:.0f}'


def print_percent_bar(fraction, size=50, newLine=True):
    """ Print percent bar. Fraction must be a float between 0 and 1 """

    if fraction > 1 or fraction < 0:
        return()
    squares = fraction * size
    bar     = "█" * int(squares)
    nobar   = "░" * ( size - 1 - int(squares))
    rest    = squares - int (squares)
    mid     = "░" if rest < 1/3 else \
              "▒" if rest < 2/3 else \
              "▓"
    print(bar, mid, nobar, sep='', end= '\n' if newLine else '')


def print_dots(numberOfDots=10, newLine=True, char="■"):
    """ Print dots """
    print(char * numberOfDots, sep='', end= '\n' if newLine else '')


def horizontal_line(bold=0, size=80):
    """ Print horizontal line """
    if bold:
        print("=" * size)
    else:
        print("-" * size)



# format text (for UNIX)
class Format:

    def __init__(self, activation):
        self.enable(activation)

    def enable(self, activation):
        """ Enable or disable the colored text output """

        if activation:
            self.HEADER = '\033[95m'
            self.OKBLUE = '\033[94m'
            self.OKGREEN = '\033[92m'
            self.WARNING = '\033[93m'
            self.FAIL = '\033[91m'
            self.ENDC = '\033[0m'
            self.BOLD = '\033[1m'
            self.UNDERLINE = '\033[4m'
            self.YELLOW = '\033[33m'
            self.MAGENTA = '\033[35m'
            self.CYAN = '\033[36m'
        else:
            self.HEADER = ''
            self.OKBLUE = ''
            self.OKGREEN = ''
            self.WARNING = ''
            self.FAIL = ''
            self.ENDC = ''
            self.BOLD = ''
            self.UNDERLINE = ''
            self.YELLOW = ''
            self.MAGENTA = ''

# format singleton, can be used everywhere where util is imported:
format = Format(is_linux and format_enabled)
# the colored output can be toggled with format.enable(True|False)
