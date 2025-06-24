target = 10
position = [4,1,0,7]
speed = [2,2,1,1]
cars=[]
stack=[]

for i in range (len(position)):
    cars.append((position[i],speed[i]))
print(cars)

cars.sort()
cars.reverse()
print(cars)

'''now we will calculate time to reach target for each car and add to stack'''

for car in cars:
    time=(target-car[0])/car[1]
    stack.append(time)

print stack()