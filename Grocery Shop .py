a = "Welcome!!!"
b = input("Hello!!! What's your name?")
print(a, b)
c = (input("Do you want to buy something?"))
list=[]
price=[]
if c == ("yes"):
    x=("""
    Welcome to our Shop_Basket
----------------------------------
1. Rice
2. Mustard Oil
3. Soap
4. Toothpaste
5. Detergent
6. Shampoo

""")
    print(x)
    def main():
        item = int(input("Enter the Product number which you want to buy: "))
        if item == 1:
            Rice = {
                'Basmati': 'Rs.100 per_kg',
                'Minikit': 'Rs.90 per_kg',
                'Dawat': 'Rs.85 per_kg',

            }
            print(Rice)

            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity?:"))
        elif item == 2:
            Mustard_oil = {
                'Emami': 'Rs.180',
                'Fortune': 'Rs.185',
                'Dhara': 'Rs.160',
            }
            print(Mustard_oil)
            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity?:"))
        elif item == 3:
            Soap = {
                'Lifebuoy': 'Rs.30',
                'Lux': 'Rs.40',
                'Dettol': 'Rs.35',
                'Wild_Stone': 'Rs.50',
            }
            print(Soap)
            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity?:"))
        elif item == 4:
            Toothpaste = {
                'Colgate': 'Rs.92',
                'Pepsodent': 'Rs.80',
                'Dabur_red': 'Rs.88',
                'Close_up': 'Rs.95',
            }
            print(Toothpaste)
            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity?:"))

        elif item == 5:
            Detergent = {
                'Sunlight': 'Rs.83',
                'Tide': 'Rs.100',
                'Surf_Excel': 'Rs.120',
                'Wheel': 'Rs.45',
            }
            print(Detergent)
            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity?:"))
        elif item == 6:
            Shampoo = {
                'head&shoulders': 'Rs.85',
                'Dove': 'Rs.98',
                'Loreal': 'Rs.95',
                'Sunsilk': 'Rs.55',
            }
            print(Shampoo)
            y=(input("Choose your Product_Brand: "))
            z=(input("Put your quantity!!:"))
        e = eval(input("Please calculate your product price!!: "))     # Calculation = product price * product quantity (pls calculate manually)
        print(e)
        Repeat=input('Do you want to buy something else?')
        list.append(item)
        price.append(e)
        if Repeat=='yes':
            main()

        else:
            print("your final products are:", list)
            print("You have to pay:", price)
            print('THANK YOU VISIT AGAIN!')
            exit()
    main()
else:
    c=="no"
    print("THANK YOU!")