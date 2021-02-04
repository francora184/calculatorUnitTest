import unittest

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mult(a, b):
  return a * b

def div(a, b):
  if(b == 0):
    return -1
  else:
    return a / b

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(1,2), 3)
    self.assertEqual(add(-1,3), 2)
    self.assertEqual(add(-1,-1), -2)

  def test_sub(self):
    self.assertEqual(sub(2,1), 1)
    self.assertEqual(sub(2,-1), 3)
    self.assertEqual(sub(-1,-1), 0)

  def test_mult(self):
    self.assertEqual(mult(2,2), 4)
    self.assertEqual(mult(-2,2), -4)
    self.assertEqual(mult(-2,-2), 4)

  def test_div(self):
    self.assertEqual(div(10,2), 5)
    self.assertEqual(div(10,0), -1)
    self.assertEqual(div(10,-2), -5)

if __name__ == '__main__':
  unittest.main()