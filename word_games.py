def main():
	print (score("zzz"))
def score(word):
	count = 0
	for element in word:
		if element in [ "a", "e", "i", "l", "r", "s", "t", "u", "o"]:
			count = count + 1
		elif element in ["d", "g"]:
			count = count + 2
		elif element in ["b", "c", "m", "p"]:
			count = count + 3
		elif element in ["f", "h", "v", "w", "y"]:
			count = count + 4
		elif element in ["k"]:
			count = count + 5
		elif element == ["j", "x"]:
			count = count + 8
		elif element in ["q", "z"]:
			count = count + 10
	return count
main()