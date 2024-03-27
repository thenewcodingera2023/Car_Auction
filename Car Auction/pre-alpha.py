
import random
import time

#Variables and data
Car_Brand = ["Porsche", "Mercedes", "Triumph", "Peugeot", "Honda", "Mini", "Jaguar", "Aston", "BMW", "Ford"] 
reserve_price = []
for i in range(1,11):
    price = random.randint(1000,5000)
    reserve_price.append(price)
bid_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
sold = [False, False, False, False, False, False, False, False, False, False]
bid_competition = []
for i in range(1,11):
    bid_ai = random.randint(5001,9000)
    bid_competition.append(bid_ai)
print(bid_competition)
Total_Purchase = []
user_id = random.randint(1000,9999)
topay = 0



#Class N Functions

def bid():
#need to add bid competition function
    car_id = int(input("Input CAR ID:"))
    amount = int(input("How Much Money Do you want to Bid on this Car?"))
    car_id-=1

    
    if amount > (reserve_price[car_id] or bid_data[car_id] or bid_competition[car_id] or 0) and sold[car_id] == False:
        print("Bid Successful!")
        print(f"The Greatest Bid for {Car_Brand[car_id]} (previously ${bid_competition[car_id]}) is now ${amount}! ")
        bid_data[car_id] = amount
        bid_competition[car_id] = amount
    else:
        print("Bid Failed.")

def view_bid():
    print("Current Bids By You: ")
    for i in range(0,10):
        print(Car_Brand[i],": ",bid_data[i])
    print("\nCurrent Bids By Everyone: ")
    for i in range(0,10):
        print(Car_Brand[i],": ",bid_competition[i])

def purchase():
    global topay
    car_id = int(input("Car ID: "))
    car_id-=1
    if bid_data[car_id] == 0 or sold[car_id] == True:
        print("Car Not Bidded. Please Bid first.")
    else:
        sold[car_id] = True
        Total_Purchase.append(Car_Brand[car_id])
        topay+=bid_data[car_id]
        print(f"{Car_Brand[car_id]} purchased for ${bid_data[car_id]} ")
        print(f"Outgoing Transactions: ${topay}")
        return topay



def view_all_purchase():
    print(f"Cars Sold: {Total_Purchase}")
    print(f"Total Outgoing transactions: ${topay}")



def add_user(name):
    print(f"Welcome, {name}! Your user ID is {user_id}.")
    return name


def view_car():
    car_id = int(input("Car ID: "))
    car_id-=1
    print(f"Item name: {Car_Brand[car_id]}")
    print(f"Reserve Price: ${reserve_price[car_id]}")
    print(f"Sold? {sold[car_id]}")
    print(f"Current Bid: ${bid_competition[car_id]}")
    print(f"Current Bid By You: ${bid_data[car_id]}")






#Testing Zone!
#print("Welcome to the Car Auction")
#name = input("Please Input Your Name: ")
#add_user(name)
#print("-----------------------")
#time.sleep(3)
#print(f"Reserve Price of cars [IN USD]:")
#for i in range(0,10):
#    print(Car_Brand[i],": ",reserve_price[i])

#bid(1,10000)
#view_bid()


#Execution













name = input("Please enter your username: ")
print("----------------------")
print("Hello there, ",name,", Your ID is: ",user_id)
print("----------------------")
print("Here are the cars available for auction: ", Car_Brand)
print("----------------------")
time.sleep(2)
while True:
    ask = input("To bid, press B. To view car info Press V. To view Current Bid Press F. To Buy press P \n")
    if ask == "B":
        bid()
    elif ask == "V":
        view_car()
    elif ask == "F":
        view_bid()
    elif ask == "P":
        purchase()