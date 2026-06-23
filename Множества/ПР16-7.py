agent = (2, 2)
points = {(1, 1), (5, 5), (0, 3)}
print("Агент: ", agent)
print("Точки: ", *points)

distances = []
for point in points:
    dist = abs(point[0]-agent[0]) + abs(point[1]-agent[1])
    distances.append((dist, point))

nearest = distances[0][1]
print("Ближайшая точка: ", nearest)