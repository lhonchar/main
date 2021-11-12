import homework11

from unit_test_framework import *


def UnitTestRun():
    def TestMyCalc():
        ExpectEqual(homework11.my_calc('2 + 3'), 5)
        ExpectEqual(homework11.my_calc('6 - 3'), 3)
        ExpectEqual(homework11.my_calc('15 * 1.5'), 22.5)
        ExpectEqual(homework11.my_calc('-100 + 30.5'), -69.5)
        ExpectEqual(homework11.my_calc('-10 - -100'), 90)

    TestMyCalc()

UnitTestRun()
