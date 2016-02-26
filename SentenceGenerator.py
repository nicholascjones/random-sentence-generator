#!/usr/bin/env python

## SentenceGenerator.py
## Nicholas Jones
## Course Project 1 -- English Sentence Generator

#imports
import random


#List Initialization for Parts of Speech
proper = ['Nick','Alumni Hall','Sara','Pablo','Kanye','Pat','Notre Dame','Bernie Sanders', 'Donald Trump', 'Jaylon Smith']
common = ['dog','puppy','musician','player','campus','homework','computer','program','professor','friend','television','politician']
modifier = ['funny','stupid','weird','beautiful']
verb = ['runs','is','plays','jumps','sings','walks','screams','yells','performs','kicks']
prep = ['with','to','around','near','above','at']


#functions

#noun phrase takes argument to determine capitalization
def NounPhrase(case=0):

	phrase = ""
#	print phrase
	#establish random boolean value
	rn = random.randint(0,1)
#	print rn
	#if statement to determine
	if rn == 0: #if random int is zero, generate proper noun as phrase
		n = random.randint(0,(len(proper)-1)) #picks random index
	#	print n
	#	print proper[n]
		phrase = proper[n] #initializes to noun phrase plus space

	else: #if random int is 1, generate common noun phrase
		phrase = "The " #initializes phrase with "The"

		rn = random.randint(0,1) #re-initializes random int
		if rn == 1: #if random int is 1, need to include modifier
			n = random.randint(0,(len(modifier)-1)) #picks random index
			phrase += (modifier[n] + " ") #appends modifier and space to end of string
		
		#common noun implementation phase
		n = random.randint(0,(len(common)-1)) #picks random index
		phrase += common[n] #appends common noun to end of string
		if case == 1:
			phrase = phrase.lower()
	
	return phrase #noun phrase returned here

def PrepPhrase(): #prepositional phrase generator
	rn = random.randint(0,1) #re-initializes random int
	if rn == 0: #if random int is zero, no prepositional phrase
		return "" #return null string
	else: 
		n = random.randint(0,(len(prep)-1)) #picks random index of preposition
		phrase = " " + prep[n] + " " + NounPhrase(1)
		return phrase

def VerbPhrase(): #verb phrase generator
	rn = random.randint(0,1) #re-initializes random int
	n = random.randint(0,(len(verb)-1)) #picks random index
	phrase = " " + verb[n] + PrepPhrase()
	return phrase

	
def MakeSentence(): #makes sentence by combining noun and verb phrase

	x = NounPhrase() + VerbPhrase() #initialize sentence as such
	rn = random.randint(0,8) #re-initializes random int
	if rn == 0: #1/8 of time, use exclamation as punctuation
		x += "!"
	else: #7/8 of time, use period
		x += "."
	return x

#prints number of sentences given as argument
def NumSentences(n):
	i = 0
	while (i < n):
		print MakeSentence()
		i+=1
	print "\n" #newline needed

#function to add word to the dictionary
def AddWord():

	#starts by giving instructions
	print "Note: this generator only supports singular nouns and singular conjugations of verbs."
	print "Parts of speech are defined as follows:"
	print "Proper Noun = 'proper', Common Noun = 'common', Verb = 'verb', Modifer = 'modifier', Preposition - 'prep'"
	word = raw_input("What word would you like to input?\n")
	pos = raw_input("What part of speech is this word?\n")
	try: #ensures input is valid
		if pos == 'proper': #essential case switch to determine part of speech
			proper.append(word)
		elif pos == 'common':
			common.append(word)
		elif pos == 'verb':
			verb.append(word)
		elif pos == 'modifier':
			modifier.append(word)
		elif pos == 'prep':
			prep.append(word)
	except AttributeError: #if given invalid part of speech
		print "Sorry, that part of speech is invalid."
	return


#de-facto main function generation

#instructions
print "\n"
print "Hello, welcome to Nick's Random Sentence Generator!!"
print "\n"
print "Enter a positive integer to randomly generate that many sentences" 
print "Enter '+' to add a word to the dictionary."
print "Enter 'Q' to quit."
print "\n"
response = 'x' #generic response as to not cause problems

while (response != 'Q'): #case switch kills it all

	#prompt given with responses used to control flow
	response = raw_input("What would you like to do?\n")
	if response == 'Q':
		break
	elif response == '+':
		AddWord()
	else: 
		try:
			n = int(response)
			print "\n"
			if n > 0:
				NumSentences(n)
			else:
				print "Please enter a valid number."
		except ValueError:
			print "Invalid input. Please try again."
			continue
		


print "\n" #newline easy to print
#end execution



