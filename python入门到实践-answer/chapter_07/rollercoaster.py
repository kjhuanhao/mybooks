height = input("How tall are you, in inches? ")
height = int(height)#input输入的是字符串，需要用int转化为数值

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
