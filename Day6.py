import random
while True:
 

 words_list = ['nation', 'county', 'police', 'friend']
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
    while r,i < len(b):
        c = input("Enter a alphabet in the word chosen ")
        if c in b:
            i+=1
            String[b.index(c)]=c
            print(' '.join(String))
        else:
            r += 1
            stage = 'stage' + str(r)
            number = stages.index(stage)
            print(hanger[number])
            print(6-r," Trials remaining")
    if i==len(b):
              print("Winner")
    else:      
              print("Game Over")
