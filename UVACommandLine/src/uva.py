# Foreign libraries
import dill
import clint
# Native modules
import os
import sys
import time
import getpass
# Own modules
import loginServices
import userServices
import consultSubmissions
import submit
import spellCorrector
import txt

persistence_file = txt.PERSISTENCE_FILENAME
USERNAME = ''
PASSWORD = ''
USERID = ''
POINTS = ''

def main():
	count = len(sys.argv)
	new_user = not os.path.isfile(persistence_file)
	if count == 1:
		# Interactive based mode
		print txt.HEADER
		print txt.MANUAL
		saved = True
		new_user = not os.path.isfile(persistence_file)		
		if new_user or not saved:			
			print
			print txt.WELCOME_MESSAGE
			print
			username = raw_input('Username: ')
			password = getpass.getpass("Password: ")
			saved = userServices.saving_user(username, password)
		new_user = not os.path.isfile(persistence_file)
		while new_user or not saved:
			print 'Try again'
			username = raw_input('Username: ')
			password = getpass.getpass("Password: ")
			saved = userServices.saving_user(username, password)
			new_user = not os.path.isfile(persistence_file)

		if not new_user and saved:
			USERNAME, PASSWORD, USERID, POINTS = userServices.load_user()
			print
			print 'Hello, ' + USERNAME
			print					

		cmds = ['submit', 'msubs', 'stats', 'browse', 'help', 'whoami']
		# TODO: EDIT, VIEW A file, STATS OF PROBLES, USER, BROWSE PROBLEMS
		# Customize error printing, comment. Add status, ranking, tests, hints
		# print problem!!!!!
		command = ''
		while command != 'quit':
			input_sequence = raw_input('~ ').split()
			command = input_sequence[0]
			if command == cmds[0]:
				if len(input_sequence) == 1:
					submit.submit(USERNAME, PASSWORD, '', '', '', 1)
				else:
					pass
				
			elif command == cmds[1]:
				# My sumbissions
				if len(input_sequence) == 1:
					consultSubmissions.consultSubmissions(USERID, 1, 0)
				else:
					num = input_sequence[1]
					if num.isdigit():
						consultSubmissions.consultSubmissions(USERID, 2, int(num))
					else:
						print 'Flag must be a number'
				
			elif command == cmds[2]:
				# Problem, and users statistics
				pass
				
			elif command == cmds[3]:
				# Browse a problem
				pass
				
			elif command == cmds[4]:
				# Print the manual
				print txt.MANUAL
				pass
				
			elif command == cmds[5]:
				# Print current logged user
				print USERNAME
				print USERID
				pass
				
			elif command != 'quit': 
				distances = dict((spellCorrector.levenshtein(command, real_command), real_command) for real_command in cmds)
				keys = distances.keys()
				minimum = min(keys)
				possible = distances[minimum]
				print txt.WRONG_COMMAND , possible



				# Remove user file, if temp session
				# TODO

		print txt.FINAL_MESSAGE

	elif count > 1:
		# Flag based submission
		flags = sys.argv
		if new_user:
			print txt.FLAG_BASED_AUTH_ERROR
		else:
			USERNAME, PASSWORD, USERID, POINTS = userServices.load_user()
			if count == 2:
				flag = flags[1]
				if flag == '-h':
					print txt.MANUAL
				if flag == '-sb':
					consultSubmissions.consultSubmissions(USERID, 0, 5)

			elif count == 3:
				flag = flags[1]
				mode = flags[2]
				if flag == '-sb':
					if mode.isdigit():
						consultSubmissions.consultSubmissions(USERID, 0, int(mode))
					else:
						print 'Mode must be an integer.'


		#if count == 2:

		# -h for help
		# -s <filename> for submit
		# -s <filename> <c_pp definition> for submit
		# -sb <num> for see user submissions, default num is 5
		# -st for see user statistics 
		pass

if __name__ == '__main__':
	main()