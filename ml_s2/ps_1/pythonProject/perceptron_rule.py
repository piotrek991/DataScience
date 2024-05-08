import numpy as np
import time
import matplotlib.pyplot as plt

x_points = np.arange(-10,10).reshape(20,1)

######### first exercise ############

weights = np.array([0.8,-0.2])
dest = np.array([1,1,-1])

points = np.array([
    [1,-1],
    [1,1],
    [1,2],
])
try:
    assert weights.shape[0] == points.shape[1]
    assert dest.shape[0] == points.shape[0]
except AssertionError:
    print('one of the conditions to use programs not met')

target_met = False
while not target_met:
    target_met = True
    iter_num = -1
    for point in points:
        iter_num += 1
        bipolar_r = 1 if sum(point*weights) > 0 else -1
        if bipolar_r == dest[iter_num]:
            print(f'result as expected')
            continue
        else:
            target_met = False
            if bipolar_r > dest[iter_num]:
                weights = weights - point
            else:
                weights = weights + point
            print(f'weights adjusted: {weights}')
            break
print(f'final weights : {weights}')

f1 = plt.figure(1)
y_calc = np.apply_along_axis(lambda x: (-weights[0]*x[0]) / weights[1], 1, x_points)
plt.plot(x_points, y_calc)
plt.scatter([point[0] for point in points]
               ,[point[1] for point in points]
               , marker = '*'
               , c='red')
plt.title('perceptron')
######### second exercise ############

or_T = 1
and_T = 1
points_OR_AND = np.array([
    [1,1]
    ,[1,0]
    ,[0,0]
])

for point in points_OR_AND:
    # OR
    if sum(point) >= or_T:
        result_OR = 1
    else:
        result_OR = 0
    # AND
    point_NOT = list(map(lambda x: 1 if x == 0 else 0, point))
    if sum(point_NOT) >= and_T:
        result_AND = 0
    else:
        result_AND = 1

f2 = plt.figure(2)
y_calc = np.apply_along_axis(lambda x: (-1*x[0]), 1, x_points)
plt.plot(x_points, y_calc)
plt.scatter([point[0] for point in points_OR_AND]
               ,[point[1] for point in points_OR_AND]
               , marker = '*'
               , c='red')
plt.title('or calc')
f3 = plt.figure(3)
y_calc = np.apply_along_axis(lambda x: (-1*x[0]), 1, x_points)
plt.scatter([point[0] for point in points_OR_AND]
               ,[point[1] for point in points_OR_AND]
               , marker = '*'
               , c='red')
plt.plot(x_points, y_calc)
plt.title('and calc')
######### third exercise ############
weights_per = np.random.rand(2)
dest_OR_AND = np.array([
    [1,1]
    ,[1,0]
    ,[0,0]
])
points_OR_AND_perceptron = np.array([
    [1,1]
    ,[1,0]
    ,[0,0]
])

target_met = False
while not target_met:
    target_met = True
    iter_num = -1
    for point in points_OR_AND_perceptron:
        iter_num += 1

        result_OR = 1 if sum(point * weights_per) >= 1 else 0

        if result_OR == dest_OR_AND[iter_num][0]:
            print(f'result as expected in OR')
            continue
        else:
            target_met = False
            if result_OR >= dest_OR_AND[iter_num][0]:
                weights_per = weights_per - point
            else:
                weights_per = weights_per + point
            print(f'weights adjusted in OR: {weights_per}')
            break
print(f'final weights in OR : {weights_per}')
f4 = plt.figure(4)
y_calc = np.apply_along_axis(lambda x: (-weights_per[0]*x[0]) / weights_per[1], 1, x_points)
plt.plot(x_points, y_calc)
plt.scatter([point[0] for point in points_OR_AND_perceptron]
               ,[point[1] for point in points_OR_AND_perceptron]
               , marker = '*'
               , c='red')
plt.title('or perceptron')

weights_per = np.random.rand(2) + 1

target_met = False
while not target_met:
    target_met = True
    iter_num = -1
    for point in points_OR_AND_perceptron:
        iter_num += 1

        point_NOT = list(map(lambda x: 1 if x == 0 else 0, point))
        result_AND = 0 if sum(point_NOT * weights_per) >= 1 else 1

        if result_AND == dest_OR_AND[iter_num][1]:
            print(f'result as expected in AND')
            continue
        else:
            target_met = False
            if result_AND >= dest_OR_AND[iter_num][1]:
                weights_per = weights_per + point
            else:
                weights_per = weights_per - point
            print(f'weights adjusted in AND: {weights_per}')
            time.sleep(3)
            break
print(f'final weights in AND : {weights_per}')

f5 = plt.figure(5)
y_calc = np.apply_along_axis(lambda x: (weights_per[0]*x[0]) / weights_per[1], 1, x_points)
plt.plot(x_points, y_calc)
plt.scatter([point[0] for point in points_OR_AND_perceptron]
               ,[point[1] for point in points_OR_AND_perceptron]
               , marker = '*'
               , c='red')
plt.title('and perceptron')


plt.show()
