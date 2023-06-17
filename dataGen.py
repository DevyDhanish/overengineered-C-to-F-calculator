import random

x_train = []
y_train = []

iteration = int(input("Iteration :- "))

for i in range(iteration):
    C = random.randrange(0, 100)
    x_train.append([C])
    F = (C * 9/5) + 32
    y_train.append(F)

print(x_train)
print(y_train)
