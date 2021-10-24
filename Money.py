print('Amount of Your Money:')
Amount = int(input())
print('Price of an Apple:')
Price = int(input())
Quantity = Amount//Price
Change = Amount-Quantity*Price
print(f"You can buy {Quantity} apples and your change is {Change} pesos.")