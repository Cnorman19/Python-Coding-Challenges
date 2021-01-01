import sys
word = sys.argv[1]

def stutter(word):


	wordStack = []

	wordStack.append(word[0])
	wordStack.append(word[1])

	for i in range(0,2):
		print(wordStack[0] + wordStack[1], "..." , end = " ")

	print(word + "?")


stutter(word)