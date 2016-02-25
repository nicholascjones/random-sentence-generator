#!/usr/bin/env python

## SentenceGenerator.py
## Nicholas Jones
## Course Project 1 -- English Sentence Generator

#imports
import random

#functions

#noun phrase takes no arguments as is first part of sentence
def NounPhrase():

	#establish random boolean value
	rn = random.randint(0,1)

	#if statement to determine
	if rn == 0: #if random int is zero, generate proper noun as phrase
		n = random.randint(0,(len(proper)-1) #picks random index
		phrase = proper[n] + " " #initializes to noun phrase plus space

	else: #if random int is 1, generate common noun phrase
		phrase = "The " #initializes phrase with "The"

		rn = random.randint(0,1) #re-initializes random int
		if rn == 1: #if random int is 1, need to include modifier
			n = random.randint(0,(len(modifier)-1) #picks random index
			phrase += (modifier[n] + " ") #appends modifier and space to end of string
		
		
		

	
	return phrase #noun phrase returned here

#List Initialization for Parts of Speech
proper = []
common = []
modifier = []
verb = []
prep = []


#Start with Noun Phrase
sent = NounPhrase()



