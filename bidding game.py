bidders = {}
while 1==1:
 name = input("Enter the name of the bidder ")
 bid = int(input("Enter the bid "))
 bidders[name]=bid
 a=input("Enter yes to continue or no to stop ")
 if a=="yes":
     print("\n"*40)     
 else:
     l1=[]
     for i in bidders:
         l1.append(bidders[i])
     for j in bidders:
         if bidders[j]==max(l1):
             print("The highest bid is ",max(l1),"by ",j)
     break
