def greedyRoute(cities):

    n = len(cities[0])

    options = {}
    for i in range(n):
        options[i] = i

    path = [0]
    options.pop(0, None)

    while len(path) < n:
        min = 999999999
        city = 0
        for i in options.items():
            if cities[path[len(path) - 1]][i[1]] < min:
                min = cities[path[len(path) - 1]][i[1]]
                city = i[1]
        path.append(city)
        options.pop(city, None)

    return path, routeValue(cities, path)


def routeValue(cities, path):

    dist = 0
    for i in range(len(path) - 1):
        dist += cities[path[i]][path[i+1]]

    dist += cities[path[len(path) - 1]][0]
    return dist


def minRoad(departPoint, cities, partOf):

    min = 999999999
    min_index = 0

    for u in range(len(cities[departPoint])):
        if min > cities[departPoint][u] and partOf[u] == False:
            min = cities[departPoint][u]
            min_index = u

    return min_index, min


def distanceBetween2Points(start, end, cities):

    n = int(len(cities))
    partOfRoad = [False] * n
    partOfRoad[start] = True
    current = start
    route = [start]

    dist = 0
    while current != end:
        newCity, distance = minRoad(current, cities, partOfRoad)
        route.append(newCity)
        dist += distance
        partOfRoad[newCity] = True
        current = newCity

    return route, dist
