#Vending machine.


#Price and Items


#Snacks


#Lays = 3
#Biscuits = 5
#Skyflakes = 2
#Cookies = 3
#Sandwich = 7



#Hot Beverages


#Latte = 2
#Cappuccino = 3
#Chai = 2



#Cold Beverages


#Lemon Ice Tea = 8      
#Peach Ice Tea = 8
#Banana Milk= 5
#Coke  = 3
#Sprite = 3
#Orange Juice = 5



#This part shows the user the different variaty of Goods, Price , Change , and Code for the Machine, this is what a user will see if using vending machine


print ("""Hello! Below are the different options for goods.
To confirm order, Type in Code.""")



vending_machine_stock = """
Snacks:
Name:                Price:                    Code:
Lays---------------3DHS----------------------s1
Biscuits-------------5DHS----------------------s2
Skyflakes------2DHS----------------------s3
Cookies--------------3DHS----------------------s4
Sandwich--------------7DHS----------------------s5

Hot Beverages:
Name:                Price:                    Code:
Latte----------------2DHS----------------------h1
Cappuccino-------------3DHS----------------------h2
Chai-------------2DHS----------------------h3

Cold Beverages:
Name:                Price:                    Code:
Lemon Ice Tea---------8DH-----------------------c1
Peach Ice Tea--------------8DHS----------------------c2
Banana Milk-----------5DHS----------------------c3
Coke-------3DHS----------------------c4
Sprite------------------3DHS----------------------c5
Orange Juice----5DHS----------------------c6
"""
print(vending_machine_stock)


#User Interface(Part where the user will interact with the machine)


money = (int(input("Insert Cash or Coins (minimum of 2DHS) ")))
print("==Machine Processing==")
print("==Loading==")
if money > 1:
   print("You have Entered", money, "DHS")
else:
   print("Amount Defeicent.")
   money = (int(input("Insert Cash or Coins (minimum of 2DHS) ")))
   print("==Machine Processing==")
   print("==Loading==")
   print("You have Entered", money, "DHS")

answer = (input("""Proceed?(type in "yes" or "no") """))
if answer == "yes":
  product_code = (input("Enter the Code : "))

elif answer == "no":
  print("""==Processing Demand==
Refunding amount of""", money, """DHS
 Have a nice day, Thank You.""")
  

#Price



#Snacks


Lays = 3
Biscuits = 5
Skyflakes = 2
Cookies = 3
Sandwich = 7
#Hot Beverages

Latte = 2
Cappuccino = 1
Chai = 2
#Cold Beverages

Lemon_Ice_Tea = 8 
Peach_Ice_Tea = 8
Banana_Milk = 5
Coke = 3
Sprite = 3
Orange_Juice = 5




#This is where is whole interface proccess any demand/s from the user









#Snacks


def s1():
  if money >= Lays:
     money_to_return = money - Lays
     print("""Order now being Processed,
     Please wait
     Dropping Lays
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")


def s2():
  if money >= Biscuits:
     money_to_return = money - Biscuits
     print("""Order now being Processed,
     Please wait
     Dropping Biscuits
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")


def s3():
  if money >= Skyflakes:
     money_to_return = money - Skyflakes
     print("""Order now being Processed,
     Please wait
     Dropping Skyflakes
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")


def s4():
  if money >= Cookies:
     money_to_return = money - Cookies
     print("""Order now being Processed
     Please wait
     Dropping Cookies
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")


def s5():
  if money >= Sandwich:
     money_to_return = money - Sandwich
     print("""Order now being Processed,
     Please wait
     Dropping Sandwich
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificeint to the Request.")










#Hot Beverages


def h1():
  if money >= Latte:
     money_to_return = money - Latte
     print("""Order now being Processed,
     Please wait
     Dropping Latte
     You have a change of""", money_to_return, """DHS"
     Thank you!""")
  
  else:
     print("The amount you have Entered is Dificient to the Request.")


def h2():
  if money >= Cappuccino:
     money_to_return = money - Cappuccino
     print("""Order now being Processed,
     Please wait
     Droppin Cappucciono
     You have a change of""", money_to_return, """DHS"
     Thank you!""")
  
  else:
     print("The amount you have Entered is Dificient to the Request.")


def h3():
  if money >= Chai:
     money_to_return = money - Chai
     print("""Order now being Processed,
     Please wait
     Dispensing Chai
     You have a change of""", money_to_return, """DHS"
     Thank you!""")

  
  else:
     print("The amount you have Entered is Dificient to the Request.")

  









#Cold Beverages
 

def c1():
  if money >= Lemon_Ice_Tea:
     money_to_return = money - Lemon_Ice_Tea
     print("""Order now being Processed,
     Please wait
     Dropping Lemon Ice Tea
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")




def c2():
  if money >= Peach_Ice_Tea:
     money_to_return = money - Peach_Ice_Tea
     print("""Order now being Processed
     Please wait
     Dropping Peach Ice Tea
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")




def c3():
  if money >= Banana_Milk:
     money_to_return = money - Banana_Milk
     print("""Order now being Processed
     Please wait
     Dropping Banana Milk
     You have a change of""", money_to_return, """DHS
     Thank you for using this vending machine""")
  else:
     print("The amount you have Entered is Dificient to the Request.")


def c4():
  if money >= Coke:
     money_to_return = money - Coke
     print("""Order now being Processed,
     Please wait
     Dropping Coke
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have entered is Dificient to the Request.")



def c5():
  if money >= Sprite:
     money_to_return = money - Sprite
     print("""Order now being Processed,
     Please wait
     Dropping Sprite
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")




def c6():
  if money >= Orange_Juice:
     money_to_return = money - Orange_Juice
     print("""Order now being Processed
     Please wait
     Dropping Orange Juice
     You have a change of""", money_to_return, """DHS
     Thank you!""")
  else:
     print("The amount you have Entered is Dificient to the Request.")





#snacks


if product_code == "s1":
   s1()
elif product_code == "s2":
   s2()
elif product_code == "s3":
   s3()
elif product_code == "s4":
   s4()
elif product_code == "s5":
   s5()


#hot drinks


elif product_code == "h1":
   h1()
elif product_code == "h2":
   h2()
elif product_code == "h3":
   h3()


#cold drinks


elif product_code == "c1":
   c1()
elif product_code == "c2":
   c2()
elif product_code == "c3":
   c3()
elif product_code == "c4":
   c4()
elif product_code == "c5":
   c5()
elif product_code == "c6":
  c6()
else:
  print("Error! Invalid Code")