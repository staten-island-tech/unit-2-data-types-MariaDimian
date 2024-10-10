num_1 = int(input("give me a number"))
num_2 = int(input("give me  another number"))
gcf = 1

for i in range(1, min(num_1, num_2)):
    if num_1 % i == 0 and num_2 % i == 0:
        gcf = i
print(f"{gcf}")