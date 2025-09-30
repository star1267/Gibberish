import pytest
from .word_handler import split_words



def test_splitting():
    dat = split_words()
    assert dat == True
    ...