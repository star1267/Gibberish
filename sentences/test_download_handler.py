import pytest
from .download_handler import download



def test_download():
    dat = download()
    assert dat == True
    ...