
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# You can print a section of a string by giving a range of character positions
cars2 = "audi, bmw, subaru, toyota"
print(f"{cars2[0:4]}")


