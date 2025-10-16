import random
user=[]
computer=[]
def pick_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def showing(user,computer,status):
    print(f"your cards:{user} and sum={sum(user)}")
    if status=="n":
        print(f"computer cards:{computer}and sum={sum(computer)}")
    else:    
        print(f"computer cards:{computer[0]}")
def check(user,computer):
    if sum(user)>21 and 11 in user:
        user.remove(11)
        user.append(1)
    elif sum(user)>21:
        return -1
    elif sum(user)==sum(computer):
        return -2
    elif sum(user)>sum(computer):
        return -3
    elif sum(user)<sum(computer):
        return-4
def blcak_jack():
    game=input("do you want to play:y/n")
    if game=='y':
        for i in range(2):
            user.append(pick_card())
            computer.append(pick_card())
        showing(user,computer,status='y')
        while True:
            status=input("do you want another card:y/n")
            if status=='y':
                user.append(pick_card())
                computer.append(pick_card())
                showing(user,computer,status)
                stat=check(user,computer)
                if stat==-1:
                    print("you bust of!!!!")
                    return
            elif status=='n':
                showing(user,computer,status)
                stat=check(user,computer)
                if stat==-1:
                    print("you bust of!!!!")
                    return
                elif stat==-2:
                    print("Draw!!!!!!")
                    return
                elif stat==-3:
                    print("you won!!!!!!")
                    return
                elif stat==-4:
                    print("you lost!!!!")
                    return
            else:
                print("invalid stats")
    else:
        print("have good day")            

      
    
