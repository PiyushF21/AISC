import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(precision=2,suppress=True)
rooms=np.array(["room1","room2","room3"])
A = np.array([0.8, 0.5, 0.2])  # Hot Temperature
B = np.array([0.7, 0.5, 0.3])

temperature = np.array([0.8, 0.5, 0.2])
humidity = np.array([0.7, 0.5, 0.3])
cooling = np.array([0.2, 0.5, 0.9])

temperature_names = np.array(["cold","comfortabke","hot"])
humidity_names = np.array(["Low","Moderate","High"])
cooling_names = np.array(["Low","Medium","High"])

union = np.maximum(A,B)
intersection = np.minimum(A,B)
algrbraic_sum = A+B-A*B
algrebraic_product = A*B
bounded_sum = np.minimum(A+B,1)
bounded_difference = np.maximum(A-B,0)

cartesian_product = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        cartesian_product[i][j]= np.maximum(temperature[i],humidity[j])

S = np.array([
    [0.2, 0.4, 0.8],
    [0.3, 0.6, 0.8],
    [0.7, 0.8, 0.9]
])
max_min = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        maximum = 0
        for k in range(3):
            value = min(cartesian_product[i][k],S[j][k])
            if value>maximum:
                maximum=value
        max_min = maximum

max_product = np.zeros((3, 3))

for i in range(3):
    for k in range(3):
        maximum = 0

        for j in range(3):
            value = cartesian_product[i][j] * S[j][k]

            if value > maximum:
                maximum = value

        max_product[i][k] = maximum

plt.figure(figsize=(7,4))
plt.plot(temperature_names,temperature,marker='o',label='temperature')
plt.plot(humidity_names,humidity,marker='s',label='humdity')
plt.plot(cooling_names,cooling,marker='^',label='cooling')
plt.ylabel('Membership values')
plt.ylim(0,1)
plt.legend()
plt.grid()
plt.show()


plt.subplot(1, 2, 1)
plt.imshow(max_min, cmap="YlGnBu", vmin=0, vmax=1)
plt.title("Max-Min Composition")
plt.xticks(range(3), cooling_names)
plt.yticks(range(3), temperature_names)
plt.colorbar()

plt.subplot(1, 2, 2)
plt.imshow(max_product, cmap="YlGnBu", vmin=0, vmax=1)
plt.title("Max-Product Composition")
plt.xticks(range(3), cooling_names)
plt.yticks(range(3), temperature_names)
plt.colorbar()

plt.tight_layout()
plt.show()
