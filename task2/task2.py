import math
import sys

def read_circle_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        x_center, y_center = map(float, lines[0].strip().split())
        radius = int(lines[1].strip())
    return x_center, y_center, radius

def read_points_data(filename):
    points = []
    with open(filename, "r") as file:
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x,y))
    return points

def point_position(x_center, y_center, radius, x, y):
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    if distance == radius:
        return 0
    elif distance < radius:
        return 1
    else:
        return 2

def main():
    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    x_center, y_center, radius = read_circle_data(circle_file)
    points = read_points_data(points_file)

    for x, y in points:
        position = point_position(x_center, y_center, radius, x, y)
        print(position)

if __name__ == "__main__":
    main()