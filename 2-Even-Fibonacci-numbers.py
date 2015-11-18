#!/usr/bin/python

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

MAX = 4000000
i = 1
j = 2
s = i+j
SUM = 2
while s <= MAX :
#	print i,j,i+j
	if s % 2 == 0 : 
		SUM += s
		#print s
	i = j
	j = s
	s = i+j
	#print s

print SUM
