'''28.	Take the price of a product and quantity as input. Calculate the total bill. 
Example:
Price = 250.50
Quantity = 4

Total = 1002.0'''


price = float(input("Enter  price of given product : "))
quantity = int(input("Enter quantity of given product : "))


bill = price * quantity


print(f"Product price : {price} , Product quantity :  {quantity}")
print("Total bill of the product is : ",bill)
