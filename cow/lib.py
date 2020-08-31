# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for cow Project
"""

import cowsay

if __name__ != '__main__':
    cowsay.cow('Have fun!')

def say_hello(message='hello'):
    """ say hello
    """
    cowsay.stegosaurus(message)


if __name__ == '__main__':
    say_hello()
