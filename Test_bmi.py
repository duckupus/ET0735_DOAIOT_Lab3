import unittest
import importlib
bmi = importlib.import_module("ET0735-DOAIOT-Lab-2.bmi")

def test_bmi_normal_weight():
    assert(0 == bmi.calculate_bmi(height=1.74, weight=57))

def test_bmi_over_weight():
    assert(1 == bmi.calculate_bmi(height=1.2, weight=80))

def test_bmi_under_weight():
    assert(-1 == bmi.calculate_bmi(height=1.8, weight=40))


if __name__ == '__main__':
    unittest.main()
