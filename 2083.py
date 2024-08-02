while True :
    name, age, height = input().split()
    age, height = int(age), int(height)
    if name == "#" and age == 0 and height == 0:
        break
    elif age > 17 or height >= 80 :
        print(name, "Senior")
    else :
        print(name, "Junior")