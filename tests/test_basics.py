import pytest
import math
from src.basics import area

def test_area_rect():
  assert area.area_rect(3,4) == 12


def test_area_circle():
  circle_area = "{:.2f}".format(area.area_circle(4))
  assert float(circle_area) == pytest.approx(50.27)
  # assert circle_area == '50.27'
