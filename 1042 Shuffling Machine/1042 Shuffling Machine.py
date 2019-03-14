"""
start time: 2019-02-26 12-00-22 周二
end time: 2019-02-26 12-12-54 周二

"""

K = int(input())
cards = ["S{}".format(i+1) for i in range(13)]
cards.extend(["H{}".format(i+1) for i in range(13)])
cards.extend(["C{}".format(i+1) for i in range(13)])
cards.extend(["D{}".format(i+1) for i in range(13)])
cards.extend(["J1", "J2"])

orders = list(map(int, input().split()))

for i in range(K):
    new_cars = [0] * 54
    for j, each in enumerate(orders):
        new_cars[each - 1] = cards[j]
    cards = new_cars


print(" ".join(new_cars))

