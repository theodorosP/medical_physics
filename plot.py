import matplotlib.pyplot as plt
from medical_library import *

file = "3saSingles_Tc.dat"

data = read(file)
dataset = data.get_dataset()
print(dataset)
#data.print_whole_dataset()
columns = data.get_columns()
print("The columns of the datese are: ", columns)

plt.hist(dataset[columns[10]], bins = 100, edgecolor= "black", label = "Energy")
plt.ylabel("Frequency")
plt.xlabel("Energy")
plt.title("Energy Histogram")
plt.savefig("Energy_histogram.png")
plt.show()

plt.hist(dataset[columns[11]], bins = 100, edgecolor= "black", label = "X")
plt.ylabel("Frequency")
plt.xlabel("Energy")
plt.title("X Direction Incident Histogram")
plt.savefig("X_histogram.png")
plt.show()


plt.hist(dataset[columns[12]], bins = 100, edgecolor= "black", label = "X")
plt.ylabel("Frequency")
plt.xlabel("Energy")
plt.title("Y Direction Incident Histogram")
plt.savefig("Y_histogram.png")
plt.show()

plt.hist(dataset[columns[13]], bins = 100, edgecolor= "black", label = "Z")
plt.ylabel("Frequency")
plt.xlabel("Energy")
plt.title("Z Direction Incident Histogram")
plt.savefig("Z_histogram.png")
plt.show()

plt.scatter(dataset[columns[11]], dataset[columns[12]], s = 2, label = "X - Y")
plt.ylabel("Y")
plt.xlabel("X")
plt.title("X vs Y")
plt.gca().set_aspect('equal')
plt.savefig("X_Y.png")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset[columns[11]], dataset[columns[12]], dataset[columns[13]], s = 2, c='b', marker='o')
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.gca().set_aspect('equal')
plt.savefig("X_Y_Z.png")
plt.show()
