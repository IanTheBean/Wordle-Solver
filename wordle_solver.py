import string, os

## APPROACH
## Step 1: count how many times the letters appear in all possible words
## Step 2: rank the letters based on appearance, the lower sscore the better
## Step 3: guess that word and get the results
## Step 4: parse the list and only keep possible results
## Step 5: repeat 1-4 util the wordle is solved

## the wordle class represents the answer to the puzzle
class Wordle_word:
	## yellows represent letters that must be in the word, but cannot be at the given index
	## greens represent letters that must be in the word at the given index
	## gray represents a letter that CANNOT be in the word
	def __init__(self):
		self.yellows = {}
		self.greens = {}
		self.grays = []

	def add_yellow(self, letter, index):
		self.yellows[letter] = index

	def add_green(self, letter, index):
		self.greens[letter] = index

	def add_gray(self, letter):
		self.grays.append(letter)

	## takes in a word and returns true if the word is a possbile answer
	def compare(self, word):
		for yellow in self.yellows:
			if not yellow in word or word[self.yellows[yellow]] == yellow:
				return False

		for green in self.greens:
			if not word[self.greens[green]] == green:
				return False

		for gray in self.grays:
			if gray in word:
				return False
			
		return True 
			

def get_best_word(wordle_word, disallowed_words):
	## get all of the lowercase letters in the alphabet
	letters = string.ascii_lowercase
	
	#create a dictionary to store the occurance of the letters
	letter_occurance_dict = {}
	letter_rank = {}
	
	# loop through the letters and create an entry in the dictionaryfor each one
	for letter in letters:
		letter_occurance_dict[letter] = 0
	
	## read the words from the list one at a time
	## for each word loop through the letters and append the dictionary correctly
	with open("words.txt", "r") as f:
		total_words = 0
		for line in f:
			if wordle_word.compare(line[:5]):
				total_words += 1
				for letter in line[:5]:
					if letter in letter_occurance_dict:
						letter_occurance_dict[letter] += 1
		print("there are " + str(total_words) + " total words")
		
					
	
	## sort the list by the most common letter
	rank = 0
	for w in sorted(letter_occurance_dict, key=letter_occurance_dict.get, reverse=True):
		letter_rank[w] = rank
		rank += 1

	## loop through all of the words and find the best word based on the letter occurance data
	best_word = ""
	best_score = 1000
	with open("words.txt", "r") as f:
		for line in f:
			if wordle_word.compare(line[:5]) and line[:5] not in disallowed_words:
				current_word_score = 0
				double_letter = []
				
				for letter in line[:5]:
					if letter in letter_occurance_dict:
						current_word_score += letter_rank[letter]

					## in order to help with double letters, we distribute a punishment to those words with multiple letters
					if letter in double_letter:
						current_word_score += 10
					else:
						double_letter.append(letter)
						
				if current_word_score < best_score:
					best_word = line
					best_score = current_word_score
				
	return best_word[:5]

w = Wordle_word()
disallowed_words = []
## interface to use the functions above and solve the wordle
while True:
	
	guess = get_best_word(w, disallowed_words)
	print("your guess is " + guess)
	data = input("Enter s for skip or enter the results(space for gray, y for yellow, and g for green):")

	if data[0] == "s":
		disallowed_words.append(guess)
	else:
		disallowed_words = []
		for i in range(len(data)):
			if data[i] == " ":
				w.add_gray(guess[i])
			if data[i] == "y":
				w.add_yellow(guess[i], i)
			if data[i] == "g":
				w.add_green(guess[i], i)
			

	os.system("clear")
	

