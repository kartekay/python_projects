class QuizBrain:
    def __init__(self,qlist):
        self.question_number=0
        self.score=0
        self.qlist=qlist
    def nextquestion(self):
        self.question_number+=1
        print("Q"+str(self.question_number),"\n",self.qlist[self.question_number-1].question)
    def checkanswer(self):
        entered=input("Enter your answer ")
        if self.qlist[self.question_number-1].answer==entered:
           self.score+=1
           print("Your score is ",self.score)
        else:
           print("Your score is ", self.score)


