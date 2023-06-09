#!/usr/bin/env python
import fileinput
import csv
import sys

# This prevents prematurely closed pipes from raising
# an exception in Python
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE, SIG_DFL)

# allow large content in the dump
csv.field_size_limit(sys.maxsize)

def is_insert(line):
    """
    Returns true if the line begins a SQL insert statement.
    """
    return line.startswith('INSERT INTO') or False

