#lists challenge 7 groceryy list
import datetime

#create the datetime object and store the current date and time.
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("\nWelcome to the grocery list program")
foods = ["Meat", "Cheese"]
print("Current date and time: " + month + "/" + day + "/" + "\t" + hour + ":" + minute)
print("You currently have " + foods[0] +  " and " + foods[1] + " in your list.")

#user input
food = input("\nType of food to add in the grocery list: ")
foods.append(food.title())
food = input("Type of food to add in the grocery list: ")
foods.append(food.title())
food = input("Type of food to add in the grocery list: ")
foods.append(food.title())
print("\nHere is your grocery list:")
print(foods)

#print and Permanently sort the list
sorted_list = foods.sort()
print("Here is your grocery list sorted:")
print(foods)

#simulate grocery list
print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items ")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing" + buy_food + "from the list...")

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items ")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing" + buy_food + "from the list...")

print("\nSimulating grocery shopping...")
print("\nCurrent grocery list: " + str(len(foods)) + " items ")
print(foods)
buy_food = input("What food did you just buy: ").title()
foods.remove(buy_food)
print("Removing" + buy_food + "from the list...")

#The store is out of an item
print("\nCurrent grocery list " + str(len(foods)) + "items")
