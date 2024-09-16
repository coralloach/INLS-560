sales = 60000
bonus = 500
if sales > 50000:
    print(f"whoo-hoo!")


prompt = "what is today's temp?"
degrees_f = int(input(prompt))

# int(input()) will be on the midterm, casting a number

if degrees_f < 60:
    print("wear a jacket")

is_cold = degrees_f < 60


num = "pick a number between 1 and 10"
var_1 = int(input(num))
if var_1 > 8:
    var_2 = 'Y'
else:
    var_2 = 'N'
print (var_2)