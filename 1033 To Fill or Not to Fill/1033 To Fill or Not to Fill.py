"""
start time: 2019-02-21 20-17-15 周四
end time: 2019-02-21 22-37-52 周四
坑： f-string 输出格式时注意不要多家空格，比如f"{a: .2f}"会让你莫名其妙左边多一个空格，正确是f"{a:.2f}"
    在贪心时，假设行驶范围内有多个站点的price比当前站点好，那么应该先开到最近更好的站点，而不是直接开到最便宜的站点
    因为这道题的思路是，尽可能少用费用高的油，所以只要有更好的，我们就赶快过去

# 到一个站点
# 计算当前站点的能够支撑我走多远，求出范围内的所有站点
# 从范围内的站点里挑选一个费用最小的站点，和当前站点做对比
    # 假设当前站点更便宜
        # 在当前站点加满油，然后行驶到下一个站点，形式到了之后可能会有油量剩余
    # 假设下一个站点更便宜
        # 计算剩余油量是否足以到达下一个站点，如果能到就不用加油，否则要加油

"""
from cmath import inf


class Station:
    def __init__(self, price, dist):
        self.price = price
        self.dist = dist

    def __repr__(self):
        return f"{self.price} {self.dist}"


def get_min_price_station():
    global cur_station, capacity, stations
    max_run_dist = cur_station.dist + capacity * run_dist
    next_station = None
    next_price = inf
    for station in stations:
        if cur_station.dist < station.dist <= max_run_dist:
            if station.price <= next_price:
                next_station = station
                next_price = station.price
        if station.dist > max_run_dist:
            break

    if next_price < cur_station.price:
        # 如果下一个站点更便宜，那么重新找，我们要找个第一个比当前站点便宜的地方
        next_price = cur_station.price
        for station in stations:
            if cur_station.dist < station.dist <= max_run_dist:
                if station.price < next_price:
                    next_station = station
                    break

    return next_station


capacity, destination_dist, run_dist, n = list(map(int, input().split()))
stations = []
for i in range(n):
    price, dist = list(map(float, input().split()))
    if dist < destination_dist:
        stations.append(Station(price, dist))
stations.append(Station(inf, destination_dist))
stations.sort(key=lambda x: x.dist)

cur_station = stations[0]
oil_remain = 0
total_cost = 0

if cur_station.dist > 0:
    print(f"The maximum travel distance = 0.00")
    exit(0)

while True:
    next_station = get_min_price_station()
    if next_station is None:
        print(f"The maximum travel distance = {cur_station.dist + capacity * run_dist:.2f}")
        break
    if next_station.price > cur_station.price:
        if cur_station.dist + capacity * run_dist < destination_dist:
            # 假如此时还不能够直接跑到终点，那么再继续折腾
            total_cost += (capacity - oil_remain) * cur_station.price
            oil_remain = capacity - (next_station.dist - cur_station.dist) / run_dist
        else:
            # 假如现在能直接到终点了，那不BB直接去了
            total_cost += ((destination_dist - cur_station.dist) / run_dist - oil_remain) * cur_station.price
            print(f'{total_cost:.2f}')
            break
    else:
        total_cost += ((next_station.dist - cur_station.dist) / run_dist - oil_remain) * cur_station.price
        oil_remain = 0
    cur_station = next_station
