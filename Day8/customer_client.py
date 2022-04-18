from customer_entity import Customers
import customer_service as s

print("welcome!!")
loop_check = 'yes'
while loop_check == 'yes':
    customerId = input("Enter customer id:")
    name = input("Enter the name:")
    age = int(input("Enter your age:"))
    gender = input("enter your gender:")
    customer = Customers(customerId, name, age, gender)

    items = []
    kilograms = []
    print("available items:")
    print("item\tprice\tquantity")
    for i in range(len(s.groceries)):
        print(f'{s.groceries[i]}\t{s.price[i]}\t\t{s.quantity[i]}')
    loop_var = "yes"
    while loop_var == "yes":
        item = input("enter the item to purchase:")
        items.append(item)
        kg = int(input("enter the quantity:"))
        kilograms.append(kg)
        loop_var = input("Do you want to add another item?(yes/no)")
    bill = s.bill_calculation(items, kilograms)
    print(f"total price : {bill}/-")
    loop_check = input("do you want to add another customer?(yes/no)")
