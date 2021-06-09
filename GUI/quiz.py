import html

class Quiz:

    def __init__(self, data):
        self.score = 0
        self.data = data
        self.index = 0
        self.answer = 0
        self.num = 0

    def is_remaining(self):

        # checks if questions from the response are remaining after each function call
        if self.num < len(self.data):
            self.num += 1
            return True
        else:
            return False

    def questions(self):
        
        # generating list of questions & cleaning html special characters & updating the question on each function call
        question_list = [ques['question'] for ques in self.data] 
        q_list = []
        for question in question_list:
            question = html.unescape(question)
            q_list.append(question)
        if self.index < len(q_list):
            format = f'{self.index+1}. {q_list[self.index]}'
            self.index += 1
            return format 
        else:
            return False

    def answer_check(self, u_answer):

        # parsing out answers from the response & checking the answer of the specific question 
        answer_list = [ans['correct_answer'] for ans in self.data] 
        if self.answer < len(answer_list):
            self.answer +=1
        if answer_list[self.answer-1] == u_answer:
            self.score += 1
            return True            
        else:
            return False
    
    def replay_quiz(self):

        # restarting the quiz
        self.__init__(self.data)
