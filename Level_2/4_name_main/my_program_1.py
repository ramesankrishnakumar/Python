"""
do not execute this file but execute `simple_import_pgm_2.py`
"""


def call_me():
    print(__name__)
    print("hello!")


# checks if it is a top level program
# if within the same module __name__ is given value __main__
# if not given the name of the file stripped of .py
if __name__ == '__main__':
    call_me()


call_me()