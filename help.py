import nltk
from nltk.corpus import words

nltk.download('words')
# TODO Find a better source of words, some of these are not in wordle's dictionary
word_list = words.words()

words_five = [word.lower() for word in word_list if len(word) == 5]
words_five = list(set(words_five))

letter_frequencies = {}
for word in words_five:
	for i in range(0, 5):
		letter = word[i]
		if letter not in letter_frequencies:
			letter_frequencies[letter] = 0

		letter_frequencies[letter] = letter_frequencies[letter] + 1

letter_score = sorted(letter_frequencies, key=lambda x: letter_frequencies[x], reverse=True)
word_scores = [(word, sum([letter_score.index(letter) for letter in word]), len(set(word))) for word in words_five]
word_scores = sorted(word_scores, key=lambda tup: tup[1])
word_scores = sorted(word_scores, key=lambda tup: tup[2], reverse=True)
# TODO sort by position likelihood
words_five = [word_score_tuple[0] for word_score_tuple in word_scores]

def print_words(words):
	num_words = len(words)
	print(str(num_words) + ' words')
	print(words[:100])

print_words(words_five)

solved = False
wordle = (None, None, None, None, None)
ruled_out = []
possible = []

while not solved:
	attempt = input("Input: ")

	if len(attempt) != 11 or attempt[5] != ',':
		exit(0)

	attempted_word, result = attempt.split(',')

	results = zip(attempted_word, result)

	letter_num = 0
	for result in results:
		letter = result[0]
		value = int(result[1])
		if value == 0:
			if attempted_word.count(letter) == 1:
				words_five = [word for word in words_five if letter not in word]
			else:
				words_five = [word for word in words_five if letter != word[letter_num]]
			# TODO: does not count none doubles
		if value == 1:
			words_five = [word for word in words_five if letter in word]
			words_five = [word for word in words_five if letter != word[letter_num]]
		if value == 2:
			words_five = [word for word in words_five if letter == word[letter_num]]

		letter_num = letter_num + 1

	print_words(words_five)
