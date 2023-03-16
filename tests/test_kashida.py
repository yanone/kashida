import sys
import os

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Lib"))
sys.path.insert(0, path)
from kashida import word, text


def test_word():
    assert word("كلمة") == "كلمـة"
    assert word("المانيا") == "المانيـا"
    assert word("الراي") == "الـراي"
    assert word("راي") == "راي"


def test_text():
    assert text("انا بحب الكشيدة") == "انـا بحـب الكشـيدة"
    # out-of-place punctuation w/o space:
    assert text("انا.بحب الكشيدة") == "انـا.بحـب الكشـيدة"
