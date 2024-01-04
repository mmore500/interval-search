#!/usr/bin/env python

'''
`binary_search_recursive` tests for `interval_search` package.
'''

import pytest

import interval_search as inch


def test_binary_search_recursive_singleton():
    assert inch.binary_search_recursive(lambda __: True, 10, 10) == 10
    assert inch.binary_search_recursive(lambda __: False, 10, 10) is None


def test_binary_search_recursive():
    assert inch.binary_search_recursive(lambda x: x >= 5, 0, 100) == 5


def test_fruitless_binary_search_recursive():
    assert inch.binary_search_recursive(lambda x: False, 0, 100) is None


def test_empty_binary_search_recursive():
    def do_not_run(*args):
        assert False

    assert inch.binary_search_recursive(lambda x: False, 1, 0) is None
    assert inch.binary_search_recursive(lambda x: False, 1, -1) is None
    assert inch.binary_search_recursive(lambda x: False, 100, 99) is None
    assert inch.binary_search_recursive(lambda x: False, 100, 0) is None

    assert inch.binary_search_recursive(lambda x: True, 1, 0) is None
    assert inch.binary_search_recursive(lambda x: True, 1, -1) is None
    assert inch.binary_search_recursive(lambda x: True, 100, 99) is None
    assert inch.binary_search_recursive(lambda x: True, 100, 0) is None

    assert inch.binary_search_recursive(do_not_run, 1, 0) is None
    assert inch.binary_search_recursive(do_not_run, 1, -1) is None
    assert inch.binary_search_recursive(do_not_run, 100, 99) is None
    assert inch.binary_search_recursive(do_not_run, 100, 0) is None
    assert inch.binary_search_recursive(do_not_run, 100, 99) is None
    assert inch.binary_search_recursive(do_not_run, 100, 0) is None


@pytest.mark.parametrize("predicate_value", [True, False])
def test_out_of_bounds_extra(predicate_value: bool):
    def predicate(x: int) -> bool:
        assert 0 <= x < 2
        return predicate_value

    assert inch.binary_search_recursive(
        lambda i: predicate(i + 1),
        0,
        2 - 2,  # inclusive
    ) == (0 if predicate_value else None)
