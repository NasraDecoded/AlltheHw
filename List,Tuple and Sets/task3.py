numbers = []
good = []

x = 1
while x <=100:
    numbers.append(x)
    x += 1

y = 0

while y < len(numbers):
    num = numbers[y]

    if num % 7 == 0 and num % 5 != 0:
        good.append(num)

    y += 1
    print(good)