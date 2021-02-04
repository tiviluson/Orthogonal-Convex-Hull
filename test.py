import csv
import matplotlib.pyplot as plt
import random
import convexOQHNew
#from test_mainoquickhull import *
from pathlib import Path

# input_points = []
# dataset = []

# with open("3000.csv") as f:
# with open("50.csv") as f:
#     csv_reader = csv.reader(f, delimiter=",")
#     for row in csv_reader:
#         input_points = input_points + [[float(row[0]), float(row[1])]]

def file_generator(number_of_files=20):
    #number_of_files = int(input("Enter number of files: "))
    data_folder = Path("Input/")
    for i in range(number_of_files):
        file_name = data_folder / (str(i) + ".csv")
        number_of_points = random.randint(80, 100)
        with open(file_name, mode="w") as file:
            for i in range(number_of_points):
                point = (random.uniform(0, 100), random.uniform(0, 100))
                file.write(str(point[0]) + ", " + str(point[1]) + "\n")
            #print("Finish")
            file.close()

def points_supplement(points):
    S = []
    for i in range(0, len(points) - 1):
        if points[i+1][0] > points[i][0] and points[i+1][1] > points[i][1]:
            p3 = [points[i][0], points[i+1][1]]
            S.append([i+1, p3])
        elif points[i+1][0] > points[i][0] and points[i+1][1] < points[i][1]:
            p3 = [points[i+1][0], points[i][1]]
            S.append([i+1, p3])
        elif points[i+1][0] < points[i][0] and points[i+1][1] < points[i][1]:
            p3 = [points[i][0], points[i+1][1]]
            S.append([i+1, p3])
        elif points[i+1][0] < points[i][0] and points[i+1][1] > points[i][1]:
            p3 = [points[i+1][0], points[i][1]]
            S.append([i+1, p3])
    return S

def graph(processed_points, input_points):
    fig, ax = plt.subplots()

    # Input points in blue
    ax.plot([x[0] for x in input_points], [x[1] for x in input_points], 'r.')

    # Orthogonal convex hull points in red
    ax.plot([x[0] for x in processed_points], [x[1] for x in processed_points], 'b-')

    plt.ylabel('Y')
    plt.xlabel('X')
    return plt

def orthogonalize(number_of_files=20):
    input_folder = Path("Input/")
    output_folder = Path("Output/")
    for i in range(number_of_files):
        input_file_name = input_folder / (str(i) + ".csv")
        output_file_name = output_folder / (str(i) + ".csv")
        output_graph_name = output_folder / (str(i) + ".png")
        input_points = []
        with open(input_file_name, "r") as input_file:
            csv_reader = csv.reader(input_file, delimiter=",")
            for row in csv_reader:
                #input_points.append[[float(row[0]), float(row[1])]]
                input_points.append([float(row[0]), float(row[1])])
            input_file.close()

        processed_points = convexOQHNew.findOrthogonalConvexHull(input_points)
        processed_points.append(processed_points[0])
        S = points_supplement(processed_points)
        for i in range(len(S)):
            processed_points.insert(S[i][0]+i, S[i][1])
        #processed_points.append(processed_points[0])

        with open(output_file_name, "w") as output_file:
            for point in processed_points:
                output_file.write(str(point[0]) + ", " + str(point[1]) + "\n")
            output_file.close()

        plt = graph(processed_points, input_points)
        plt.savefig(output_graph_name)
        plt.close()

number_of_files = int(input("Enter number of files: "))
file_generator(number_of_files)
orthogonalize(number_of_files)
