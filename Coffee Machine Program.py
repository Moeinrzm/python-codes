resource={
    "water":500,
    "milk":500,
    "coffee":100,
    "money":0
    }
menu={
    "latte":{
        "contents":{
            "water":200,
            "milk":150,
            "coffee":25
        },
        "cost":2.5
        },
    "espersso":{
        "contents":{
            "water":50,
            "coffee":18
        },
        "cost":1.5
        },
    "cappuccino":{
        "contents":{
            "water":250,
            "milk":100,
            "coffee":24
        },
        "cost":3.0
        }
}
def report():
    print(f"the current values on machine:\nwater:{resource['water']}ml\nmilk:{resource['milk']}ml\ncoffee:{resource['coffee']}g\nMoney:${resource['money']}")

def making(drink,total):
    
    if drink=="latte": 
        report()
        resource["coffee"]-=menu["latte"]["contents"]["coffee"]
        resource["water"]-=menu["latte"]["contents"]["water"]
        resource["milk"]-=menu["latte"]["contents"]["milk"]
        resource["money"]+=round(total-menu['latte']["cost"],2)
        print("---------------------------------")
        report()
        
    elif drink=="espersso":
        report()
        resource["coffee"]-=menu["espersso"]["contents"]["coffee"]
        resource["water"]-=menu["espersso"]["contents"]["water"]
        resource["money"]+=round(total-menu['espersso']["cost"],2)
        print("---------------------------------")
        report()
        
    else:
        report(),
        resource["coffee"]-=menu["cappuccino"]["contents"]["coffee"]
        resource["water"]-=menu["cappuccino"]["contents"]["water"]
        resource["milk"]-=menu["cappuccino"]["contents"]["milk"]
        resource["money"]+=round(total-menu['cappuccino']["cost"],2)
        print("---------------------------------")
        report()
    print(f"Here is {total-menu[drink]["cost"]:.2f} dollars in change")    
   
    print(f"enjoy your {drink}")
      

def take_money(drink):
    quarters=0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01
    try:
        numbers_of_quarters=int(input("how many quarters($0.25): "))
        numbers_of_dimes=int(input("how many dimes($0.10):  "))
        numbers_of_pennies=int(input("how many pennies($0.01):  "))
        numbers_of_nickles=int(input("how many nickles($0.05):  "))
    except ValueError:
        print("try agian")
        return
    total=quarters*numbers_of_quarters+dimes*numbers_of_dimes+pennies*numbers_of_pennies+nickles*numbers_of_nickles
    print("total:",total)
 
    if total<menu[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded")
        return 
    
    else:
        making(drink,total)
           

        


def check_resource(drink):
    if drink=="latte":
        if  menu["latte"]["contents"]["water"]>=resource["water"] :
            return "water"
        elif menu["latte"]["contents"]["milk"]>=resource["milk"]:
            return "milk"
        elif menu["latte"]["contents"]["coffee"]>=resource["coffee"]:
            return "coffee"
        else:
            return True
       
        
    elif drink=="espersso":
        if menu["espersso"]["contents"]["water"]>=resource["water"]:
            return "water"   
        elif  menu["espersso"]["contents"]["coffee"]>=resource["coffee"]:
            return "coffee"
        else:
            return True
    elif drink=="cappuccino":
        if  menu["cappuccino"]["contents"]["water"]>=resource["water"] :
            return "water"
        elif  menu["cappuccino"]["contents"]["milk"]>=resource["milk"]:
            return "milk"
        elif  menu["cappuccino"]["contents"]["coffee"]>=resource["coffee"]:
            return "coffee"
        else:
            return True
    else:
        return -1   
    
def add():
     while 1:
        loot=input("enter which resoure do you want add water/coffee/milk/(enter 'n' for exit)")
        if loot=="water" or loot=="milk" or loot=="coffee":
            try:
                weight=int(input("how much do you want add "))
                resource[loot]+=weight
                report()             
            except ValueError:
                print(" invalid inpute ,,enter agian")
        elif loot=='n':
            print("exiting from adding section")
            break
        else:
            print ("inavlid input")  
        

        

    


def order(user):
    if user=="report":
        report()
        return
    elif user=="add":
        add()   
        return
    test=check_resource(user)
    if test==-1:
        print("invalid order")
        return False
    elif test=="water" or test=="coffee" or test=="milk":
        print(f"Sorry there is not enough {test}")
        return        
    elif test:
        take_money(user)
    else:
        print(f"sorry there is not enough {test}")
            


    

def coffee_machine():
    while 1:
        user=input("what do you want to order(latte/espersso/cappuccino)")
        if user=="off":
            print("shuting down coffee machine")
            break
        else:
            order(user)


            
coffee_machine()