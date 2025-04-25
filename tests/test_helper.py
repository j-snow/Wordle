import unittest

from functions import whittle_down


class HelperTest(unittest.TestCase):
	def test_one_correct_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']
		remaining_words = whittle_down('xxxxb', '00002', remaining_words)
		self.assertEqual(['aaaab'], remaining_words)

	def test_one_wrong_spot_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa']
		remaining_words = whittle_down('xxxxb', '00001', remaining_words)
		self.assertEqual(['aaaba', 'aabaa', 'abaaa', 'baaaa'], remaining_words)

	def test_one_wrong_char(self):
		remaining_words = ['aaaab', 'aaaba', 'aabaa', 'abaaa', 'baaaa', 'ccccc']
		remaining_words = whittle_down('xxxxb', '00000', remaining_words)
		self.assertEqual(['ccccc'], remaining_words)

	def test_double_word_answer(self):
		remaining_words = ['teeth', 'clean', 'learn']
		remaining_words = whittle_down('xxexx', '00200', remaining_words)
		self.assertEqual(['teeth', 'clean'], remaining_words)

	def test_double_e_guess(self):
		remaining_words = ['teeth', 'scene']
		remaining_words = whittle_down('xeexx', '01200', remaining_words)
		self.assertEqual(['scene'], remaining_words)

	def test_double_e_guess_no_2nd_e(self):
		remaining_words = ['teeth', 'scene']
		remaining_words = whittle_down('xeexx', '00200', remaining_words)
		self.assertEqual(['scene'], remaining_words)

	def test_double_e_guess_no_2nd_e_2_runs(self):
		remaining_words = ['teeth', 'scene']
		remaining_words = whittle_down('xxexx', '00200', remaining_words)
		remaining_words = whittle_down('xexxx', '01000', remaining_words)
		self.assertEqual(['scene'], remaining_words)


if __name__ == '__main__':
	unittest.main()
