import random


print("Welcome to Lemonsville!")
print("You are the owner of a Lemonade stand.")
print("Make the right decisions to make money.")


# Getting the weather
def weather():
    weather = ["Sunny", "Sunny", "Sunny", "Cloudy", "Cloudy", "Hot and dry", "Hot and dry"]
    return random.choice(weather)

# Determining number of customers that will come based on the weather
def customers_based_on_weather(weather,advertisements):
    if weather == "Sunny" and advertisements == 1:
        return random.randint(30,50) + 10
    elif weather == "Sunny" and advertisements == 2:
        return random.randint(30,50) + 20
<<<<<<< HEAD
    elif weather == "Sunny" and advertisements == 3:
        return random.randint(30,50) + 30
    elif weather == "Sunny" and advertisements == 4:
        return random.randint(30,50) + 40
    elif weather == "Sunny" and advertisements >= 3:
        return random.randint(30,50) + 45
=======
    elif weather == "Sunny" and advertisements >= 3:
        return random.randint(30,50) + 30
>>>>>>> aa94fe6fd0e572282f98b77f278aca3e3af8f82e
    elif weather == "Sunny":
        return random.randint(30,50)

    elif weather == "Cloudy" and advertisements == 1:
        return random.randint(0,30) + 10
    elif weather == "Cloudy" and advertisements == 2:
        return random.randint(0,30) + 20
<<<<<<< HEAD
    elif weather == "Cloudy" and advertisements == 3:
        return random.randint(0,30) + 30
    elif weather == "Cloudy" and advertisements == 4:
        return random.randint(0,30) + 40
    elif weather == "Cloudy" and advertisements >= 5:
        return random.randint(0,30) + 45
=======
    elif weather == "Cloudy" and advertisements >= 3:
        return random.randint(0,30) + 30
>>>>>>> aa94fe6fd0e572282f98b77f278aca3e3af8f82e
    elif weather == "Cloudy":
        return random.randint(0,30)
    
    elif weather == "Hot and dry" and advertisements == 1:
        return random.randint(40,90) + 10
    elif weather == "Hot and dry" and advertisements == 2:
        return random.randint(40,90) + 20
<<<<<<< HEAD
    elif weather == "Hot and dry" and advertisements == 3:
        return random.randint(40,90) + 30
    elif weather == "Hot and dry" and advertisements == 4:
        return random.randint(40,90) + 40
    elif weather == "Hot and dry" and advertisements >= 5:
        return random.randint(40,90) + 45
=======
    elif weather == "Hot and dry" and advertisements >= 3:
        return random.randint(40,90) + 30
>>>>>>> aa94fe6fd0e572282f98b77f278aca3e3af8f82e
    else:
        return random.randint(40,90)
    
# Based on the price user inputs return customers who will buy
def sales(price, weather, customers):
    if weather =="Sunny":
        if 0 < price <= 10:
            return customers
        else:
            return 0
    elif weather == "Cloudy":
        if 0 < price <= 6:
            return customers
        else:
            return 0
    else:
        if 0 < price < 15:
            return customers
        else:
            return 0
        
    # Ask the user for how much they want to make how much they advertisments they want to make and the price they want to sell it at
def user_input(assets):
    while True:
        amount = int(input("One glass costs 2 coins to make. What is the amount of glasses you want to make: "))
        advertisements = int(input("One advertisement costs 15 coins. How many advertisements do you want to make: "))
        price = int(input("What price do you want to sell the glasses at: "))

        total_cost = amount * 2 + advertisements * 15
        if total_cost < assets:
            return amount, advertisements, price
        else:
            print(f"The total cost ({total_cost} coins) exceeds your assets. Please enter a valid combination.")

     #Use def sales and customers buying calculate sales made subtracted by input costs.
def calculate_profit(price, advertisements, amount):
    profit = price*amount - (amount*2) - (advertisements*15)
    return profit

# First display the day, assets your currently have and weather.
# Ask the user for their amount, price and advertisements they want to have
# Then calculate the amount of customers that will come based on the amount of advertisements
# Then calculate the profit made after the day.
# If the assets are less than 0 end the game
# if not ask if the user wants to continue

def simulate_day():
    day = 0
    assets = 200
    while assets > 0:
        day += 1
        weather_today = weather()
        print(f"It is day {day}")
        print(f"The weather is {weather_today} today")
        print(f"Your assets are {assets} coins")

        amount, advertisements, price = user_input(assets)
        customers = customers_based_on_weather(weather_today,advertisements)
        customer_buyers = sales(price, weather_today, amount)
        profit = calculate_profit(price, advertisements, customer_buyers)
        assets = assets + profit
        print("=================================")
        print(f"You made {amount} cups today")
        print(f"You sold {customer_buyers} cups for {price} each.")
        print(f"Your profit was {profit}")
        print(f"You have {assets} coins left.")

        continue_game = input("Do you want to go to the next day (yes or no): ")
        if continue_game == "no":
            break

simulate_day()

print("Game over")


        

    


   

    
    

