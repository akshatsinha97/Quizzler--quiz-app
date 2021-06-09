import html

class Quiz:

    def __init__(self, data):
        self.score = 0
        self.data = data
        self.index = 0

    def questions(self):
        
        # parsing out questions from the response & cleaning html special characters and generating list of questions
        question_list = [ques['question'] for ques in self.data] 
        q_list = []
        for question in question_list:
            question = html.unescape(question)
            q_list.append(question)
        return q_list  
        
    def answer_check(self):

        # parsing out answers from the response & checking the answer of the specific question 
        answer_list = [ans['correct_answer'] for ans in self.data] 
        for data_answer in answer_list:
            u_answer = input('(T/F)? ')
            if u_answer.upper() == 'T':
                u_answer = 'True'

            elif u_answer.upper() == 'F':
                u_answer = 'False'

            if data_answer == u_answer:
                return True
            else:
                return False

    def final_format(self):

        # Updating the score after each question and providing the respective feedback
        q_list = self.questions()
        for question in q_list:
            self.index += 1
            print(f'{self.index}. {question}')
            
            if self.answer_check():
                print('Well done! Right Answer')
                self.score += 1
                print(f'Score: {self.score}/10\n')
            else:
                print('Sorry! Wrong Answer')
                print(f'Score: {self.score}/10\n')

        print(f'Quiz completed! Your final score is: {self.score}/10')