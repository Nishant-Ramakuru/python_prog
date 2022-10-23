"""Thus, passing them does not mean that your code is fully correct.
This test file is a starting point for you to write your own tests.
Pay attention to edge cases (e.g. zero, empty list, empty string, etc).
Your mark will also depend on how you have coded your answers.

Any additional test code you produce will not be marked directly, but it may help give you credit for demonstrating understanding, so it should be included in your fork as part of this test_cw.py file or in a separate file.

To run these tests, type `pytest test_cw.py` within this directory.
"""

import importlib  
py_cw = importlib.import_module("py_cw")


## Q1

def test_q1a():
	s = py_cw.cadd((1, 0), (0, 1))
	p = py_cw.cmult((3, 2), (9, 6))
	assert s == (1, 1) and p == (15, 36)


def test_q1b():
	assert py_cw.tocomplex(1, 2) == (1 + 2j) and py_cw.fromcomplex(1 + 1j) == (1, 1)


## Q2

def test_q2a():
	assert py_cw.seqandi([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxori([True, False, True, False], [True, True, False, False]) == [False, True, True, False]

def test_q2b():
	assert py_cw.seqandr([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorr([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


def test_q2c():
	assert py_cw.seqandlc([True, False, True, False], [True, True, False, False]) == [True, False, False, False] and py_cw.seqxorlc([True, False, True, False], [True, True, False, False]) == [False, True, True, False]


## Q3 


## Q4 

def test_q4_supermap():
    assert py_cw.supermap( lambda a : 2*a, [5, [5]]) == [10, [10]]


## Q5 

def test_q5_fenc():
	assert py_cw.fenc(4)==[[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]]


def test_q5_fdec():
	assert py_cw.fdec([[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]], [[[[[], [[]]], [[[], [[]]]]], [[[[], [[]]], [[[], [[]]]]]]]]])==4

## Q6 

def test_q6_love():
   x = py_cw.love()
   assert next(x) == "I love you"
   assert next(x) == "You love that I love you"
   assert next(x) == "I love that you love that I love you"

## Q7

def test_q7_removeall_oo():
    assert py_cw.removeall_oo(0, [0, 0, 1, 1, 0]) == [1, 1]

def test_q7_removeall_ft():
    assert py_cw.removeall_ft(0, [0, 0, 1, 1, 0]) == [1, 1]

def test_q7_removeall_rd():
    assert py_cw.removeall_rd(0, [0, 0, 1, 1, 0]) == [1, 1]

## Q8

def test_q8_sudan():
    assert py_cw.sudan(0,0,0) == 0 and py_cw.sudan(2,2,1) == 27

## Q9

## Q10

## Q11

# At this level you should be providing your own tests

## Q12

## Q13

def some_magic(mod):
    all_functions = inspect.getmembers(mod, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            value()

if __name__ == '__main__':
    some_magic(sys.modules[__name__])