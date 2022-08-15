MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def bill():
    print("Please insert coins.")
    quarters_paid = int(input("how many quarters?: "))*0.25
    dimes_paid = int(input("how many dimes?: "))*0.10
    nickles_paid = int(input("how many nickles?: "))*0.05
    pennies_paid = int(input("how many pennies?: "))*0.01
    total_amount = quarters_paid+ dimes_paid + nickles_paid  + pennies_paid 
    return total_amount 

def check_ingredients(choice):
    if choice != "espresso":
        if not resources["water"] >= MENU[choice]["ingredients"]["water"]:
            return "Sorry there is not enough water."
        elif not resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
            return "Sorry there is not enough milk."
        elif not resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
            return "Sorry there is not enough coffee powder."
        else:
            return True
    else:
        if not resources["water"] >= MENU[choice]["ingredients"]["water"]:
            return "Sorry there is not enough water."
        elif not resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
            return "Sorry there is not enough coffee powder."
        else:
            return True




def ingredients_left(choice,resouces):
    if choice != "espresso":
        resources["water"] -= MENU[choice.lower()]["ingredients"]["water"]
        resources["milk"]  -= MENU[choice.lower()]["ingredients"]["milk"]
        resources["coffee"]  -= MENU[choice.lower()]["ingredients"]["coffee"]
    else:
        resources["water"] -= MENU[choice.lower()]["ingredients"]["water"]
        resources["coffee"]  -= MENU[choice.lower()]["ingredients"]["coffee"]
        
           
    


def make_coffee():
    money = 0
    choice = input("What would you like? (Espresso/ Latte/ Capuccino): ").lower()
    while choice != "off":
        
        if choice == "latte":
            if check_ingredients(choice) == True:
                x = bill()
                if x >= MENU["latte"]["cost"] :
                    balance =  x - MENU["latte"]["cost"]
                    money += MENU["latte"]["cost"]
                    print(f"Here is ${balance} in change. ")
                    print(f"Here is your {choice} ☕. Enjoy!")
                    ingredients_left(choice,resources)
                   
                   
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(check_ingredients(choice))
        elif choice == "espresso":
            if check_ingredients(choice) == True:
                x=bill()
                if x >= MENU["espresso"]["cost"] :
                    balance = x - MENU["espresso"]["cost"]
                    money += MENU["espresso"]["cost"]
                    print(f"Here is ${balance} in change. ")
                    print(f"Here is your {choice} ☕. Enjoy!")
                    ingredients_left(choice,resources)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(check_ingredients(choice))
    
        elif choice == "cappuccino":
            if check_ingredients(choice) == True:
                x=bill()
                if x >= MENU["cappuccino"]["cost"] :
                    balance = x - MENU["cappuccino"]["cost"]
                    money += MENU["cappuccino"]["cost"]
                    print(f"Here is ${balance} in change. ")
                    print(f"Here is your {choice} ☕. Enjoy!")
                    ingredients_left(choice,resources)
                    
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(check_ingredients(choice))
        
        elif choice == "report":
            for i in resources:
                print(i,":" , resources[i])
            print("Money: $",money)
                
        choice = input("What would you like? (Espresso/ Latte/ Capuccino): ").lower()
        
    


make_coffee()







