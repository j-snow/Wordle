import unittest

from functions import whittle_down


class HelperTest(unittest.TestCase):
	def test_one_correct_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']
		remaining_words = whittle_down('xxxxb', '00002', remaining_words)
		self.assertEquals(['aaaab'], remaining_words)

	def test_one_wrong_spot_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']
		remaining_words = whittle_down('xxxxb', '00001', remaining_words)
		self.assertEquals(['aaaba', 'aabaa', 'abaaa', 'baaaa'], remaining_words)

	def test_one_wrong_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']
		remaining_words = whittle_down('xxxxb', '00000', remaining_words)
		self.assertEquals([], remaining_words)

if __name__ == '__main__':
	unittest.main()