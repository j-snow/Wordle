def print_words(words):
	num_words = len(words)
	print(str(num_words) + ' words')
	print(words[:100])

def whittle_down(attempted_word, result, five_letter_words):
	results = zip(attempted_word, result)

	letter_num = 0
	for result in results:
		letter = result[0]
		value = int(result[1])
		if value == 0:
			if attempted_word.count(letter) == 1:
				five_letter_words = [word for word in five_letter_words if letter not in word]
			else:
				five_letter_words = [word for word in five_letter_words if letter != word[letter_num]]
		if value == 1:
			five_letter_words = [word for word in five_letter_words if letter in word]
			five_letter_words = [word for word in five_letter_words if letter != word[letter_num]]
		if value == 2:
			five_letter_words = [word for word in five_letter_words if letter == word[letter_num]]

		letter_num = letter_num + 1

	return five_letter_words