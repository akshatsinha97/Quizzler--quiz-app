from tkinter import Tk, Canvas, PhotoImage, Button, Label
import html
from quiz import Quiz
class UI:

    def __init__(self, quiz):

        # initial user interface on instantiating class
        self.quiz = quiz
        self.TOTAL = 10
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.configure(bg='#126e82')
        self.window.geometry("500x600")              #widthxheight
        
        self.label = Label(text= f'SCORE: {self.quiz.score}', font= ('Showcard Gothic',15), relief= 'ridge', bg= '#f48b29')
        self.label.grid(row=0, column= 0, pady='20')

        self.canvas = Canvas(master=self.window, height=400, width=400)
        self.img = PhotoImage(file="GUI/images/quiz.png")
        self.image = self.canvas.create_image(200, 150, image= self.img)
        self.ques = self.canvas.create_text(200, 350, font= ('comic sans ms', 10, 'bold'),
        text= 'Question text here!', width= 370)
        self.canvas.grid(padx=50, pady=10)
        
        self.img1 = PhotoImage(file="GUI/images/tick.png")
        self.photoimage1 = self.img1.subsample(5, 5)
        self.true_button = Button(master= self.window, image= self.photoimage1,
        bg= 'white', height= 50, width= 100, command= self.true_pressed)
        self.true_button.place(x = 50, y = 500)
        self.img2 = PhotoImage(file="GUI/images/cross.png")
        self.photoimage2 = self.img2.subsample(5, 5)
        self.false_button = Button(master= self.window, image= self.photoimage2,
        bg= 'white', height= 50, width= 100, command= self.false_pressed)
        self.false_button.place(x = 350, y = 500)

        self.next_question()

        self.window.mainloop()

       
    def next_question(self):

        # changing question on every answer given by user
        self.canvas.config(bg= 'white')
        if self.quiz.is_remaining():
            self.label.config(text= f'SCORE: {self.quiz.score}/{self.TOTAL}')
            self.canvas.itemconfig(self.ques, text= self.quiz.questions())
        else:

            # changes to be made on the interface after no more questions are remaining
            self.canvas.itemconfig(self.ques, text= f'Quiz completed! Your final score is: {self.quiz.score}/{self.TOTAL} ')
            self.canvas.delete(self.image)
            if self.quiz.score > 50/100*self.TOTAL:
                self.img = PhotoImage(file="GUI/images/happy.gif")
                self.image_happy = self.img.subsample(2, 2)
                self.image = self.canvas.create_image(220, 180, image= self.image_happy)
            else:
                self.img = PhotoImage(file="GUI/images/sad.gif")
                self.image = self.canvas.create_image(200, 150, image= self.img)
            self.true_button.place_forget()
            self.false_button.place_forget()
            self.again = Button(master= self.window, text= 'Play Again?',
            font= ('Showcard Gothic',15), height= 2, width= 20, command= self.replay)
            self.again.place(x= 120, y= 500)

    def true_pressed(self):

        # answer check on true button pressed by user
        is_right = self.quiz.answer_check('True')
        self.give_feedback(is_right)
    
    def false_pressed(self):

        # answer check on false button pressed by user
        self.give_feedback(self.quiz.answer_check('False'))

    def give_feedback(self, is_right):

        # providing feedback to user after each question is answered
        if is_right:
            self.canvas.config(bg= 'green')
        else:
            self.canvas.config(bg= 'red')
        self.window.after(700, self.next_question)
    
    def replay(self):

        # destroying initial window and creating it again on specified button click
        self.window.destroy()
        self.quiz.replay_quiz()
        self.__init__(self.quiz) 

        

