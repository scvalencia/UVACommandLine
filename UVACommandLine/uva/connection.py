from UVACommandLine.services import apiServices
import submit

class uvaConnection(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.validation = submit.check_login(username, password)
        self.user_id = None
        self.submissions = None
        if self.validation:
            self.user_id = apiServices.username_to_id(username)
            self.submissions = apiServices.get_submissions(self.user_id)

    def submit_problem(self, lang, problem_number, filename, mode):
        if self.validation:
            submit.submit(self.username, self.password, lang, problem_number, filename, mode)
            self.submissions = apiServices.get_submissions(self.user_id)