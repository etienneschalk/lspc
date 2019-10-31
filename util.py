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


# print percent bar. fraction must be float between 0 and 1
def print_percent_bar(fraction, size=50, newLine=True):
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


# print dots
def print_dots(numberOfDots=10, newLine=True, char="■"):
    print(char * numberOfDots, sep='', end= '\n' if newLine else '')


# print horizontal line
def horizontal_line(bold=0, size=80):
    if bold:
        print("=" * size)
    else:
        print("-" * size)


# format text (for UNIX). usage: print(Color.OKBLUE)
class Color:
    HEADER = '\033[95m' if is_linux and format_enabled else ''
    OKBLUE = '\033[94m' if is_linux and format_enabled else ''
    OKGREEN = '\033[92m' if is_linux and format_enabled else ''
    WARNING = '\033[93m' if is_linux and format_enabled else ''
    FAIL = '\033[91m' if is_linux and format_enabled else ''
    ENDC = '\033[0m' if is_linux and format_enabled else ''
    BOLD = '\033[1m' if is_linux and format_enabled else ''
    UNDERLINE = '\033[4m' if is_linux and format_enabled else ''
    YELLOW = '\033[33m' if is_linux and format_enabled else ''
    MAGENTA = '\033[35m' if is_linux and format_enabled else ''
    CYAN = '\033[36m' if is_linux and format_enabled else ''
