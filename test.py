import csv
import matplotlib.pyplot as plt

input_points = []
dataset = []

#with open("3000.csv") as f:
with open("50.csv") as f:
    csv_reader = csv.reader(f, delimiter=",")
    for row in csv_reader:
        input_points = input_points + [[float(row[0]), float(row[1])]]

# Draw lines
fig, ax = plt.subplots()

# Input points in blue
ax.plot([x[0] for x in input_points], [x[1] for x in input_points], 'r-')

# Orthogonal convex hull points in red
#ax.plot([x[0] for x in points], [x[1] for x in points], 'b-')
#ax.plot([list(points[0])[0], list(points[-1])[0]], [list(points[0])[1], list(points[-1])[1]],'r-')

plt.ylabel('Y')
plt.xlabel('X')
plt.show()
