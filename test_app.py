import math
from app import average

def test_average_handles_empty():
    assert average([]) == 0

def test_average_rounds_half_up_to_int():
    assert average([2,3]) == 2.5
    assert average([1,2,3]) == 2
