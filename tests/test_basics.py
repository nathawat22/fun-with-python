import pytest
from src.basics import area

def test_area_rect():
  assert area.area_rect(3,4) == 12
