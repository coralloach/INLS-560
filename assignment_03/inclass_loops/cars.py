
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# You can print a section of a string by giving a range of character positions
cars2 = "audi, bmw, subaru, toyota"
print(f"{cars2[0:4]}")


dinosaurs = ['alamosaurus', 'saltasaurus', 'alvarezsaurus', 'pinacosaurus']

for dinosaur in dinosaurs:
    if dinosaur == "pinacosaurus":
        print(dinosaur.upper())
        print('is a very cool dinosaur')
    else:
        print(dinosaur.upper())
        print('is a very silly name for a dinosaur')
# Didn't figure out if I could print message on the same line as the item.