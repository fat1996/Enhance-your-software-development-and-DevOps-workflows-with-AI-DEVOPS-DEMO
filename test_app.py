import math
from app import average

def test_average_handles_empty():
    assert average([]) == 0

def test_average_rounds_half_up_to_int():
    # Spec: return an int, round half up (2.5 -> 3)
    assert average([2,3]) == 3  # (2+3)/2 = 2.5 -> 3 expected
    assert average([1,2,2]) == 2  # 1.666.. -> 2
    assert isinstance(average([2,3]), int)
