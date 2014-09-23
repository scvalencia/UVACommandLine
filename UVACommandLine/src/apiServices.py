import requests
import json

def username_to_id(username):
	"""Gets the UVA user ID of a user by ots username.

	Retrieves the user's id corresponding to UVA notation
	using the uHunt API available as static pages serving 
	json files. Silly thing may happen if username types
	is not a valid username.

	Args:
		username: An string representing the username of
			a UVA user.

	Returns:
		An string object where every character is a digit.
		If the username is not a valid UVA username, it is
		zero, otherwise, it is the user ID corresponding to
		the provided user username.

	"""

	url = 'http://uhunt.felix-halim.net/api/uname2uid/' + str(username)
	resp = requests.get(url)
	data = json.loads(resp.text)
	return str(data)

def problem_list():
	"""Gets the current UVA problems available for users to solve

	Retrieves a json object corresponding the list of problems available
	at the moment of execution at the UVA online judge wep page. The list
	of problems, is available via the uHunt API as a static json file seved
	at the UVA web page.

	Returns:
		A list of lists of problems attributes. Each row in the returned
		object is a list, an every object in these list is a problem
		attribute. For example:

		If there was just one available proble at the UVA web page, 
		the returned object would look like:

		[
			[
				36,
				100,
				"The 3n + 1 problem",
				62964,
				0,
				1000000000,
				0,
				6515,
				0,
				0,
				95942,
				0,
				52354,
				74,
				49990,
				5209,
				222083,
				4123,
				161183,
				3000,
				1
			]
		]

		At the second level (the enclosed lists), the information is 
		classified with 21 elements classified as:

		0.  Problem ID
		1.  Problem Number
		2.  Problem Title
		3.  Number of Distinct Accepted User (DACU)
		4.  Best Runtime of an Accepted Submission
		5.  Best Memory used of an Accepted Submission
		6.  Number of No Verdict Given (can be ignored)
		7.  Number of Submission Error
		8.  Number of Can't be Judged
		9.  Number of In Queue
		10. Number of Compilation Error
		11. Number of Restricted Function
		12. Number of Runtime Error
		13. Number of Output Limit Exceeded
		14. Number of Time Limit Exceeded
		15. Number of Memory Limit Exceeded
		16. Number of Wrong Answer
		17. Number of Presentation Error
		18. Number of Accepted
		19. Problem Run-Time Limit (milliseconds)
		20. Problem Status (0 = unavailable, 1 = normal, 2 = special judge)

	"""

	url = 'http://uhunt.felix-halim.net/api/p'
	resp = requests.get(url)
	data = json.loads(resp.text)
	return data

def get_problem(problem_id, problem_number, by_id, by_number):
	"""Gets an UVA problem information via its id, or its number, exclusively.

	Retrieves a problem infomration using the id or the number
	of the problem. If by_id is on, and by_number is not, this
	function will return a dictionary from a json object, 
	representing the information of a problem. Otherwise if the
	by_number flag is on, and the by_id flag is off, the request 
	would be processed via the problem's number. If both flags 
	are on, this function would behave silly, and would not 
	be an object to return.

	Args:
		problem_id: An int representing the problem id.
		problem_number: An int representing the problem number.
		by_id: A boolean value, representing wether or not the 
			request should be processed usign the problem id.
		by_number: A boolean value, representing wether or not the 
			request should be processed usign the problem number.

	Returns:
		A dict mapping the classification labels with the actual 
		requested problem information. The keys represent the following
		information.

		pid    Problem ID
		num    Problem Number
		title  Problem Title
		dacu   Number of Distinct Accepted User (DACU)
		mrun   Best Runtime of an Accepted Submission
		mmem   Best Memory used of an Accepted Submission
		nover  Number of No Verdict Given (can be ignored)
		sube   Number of Submission Error
		noj    Number of Can't be Judged
		inq    Number of In Queue
		ce     Number of Compilation Error
		rf     Number of Restricted Function
		re     Number of Runtime Error
		ole    Number of Output Limit Exceeded
		tle    Number of Time Limit Exceeded
		mle    Number of Memory Limit Exceeded
		wa     Number of Wrong Answer
		pe     Number of Presentation Error
		ac     Number of Accepted
		rtl    Problem Run-Time Limit (milliseconds)
		status Problem Status (0 = unavailable, 1 = normal, 2 = special judge)

	"""

	url = ''
	resp = None
	data = None
	if by_id and by_number:
		return None
	elif by_id:
		url = 'http://uhunt.felix-halim.net/api/p/id/' + str(problem_id)
	elif by_number:
		url = 'http://uhunt.felix-halim.net/api/p/num/' + str(problem_number)
	if url != '':
		resp = requests.get(url)
		data = json.loads(resp.text)
	return data

def get_problem_by_id(problem_id):
	"""Gets the problem information given its id.

	See get_problem documentation for further information"""

	return get_problem(problem_id, None, True, False)

def get_problem_by_number(problem_number):
	"""Gets the problem information given its number.

	See get_problem documentation for further information"""

	return get_problem(None, problem_number, False, True)

def get_submissions(user_id):
	"""Gets the submissions by user given its id.

	Retrieves the user's sumbissions given the user id.
	This function connects to the uHunt API, that provides
	information services for this kind of stuff. This should
	baheve as expected for a correct user_id. The behaviour 
	is undefined with wrogn user_id. 

	Args:
		user_id: The id of a UVA user.

	Returns:
		A dict containing information on the user, its username
		and it submissions. The subs key, is an array representing 
		each element, a submission by the user. The information in 
		every element of the subs array is classified as follows:

		0. Submission ID (In the UVA server, the older the lesser)
		1. Problem ID (The typic problem ID)
		2. Veredict ID (See below)
		3. Runtime (In milliseconds)
		4. Submission Time (UNIX timestamp)
		5. Language ID (C = 1, 2 = Java, 3 = C++, 4 = Pascal, 5 = C++ 11)
		6. Submission Rank

		For the Veredict Id:
			10 : Submission error
			15 : Can't be judged
			20 : In queue
			30 : Compile error
			35 : Restricted function
			40 : Runtime error
			45 : Output limit
			50 : Time limit
			60 : Memory limit
			70 : Wrong answer
			80 : PresentationE
			90 : Accepted

	"""

	url = 'http://uhunt.felix-halim.net/api/subs-user/' + str(user_id)
	resp = requests.get(url)
	data = json.loads(resp.text)
	return data