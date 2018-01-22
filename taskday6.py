from collections import Counter
def descending_word():
	word_count = Counter()

	with open("out1.txt","r+") as file:
	word_count.update((word for word in file.read().split()))

		for word, count in word_count.most_common():
descending_word(print word, count)

