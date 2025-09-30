import pytest
from .sentence_handler import build_sentence



def test_sentence():
    dat = build_sentence()
    assert dat == True
    ...