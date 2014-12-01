#!/usr/bin/env python

#---------------------------------------
#password_test.py
#	example of if/else, lists, assignments, raw_input
#	comments and evalutations
#---------------------------------------
# Assign the users and passwords
users = ['Fred', 'John', 'Steve', 'Ann', 'Mary']
passwords = ['access', 'dog', '12345', 'kids', 'qwerty']
#---------------------------------------
#Get username and password
usrname = raw_input('Enter your username => ')
pwd = raw_input('Enter your password => ')
#---------------------------------------
#Check to see if user is in the list
if usrname in users:
	position = users.index(usrname) 
	if pwd == passwords[position]:
		print 'Hi there, %s. Access granted.' % users[position]
	else:
		print 'Password incorrect. Access denied.'
else:
	print 'Sorry...I don\'t recognize you. Access denied.'
	
	
