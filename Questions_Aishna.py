from Question_data import question_data
 
class Questions:
    def __init__(self, question, answer):
        self.question=question
        self.answer=answer
 
class Quiz:
    def __init__(self, questions):
                #creating a list of Questions objects containing questions and answers
        self.questions=[Questions(q["text"], q["answer"]) for q in question_data]   
        self.score=0
        self.current_index = 0
 
    def next_question(self):
        if self.current_index < (len(self.questions)-1):
                return self.questions[self.current_index].question
        else:
                return None
 
    def check_answer(self, player_ans): #checking the answer
               
        if player_ans.lower() == self.questions[self.current_index].answer.lower():
            print ("Correct!\n")
            self.score+=2
        else:
            print ("Oops! Wrong Answer\n")
            self.score-=1 #negative marking
        self.current_index += 1
 
    def do_questions_remain(self):
        return self.current_index < (len(self.questions)-1) #to check if questions remain for running the loop
 
        
    def play_quiz(self):
        print("Are you ready? Let us begin!\n")     
        while self.do_questions_remain():
                print(self.next_question())
                player_ans = input("Enter 'True' for True or 'False' for False\n")
                if (player_ans.lower() != 'true' and player_ans.lower() != 'false'):
                    print("Invalid input. Enter 'True' or 'False'.\n")
                    continue
                self.check_answer(player_ans)
 
        print("Quiz over! That was a good attempt.\n")
        print(f"Your final score: {self.score}/{len(self.questions)}")
        
    @staticmethod
    def main():
        quiz = Quiz(question_data)
        quiz.play_quiz()
        
class caller:
    Quiz.main() #calling main method of Quiz class
