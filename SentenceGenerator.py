#!/usr/bin/env python

## SentenceGenerator.py
## Nicholas Jones
## Course Project 1 -- English Sentence Generator

#imports
import random


#List Initialization for Parts of Speech
proper = ['Nick','Mara','Will','Cat','Alumni Hall']
common = ['dog','puppy','musician']
modifier = ['funny','stupid','weird','beautiful']
verb = ['ran']
prep = ['in','to','around','on','above']


#functions

#noun phrase takes no arguments as is first part of sentence
def NounPhrase():

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
		phrase = proper[n] + " " #initializes to noun phrase plus space

	else: #if random int is 1, generate common noun phrase
		phrase = "the " #initializes phrase with "The"

		rn = random.randint(0,1) #re-initializes random int
		if rn == 1: #if random int is 1, need to include modifier
			n = random.randint(0,(len(modifier)-1)) #picks random index
			phrase += (modifier[n] + " ") #appends modifier and space to end of string
		
		#common noun implementation phase
		n = random.randint(0,(len(common)-1)) #picks random index
		phrase += (common[n] + " ") #appends common noun to end of string
	
	return phrase #noun phrase returned here

def PrepPhrase():
	rn = random.randint(0,1) #re-initializes random int
	if rn == 0: #if random int is zero, no prepositional phrase
		return "" #return null string
	else: 
		n = random.randint(0,(len(prep)-1)) #picks random index of preposition
		phrase = prep[n] + " " + NounPhrase()
		return phrase

#Start with Noun Phrase
sent = NounPhrase()
print PrepPhrase()

#print len(proper)
#print proper[0]



