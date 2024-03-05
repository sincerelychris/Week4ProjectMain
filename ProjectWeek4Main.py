#if you walk in workers and get name:
name = input("Hi, Welcome to the 5 Star Breakfast! Whats your name.")

#Apply name: (*)
print("Hi "+name+ ". It is very nice to meet you. Hopefully you are having a wonderful friday so far.")

#Deal (new)
print("Every friday we have a special. Everything is $8 today!")

#How many (new)
PeopleCount = input("How many people will be dining with you?")
PeopleCount = int(PeopleCount)

print("Great!")

menu = "Pancakes, Cheese Toast, Waffles"

#List Menu (new)
print(name + ", What would you like to order? Here is our menu today: \n"+menu+"?")
order = input()

#It takes 2 minutes to prepare each item(new)
#Reason for str is because print statements only read one type(ex. only strings ore only integers)
TotalTime = str(PeopleCount*2)
print("Great Choice "+name+". Your " +order+ " will be finished in "+ TotalTime +" minutes")

