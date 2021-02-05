def personal_details():
    name, age = "Sreeja", 15
    address = "Thornhill, Ontario, Canada"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()

person = input ("Enter your name:")
print ("Hello",person)

print ("Enter a length")
length = float(input())

print (type(length))
print ("Enter a width")
width = float(input())
area = length * width 
print (f"The area is {area} units squared.")

small_container = int(input("Enter the number of small containers you recycled?"))

large_container = int(input("Enter the number of large containers you recycled?"))

refund = (small_container * 0.10) + (large_container * 0.25)

print("The total refund for returning the containers is $" + "{0:.2f}".format(float(refund)))
