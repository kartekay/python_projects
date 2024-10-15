import random
words_list = ['nation', 'county', 'police', 'friend']
while True:
 x=input("Do you want to add more words Y or N ? ")
 if x=="Y":
    z= int(input("How many ?"))
    while d<z:
       r=str(input("Enter Word"))
       z-=1
       words_list.append(r)
 A = input("Enter Y to begin the game ")
 stages = ['stage1', 'stage2', 'stage3', 'stage4', 'stage5', 'stage6']
 hanger = ["\b|\n\b|\n\bO", "\b|\n\b|\n\bO\n\b|", "\b|\n\b|\n\bO\n\b|\ ", "\b|\n\b|\n\bO\n/|\ ", "\b|\n\b|\n\bO\n/|\ \n/",
          "\b|\n\b|\n\bO\n/|\ \n/\b\ "]
 if A == "Y":

    b = words_list[random.randint(0, len(words_list) - 1)]
    b = list(''.join(b))
    print("The Game Begins")
    r = 0
    i = 0
    String=['_','_','_','_','_','_']
    while r<len(b):
        c = input("Enter a alphabet in the word chosen ")
        if c in b:
            if c in String:
                print("Already Guessed")
            else:
               i+=1
               for k in range (0,len(b)): 
                if b[k]==c:
                   String[k]=c
               print(' '.join(String))
        else:
            r += 1
            stage = 'stage' + str(r)
            number = stages.index(stage)
            print(hanger[number])
            print(6-r," Trials remaining")
        if '_' not in String:
              print("Winner")
              break
        elif r==len(b):      
              print("Game Over")
    
