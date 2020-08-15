#nested if-if inside a if

x = int(input('enter number u wanna check '))
r = x % 2

if r == 0:
    print("Even")
    if x > 5:
        print("Great")
    else:
        print("Not so great")

else:
    print("Odd")

print("end of prgrm")