import random
customers = random.randint(10,50)

print(customers)

weather = ["Sunny", "Hot and Dry", "Cloudy"]
weather_multiplier = [1.1,2.2,0.2]

weather_type = random.randint(0,2)
print(weather_type)

weather= weather[weather_type]   # get the weather from the list with that index
multiplier = weather_multiplier[weather_type] # get the weather from the list with that index



customers *= multiplier

print(customers)

#diplay instructions

# ask if they want to play again
# while(not gameover):
    # play 1 day of the game
    # then ask if they want to play again
    # if no gameover = True