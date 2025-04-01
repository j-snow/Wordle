# How to run
## Prerequisites
Will need NLTK installed, `pip install nltk`

## Solve wordle
Run the script `python help.py`

It shows a list of words, starting with the words that have the most common.
Give it you input and result in the style of aaaaa,00000. So your 5 letter word, then a comma then the result, 0=grey, 1=yellow, 2=green.
The list gets narrowed down following based on the result.

# Caveats
This just uses the words from nltk.corpus, narrowed down to 5 letter words. Many are not accepted by wordle.