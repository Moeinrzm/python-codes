import random
import game_data

logo=r"""        _       _               
  /\  /(_) __ _| |__   ___ _ __ 
 / /_/ / |/ _` | '_ \ / _ \ '__|
/ __  /| | (_| | | | |  __/ |   
\/ /_/ |_|\__, |_| |_|\___|_|   
          |___/                 
  _                             
 | | _____      _____ _ __      
 | |/ _ \ \ /\ / / _ \ '__|     
 | | (_) \ V  V /  __/ |        
 |_|\___/ \_/\_/ \___|_|   """
vs=r"""   __    
 /\   /\/ _\   
 \ \ / /\ \    
  \ V / _\ \   
   \_/  \__/"""
def pick_random():
    a=random.choice(game_data.data)
    
    game_data.data.remove(a)
    return a 

def compare(a,b,c):
    if a['follower_count']>b['follower_count'] and (c=='A'or c=="a"):
        return True
    elif a['follower_count']<b['follower_count'] and (c=='A'or c=="a"):
        return False
    elif a['follower_count']<b['follower_count'] and (c=='B'or c=="b"):
        return True
    elif a['follower_count']<b['follower_count'] and (c=='B' or c=="b"):
        return False

    

def game():
    final_score=0
    print(logo)
    a=pick_random()
    b=pick_random()
    print("welcome to higher or lower game")
    print(f"compare A : {a["name"]},a {a["description"]},from {a["country"]}")
    print(vs)
    print(f"against b:{b["name"]},a {b["description"]},from {b["country"]}")
    test=input("who has more follower: A/B")
    result=compare(a,b,test)
    if result:
        print("correct")
        final_score+=1
        a=b
        b=pick_random()
        while True:
            print(f"compare A : {a["name"]},a {a["description"]},from {a["country"]}")
            print(vs)
            print(f"against b:{b["name"]},a {b["description"]},from {b["country"]}")
            print(f"your score :{final_score}")
            test=input("who has more follower: A/B")
            result=compare(a,b,test)
            if result:
                final_score+=1
                print("correct")
                a=b
                b=pick_random()
            else:
                print("failed")   
                print(f"final score:{final_score}") 
                break
    else:
        print("failed")   
        print(f"final score:{final_score}") 
    print("thanks for playing")    

            
game()         
          



    
    
