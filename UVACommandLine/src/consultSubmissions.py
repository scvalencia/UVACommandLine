import datetime
import tabulate
import apiServices

def get_submissions(user_id, bound = 30):
	submissions = apiServices.get_submissions(user_id)[u'subs']
	submissions.sort(key = lambda x : x[0], reverse = True)
	slice_portion = submissions[:bound]
	return slice_portion

def encode_veredict(veredict):
	dct = { 10 : 'Submission error',
			15 : 'Can\'t be judged',
			20 : 'In queue',
			30 : 'Compile error',
			35 : 'Restricted function',
			40 : 'Runtime error',
			45 : 'Output limit',
			50 : 'Time limit Exceeded',
			60 : 'Memory limit',
			70 : 'Wrong answer',
			80 : 'PresentationE',
			90 : 'Accepted'
		  }
	if veredict not in dct.keys():
		return ' '
	return dct[veredict]

def encode_language(language):
	dct = {1 : 'C', 2 : 'Java', 3 : 'C++ 4', 4 : 'Pascal', 5 : 'C++ 11'}
	if language not in range(1, 6):
		return ' '
	return dct[language]

def encode_date(submission_time):
	str_time = str(submission_time)
	dt_object = datetime.datetime.fromtimestamp(submission_time)
	return dt_object.strftime('%Y-%m-%d')

def format_tuple(submission_row):
	if len(submission_row) != 7:
		return None

	submit_id = submission_row[0]
	problem_id = submission_row[1]
	veredict = submission_row[2]
	runtime = submission_row[3]
	submission_time = submission_row[4]
	language = submission_row[5]

	problem_info = apiServices.get_problem_by_id(problem_id)

	problem_number = str(problem_info[u'num'])
	problem_name = problem_info[u'title'].encode('ascii', 'ignore')
	problem = problem_number + ' ' + problem_name
	return [submit_id, problem, encode_veredict(veredict), encode_language(language), 
		runtime * 0.001, encode_date(submission_time)]

def get_table(items, user_id):
	submissions = get_submissions(user_id, items)
	ans = []
	for submission in submissions:
		ans.append(format_tuple(submission))
	return ans

def tabulate_information(table):
	headers = ["Submission ID", "Problem", "Veredict", "Language", "Run time", "Submission Date"]
	return tabulate.tabulate(table, headers, tablefmt = "grid")

def consultSubmissions(user_id, mode, size):
	if mode == 1:
		size = raw_input("Items in the table: ")
		if size.isdigit():
			size = int(size)
			table = get_table(size, user_id)
			print
			print tabulate_information(table)
			print
		else:
			print 'Size must be a number.'
	else:
		table = get_table(size, user_id)
		print
		print tabulate_information(table)
		print