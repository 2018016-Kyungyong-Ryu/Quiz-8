import random
number = []
for i in range(6):
    number.append(random.randint(1, 45))
    number.sort()
print(number)

def gen(number):
    for i in range(6):
        for j in range(i+1, 6):
            if number[i] == number[j]:
                return True
            else:
                return False

if gen(number) == True:
    print("중복이 있습니다.")

else:
    print("중복이 없습니다.")
