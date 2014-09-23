from UVACommandLine.console import txt
import apiServices
import loginServices


persistence_file = txt.PERSISTENCE_FILENAME

def save_user(usr, password):	
	user_id = apiServices.username_to_id(usr)
	ans = [True, True]
	if(int(user_id) == 0):		
		ans[0] = False
	if(not loginServices.check_login(usr, password)):
		ans[1] = False
	if not ans[0] and not ans[1]:
		return ans
	fileobject = open(persistence_file, 'w')
	fileobject.write(str(usr) + '\n')
	fileobject.write(str(password) + '\n')
	fileobject.write(str(user_id) + '\n')
	fileobject.write(str(0))
	return ans

def saving_user(usr, password):
	ans = save_user(usr, password)
	if ans[0] == False:
		print txt.WRONG_USERNAME
		return False
	elif ans[1] == False:
		print txt.WRONG_PASSWORD
		return False
	return True

def load_user():
	fileobject = open(persistence_file, 'r')
	lines = [line.strip() for line in fileobject]
	USERNAME = lines[0]
	PASSWORD = lines[1]
	USERID = lines[2]
	POINTS = lines[3]
	return USERNAME, PASSWORD, USERID, POINTS