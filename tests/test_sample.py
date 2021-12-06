# Sample Test passing with nose and pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from mypackage_da_dec21.core import MyClass


def test_pass():
    assert True, "dummy sample test"


def test_get_5():
    myclass = MyClass()
    assert myclass.get_5() == 5, "MyClass get_5 returns 5"
