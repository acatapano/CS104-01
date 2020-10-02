temp = 0

temp = int(input("Please enter current temperature: "))

if temp > 90:
    print("Wear Shorts")
elif 90 >= temp > 70:
    print("Short Sleeves are Fine")
elif 70 >= temp > 50:
    print("Wear a Jacket")
elif 50 >= temp > 32:
    print("Wear a Heavy Coat")
else:
    print("Stay Inside")
