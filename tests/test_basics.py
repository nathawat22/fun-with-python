import pytest
import math
from src.basics import area

def test_area_rect():
  assert area.area_rect(3,4) == 12


def test_area_circle():
  assert "{:.2f}".format(area.area_circle(4)) == 12.56
