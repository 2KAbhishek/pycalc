from calculator import Calculator

class Calculator_Test:
    def test_add(self):
        calc = Calculator("HP", "electricity")
        assert calc.add(2, 2) == 4
        assert calc.add(0, 0) == 0
        assert calc.add(-1, -1) == -2

    def test_subtract(self):
        calc = Calculator("Cassio", "solar")
        assert calc.subtract(3, 2) == 1
        assert calc.subtract(0, 5) == -5
        assert calc.subtract(-1, -1) == 0

    def test_multiply(self):
        calc = Calculator("Dell", "battery")
        assert calc.multiply(3, 2) == 6
        assert calc.multiply(0, 4) == 0
        assert calc.multiply(-1, -10) == 10

    def test_divide(self):
        calc = Calculator("Cassio", "electricity")
        assert calc.divide(6, 2) == 3
        assert calc.divide(12, 3) == 4
        assert calc.divide(-1, -1) == 1

    def test_exponent(self):
        calc = Calculator("Dell", "electricity")
        assert calc.exponent(2, 3) == 8
        assert calc.exponent(0, 0) == 1
        assert calc.exponent(-1, -1) == -1

    def test_log(self):
        calc = Calculator("HP", "solar")
        assert calc.log(2, 2) == 1
        assert calc.log(8, 2) == 3
        assert calc.log(16, 2) == 4

    def test_square_root(self):
        calc = Calculator("HP", "battery")
        assert calc.square_root(4) == 2
        assert calc.square_root(9) == 3
        assert calc.square_root(16) == 4

    def test_sin(self):
        calc = Calculator("Cassio", "battery")
        assert calc.sin(0) == 0
        assert calc.sin(90) == 0.8939966636005579
        assert calc.sin(180) == -0.8011526357338304

    def test_cos(self):
        calc = Calculator("Dell", "solar")
        assert calc.cos(0) == 1
        assert calc.cos(90) == -0.4480736161291701
        assert calc.cos(180) == -0.5984600690578581

    def test_tan(self):
        calc = Calculator("HP", "electricity")
        assert calc.tan(0) == 0
        assert calc.tan(90) == -1.995200412208242
        assert calc.tan(180) == 1.3386902103511544

    def test_calculator_str(self):
        calc = Calculator("HP", "electricity")
        assert str(calc) == "Calculator by HP, runs on electricity"


if __name__ == "__main__":
    calc_test = Calculator_Test()
    calc_test.test_add()
    calc_test.test_subtract()
    calc_test.test_multiply()
    calc_test.test_divide()
    calc_test.test_exponent()
    calc_test.test_log()
    calc_test.test_square_root()
    calc_test.test_sin()
    calc_test.test_cos()
    calc_test.test_tan()
    calc_test.test_calculator_str()
    print("All tests passed!")
