import pandas as pd
from PIL import Image
import numpy as np
import csv
import matplotlib.pyplot as plt
from Convert_png_to_bitmap import *

plt.style.use('seaborn-whitegrid')

def coordinate_check(x, y):
    result = ""
    # 123
    # 4.5
    # 678
    if bit_coordinates[x][y] != "1":
        return False
    else:
        try:
            if bit_coordinates[x-1][y+1] == "1": result = result + "1"
            if bit_coordinates[x][y+1] == "1": result = result + "2"
            if bit_coordinates[x+1][y+1] == "1": result = result + "3"
            if bit_coordinates[x-1][y] == "1": result = result + "4"
            if bit_coordinates[x+1][y] == "1": result = result + "5"
            if bit_coordinates[x-1][y-1] == "1": result = result + "6"
            if bit_coordinates[x][y-1] == "1": result = result + "7"
            if bit_coordinates[x+1][y-1] == "1": result = result + "8"
            if result in ("1245678", "2345678", "1234578", "1234567", "124", "235", "467", "578",
                        "1246", "1467", "1235", "1234", "3578", "2358", "4678", "5678", "2", "4",
                        "5", "7", "14678", "35678", "12346", "12358"):
                return True
            else:
                return False
        except:
            print(x, y)
    return False

def convert_bit_to_unsorted_list():
    # [Column][Row] or [x][y]
    for column in range(XRES):
        bit_coordinates[column].insert(0, 0)
        bit_coordinates[column].append(0)
    bit_coordinates.insert(0, [0] * (XRES + 2))
    bit_coordinates.append([0] * (XRES + 2))
    pixel_coordinates = []
    for x in range(1, XRES + 1):
        for y in range(1, YRES + 1):
            if coordinate_check(x, y):
                pixel_coordinates.append([x, y])
    # pixel_coordinates.append(pixel_coordinates[0])
    return pixel_coordinates

# def sort_list(unsorted_list):
#     sorted_list = []
#     temp_list = []
#     for idx in range(len(unsorted_list)):
#         if idx == 0 or idx == 1: # First verical line
#             sorted_list.append(unsorted_list[0])
#             sorted_list.append(unsorted_list[1])
#         else:
#             for i in range(idx + 1, len(unsorted_list)):
#                 if sorted_list[idx][0] == sorted_list[idx - 1][0]: # Vertical
#                     if unsorted_list[i][1] == sorted_list[idx][1]: # Same horizontal line
#                         temp_list.append(unsorted_list[i])

def sortX(e):
    return(e[0])

def sortY(e):
    return(e[1])

def dfs(x, direct):
    global unsorted_list, result
    result.append(x)
    if len(result) == len(unsorted_list):
        return
    else:
        (u, v) = x
        vertical = list()
        horizontal = list()
        for point in unsorted_list:
            if (u == point[0]):
                vertical.append(point)
            if (v == point[1]):
                horizontal.append(point)
        if (direct == 1):
            vertical.sort(key = sortY)
            #print("Vertical:", vertical)
            index = vertical.index(x)
            if (index % 2 == 0):
                dfs(vertical[index + 1], 0)
                return
            else:
                dfs(vertical[index - 1], 0)
                return
        if (direct == 0):
            horizontal.sort(key = sortX)
            index = horizontal.index(x)
            #print("horizontal:", horizontal)
            #print("index:", index)
            if (index % 2 == 0):
                dfs(horizontal[index + 1], 1)
                return
            else:
                dfs(horizontal[index - 1], 1)
                return
bit_coordinates = []

try:
    with open(image_name + '.csv', newline='') as file:
        reader = csv.reader(file)
        bit_coordinates = list(reader)
except:
    print("Can't open file")
    quit()

XRES = image.width
YRES = image.height
result = []

unsorted_list = convert_bit_to_unsorted_list()
plt.scatter([point[0] for point in unsorted_list], [point[1] for point in unsorted_list])
plt.show()
# Write the list into a csv file
df = pd.DataFrame(unsorted_list)
df.to_csv(image_name + '_unsorted.csv', index=False, header=False)

dfs(unsorted_list[0], 1)
result.append(result[0])
plt.plot([p[0] for p in result], [p[1] for p in result], 'b-')
plt.show()
# Write the list into a csv file
df = pd.DataFrame(result)
df.to_csv(image_name + '_sorted.csv', index=False, header=False)
