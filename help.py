import nltk
from nltk.corpus import words

word_list = words.words()

words_five = [word.lower() for word in word_list if len(word) == 5]

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
print(word_scores[:20])
words_five = [word_score_tuple[0] for word_score_tuple in word_scores]
print(words_five[:20])

def print_words(words):
	num_words = len(words)
	print(str(num_words) + ' words')
	print(words[:100])


nltk.download('words')

solved = False
wordle = (None, None, None, None, None)
ruled_out = []
possible = []

while not solved:
	attempt = input("Input: ")

	if len(attempt) != 11:
		print('Unknown input')
		continue

	attempted_word = attempt[0:5]
	result = attempt[6:11]

	results = zip(attempted_word, result)

	letter_num = 0
	for result in results:
		letter = result[0]
		value = int(result[1])
		print('Check: ' + letter + '(' + str(value) + ')')
		if value == 0:
			words_five = [word for word in words_five if letter != word[letter_num]]
			print_words(words_five)
		if value == 1:
			words_five = [word for word in words_five if letter in word]
			print_words(words_five)
			words_five = [word for word in words_five if letter != word[letter_num]]
			print_words(words_five)
		if value == 2:
			words_five = [word for word in words_five if letter == word[letter_num]]
			print_words(words_five)

		letter_num = letter_num + 1

	print_words(words_five)
