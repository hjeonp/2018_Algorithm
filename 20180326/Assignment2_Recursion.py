#!/usr/bin/python3

#Assignment2_Recursion.py
#180331

raw_sentence = input()
words = [i for i in raw_sentence.split()]

for i in range(len(words)):
	words[i] = words[i].lower()

def conv_to_dict(words): #converts the word array to dict of word and num
	wordDict = {}
	for word in words:
		if word in wordDict:
			wordDict[word] += 1
		else:
			wordDict[word] = 1

	return wordDict 

def find_most(wordDict): #finds the most frequent word in dic, not considering same, if so, it returns the first
	most_word = ""
	most_num = 0
	for i in wordDict.keys():
		if wordDict[i] > most_num:
			most_word = i
			most_num = wordDict[i]

	return (most_word, most_num)

def find_ascii(most_word):
	minn = maxx = most_word[0]
	for i in range(len(most_word)):
		if(most_word[i] > maxx): 
			maxx = most_word[i]
		if(most_word[i] < minn):
			minn = most_word[i]

	return (ord(minn), ord(maxx))

def factorial(n):
	if(n==1):
		return 1
	else:
		return n*factorial(n-1)

def fibonacci(n):
	if(n==1): 
		return 1
	elif(n==2):
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

def gcd(a, b):
	while b:
		a, b = b, a%b
	return a

wordDict = conv_to_dict(words)

most = find_most(wordDict)
most_word = most[0]; most_num = most[1]

minmax = find_ascii(most_word)
minn = minmax[0]; maxx = minmax[1];

##############################################################

sum = 0
for i in range(len(most_word)):
	sum += ord(most_word[i])

print("Most Frequent Word:{}, Max ASCII:{}, Min ASCII:{}, Sum:{}".format(most_word, maxx, minn, sum))
print(factorial(minn))
print()

##############################################################

n=1
while(fibonacci(n) <= sum):
	print(fibonacci(n), end=" ")
	n += 1
print()

###############################################################

g = gcd(ord(most_word[0]), ord(most_word[1]))
for i in range(2, len(most_word)):
	g = gcd(g, ord(most_word[i]))
print(g)

print()

###############################################################

exist = [0, 0, 0, 0, 0]
letter = ['e', 't', 'o', 'a', 'n']
for i in range(len(raw_sentence)):
	for j in range(5):
		if(raw_sentence[i] == letter[j]):
			exist[j] += 1

for j in range(5):
	if(exist[j] > 0):
		print("Sequential Search: {} Exist!".format(letter[j]))

print()

###############################################################

sorted_list = []
for i in range(len(raw_sentence)):
	sorted_list.append(raw_sentence[i])
sorted_list.sort()

letter = ['e', 't', 'o', 'a', 'n']

def binary_search(sorted_list, target):
	first = 0; last = len(sorted_list) - 1
	if len(sorted_list) == 0:
		return 0
	else:
		mid = (first + last) // 2
		if target == sorted_list[mid]:
			return 1
		else:
			if sorted_list[mid] < target:
				return binary_search(sorted_list[mid+1:], target)
			else:
				return binary_search(sorted_list[:mid], target)

for i in range(5):
	if(binary_search(sorted_list, letter[i]) == 1):
		print("Binary Search: {} Exist!.".format(letter[i]))

print()

###############################################################

small = big = ord(raw_sentence[0])
for i in range(len(raw_sentence)):
	if(ord(raw_sentence[i]) > big):
		big = ord(raw_sentence[i])
	if(ord(raw_sentence[i]) < small):
		small = ord(raw_sentence[i])

print("Max: {} Min: {}".format(big, small), end="")

print()

###############################################################

for i in range(len(raw_sentence)):
	print(bin(ord(raw_sentence[i])), end=" ")

print()

###############################################################
