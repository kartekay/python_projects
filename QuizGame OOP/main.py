from data import question_data
from quiz_brain import QuizBrain
from question_model import Questions
question_bank=[]
for i in question_data:
    qt=i["text"]
    qa=i["answer"]
    new_question=Questions(qt,qa)
    question_bank.append(new_question)
QB=QuizBrain(question_bank)

start=input("Do you want to start the game Y/N ? ")
if start=="Y":
    while 1==1:
      QB.nextquestion()
      QB.checkanswer()
      a=input("Do you want to continue Y/N ")
      if a=="Y":
          pass
      else:
          print("Thank you for playing, Your final score is ",QB.score)
          break



