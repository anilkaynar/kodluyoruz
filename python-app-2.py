import math

# Defining the points
points = [(2, 3), (4, 5), (1, 2), (7, 8)]

# Function to calculate Euclidean distance
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculating distances between every pair of points
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):  # Only unique pairs
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Finding the minimum distance
min_distance = min(distances)
print(f"The minimum Euclidean distance is: {min_distance}")
