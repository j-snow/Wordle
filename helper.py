from functions import print_words, whittle_down

words_file = open('words.txt', 'r')
five_letter_words = words_file.read().split("\n")

letter_frequencies = {}
for word in five_letter_words:
	for i in range(0, 5):
		letter = word[i]
		if letter not in letter_frequencies:
			letter_frequencies[letter] = 0

		letter_frequencies[letter] = letter_frequencies[letter] + 1

letter_score = sorted(letter_frequencies, key=lambda x: letter_frequencies[x], reverse=True)
word_scores = [(word, sum([letter_score.index(letter) for letter in word]), len(set(word))) for word in five_letter_words]
word_scores = sorted(word_scores, key=lambda tup: tup[1])
word_scores = sorted(word_scores, key=lambda tup: tup[2], reverse=True)
# TODO sort by position likelihood
five_letter_words = [word_score_tuple[0] for word_score_tuple in word_scores]


print_words(five_letter_words)

while len(five_letter_words) > 1:
	attempt = input("Input: ")

	if len(attempt) != 11 or attempt[5] != ',':
		exit(0)

	attempted_word, result = attempt.split(',')

	five_letter_words = whittle_down(attempted_word, result, five_letter_words)
	print_words(five_letter_words)