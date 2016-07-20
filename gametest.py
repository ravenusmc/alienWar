import unittest

from battle import valid

class GameTest(unittest.TestCase):

  def test_valid(self):
    #Does the function return true/false
    answer = valid('y')
    answer2 = valid('t')
    self.assertTrue(answer, True)
    self.assertFalse(answer2, False)


unittest.main()