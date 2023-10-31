import unittest
import employee_info as ei

def test_get_employees_by_age_range():
    result = []
    lower = 24
    upper = 39
    result = ei.get_employees_by_age_range(age_lower_limit=lower, age_upper_limit=upper)
    assert (len(result) == 4)

def test_calculate_average_salary():
    result = 0
    result = ei.calculate_average_salary()
    assert (int(result) == 60166)

def test_get_employees_by_dept():
    result = []
    param = "Engineering"
    expected = 2
    result = ei.get_employees_by_dept(param)
    assert (len(result) == expected)

if __name__ == '__main__':
    unittest.main()
