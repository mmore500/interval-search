"""Top-level package for interval_search."""

__author__ = """Matthew Andres Moreno"""
__email__ = 'm.more500@gmail.com'
__version__ = '0.3.1'

from .binary_search import binary_search
from .curried_binary_search import curried_binary_search
from .curried_doubling_search import curried_doubling_search
from .curried_iterative_binary_search import curried_iterative_binary_search
from .doubling_search import doubling_search
from .interval_search import interval_search
from .iterative_binary_search import iterative_binary_search

# adapted from https://stackoverflow.com/a/31079085
__all__ = [
    'binary_search',
    'curried_binary_search',
    'curried_doubling_search',
    'curried_iterative_binary_search',
    'doubling_search',
    'iterative_binary_search',
    'interval_search',
]
