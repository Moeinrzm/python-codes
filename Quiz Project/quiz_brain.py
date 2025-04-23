class Quiz_Brain:
    def __init__(self,list):
        self.question_number=0
        self.question_list=(list)
        self.score=0
    def question_next(self):
       current_question=self.question_list[self.question_number]
       answer=input(f"Q.{self.question_number+1}:{current_question.text}(True/False): ")
       self.question_number+=1
       self.check_answer(current_question.answer,answer)
    def checking(self):
       return self.question_number!=len(self.question_list) 

    def check_answer(self,answer,user_answer):
        if answer.lower()==user_answer.lower():
            self.score+=1
            print(f"your score is {self.score}/{self.question_number}")
        else:
            print("wrong")
            print(f"your score is {self.score}/{self.question_number}")
            

             

           
         
         