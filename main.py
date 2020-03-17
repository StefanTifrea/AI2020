from greedyTSP import greedyRoute, distanceBetween2Points


def readFromFile():

    cities = []

    f = open("cities.txt", "r")
    n = int(f.readline())

    for i in range(n):
        cities.append([])

    for i in range(n):
        distances = f.readline().split(",")
        for x in distances:
            cities[i].append(int(x))

    start, end = f.readline().split(",")
    start = int(start)
    end = int(end)

    return cities, start, end


def getDistances(cities, start, end):

    cicle, cicleLength = greedyRoute(cities)
    route, distance = distanceBetween2Points(start, end, cities)
    return cicle, cicleLength, route, distance


def test():
    assert getDistances([[0, 10, 20, 40], [10, 0, 30, 150], [20, 30, 0, 60], [40, 150, 60, 0]], 0, 3) == ([0, 1, 2, 3], 140, [0,1,2,3], 100)


def printSolutions(cities, start, end):
    cicle, cicleLength, route, distance = getDistances(cities, start, end)
    print(cicle)
    print(cicleLength)
    print(route)
    print(distance)


def main():

    cities, start, end = readFromFile()
    test()
    printSolutions(cities, start, end)


main()
