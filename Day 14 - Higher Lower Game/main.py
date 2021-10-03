# import game art and gameplay data from modules
import art
import game_data
import random

#initial game setup
#objectList = random.randint(0,len(game_data.data))
objectA = game_data.data[random.randint(0,len(game_data.data))]
objectB = game_data.data[random.randint(0,len(game_data.data))]
objectList = []
objectList.append(objectA['name'])
objectList.append(objectB['name'])
print(objectList)

print(objectA)
print(objectB)
print(art.logo)
print(f"Compare A: {objectA['name']}, a {objectA['description']}, from {objectA['country']}")
print(art.vs)
print(f"Against B: {objectB['name']}, a {objectB['description']}, from {objectB['country']}")
userChoice = input("\nWho has more followers? Type 'A' or 'B': ")


print(userChoice)

objects = game_data.data
print(game_data.data[0])