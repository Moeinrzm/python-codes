from data import question_data
from quiz_brain import Quiz_Brain
class question :
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer

question_bank=[]
for test in question_data:
    question_text=test["text"]
    question_answer=test["answer"]
    q=question(question_text,question_answer)
    question_bank.append(q)
quiz=Quiz_Brain(question_bank)
while quiz.checking():
    quiz.question_next()




