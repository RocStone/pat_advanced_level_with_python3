"""
2019-01-30 18-25-18 周三: start
2019-01-30 19-54-54 周三: datetime.replace()函数莫名其妙没有作用，google一下相关帖子很少，以后用timedelta代替repalce
2019-01-30 20-28-27 周三: 莫名其妙的错误一大堆，估计是哪里数组越界了，累了，先不做了。
2019-01-30 21-35-19 周三: datetime相减，得到对象非常脑残，要知道真实的时间差用total_seconds()函数，不要访问seconds属性！
2019-01-30 21-39-25 周三: 第二个坑，如果一个人没有完整的通话记录，那么不要答应他的bill
2019-01-30 21-39-52 周三: finish，这破题做了3个小时，PAT题目无数的chinglish和一些完全没提到的隐含要求真TM坑爹
"""
from datetime import datetime, timedelta
from operator import attrgetter


class Record:
    def __init__(self, time, tag):
        self.time = datetime.strptime(time, "%m:%d:%H:%M")
        self.tag = tag


class Pair:
    def __init__(self, record1, record2):
        self.record1 = record1  # type: {Record}
        self.record2 = record2  # type: {Record}
        self.duration = (record2.time - record1.time).total_seconds() // 60
        self.cost = self.calc_cost()

    def calc_cost(self):
        global table
        cost = 0
        start_time = self.record1.time  # type: datetime
        end_time = self.record2.time  # type: datetime
        mid_time = start_time + timedelta(hours=1) + timedelta(minutes=-start_time.minute)
        while True:
            if mid_time <= end_time:
                cost += (mid_time - start_time).seconds / 60 * table[start_time.hour] / 100
                start_time = mid_time
                mid_time = mid_time + timedelta(hours=1)
            else:
                cost += (end_time - start_time).seconds / 60 * table[start_time.hour] / 100
                return cost


class User:
    def __init__(self, name, time, tag):
        self.name = name
        self.records = [Record(time, tag)]
        self.pairs = []
        self.total_cost = 0

    def make_pairs(self):
        self.records.sort(key=attrgetter('time'))
        record1 = None
        for record in self.records:
            if record1 is None and record.tag == 'on-line':
                record1 = record
            elif record1 is not None and record.tag == 'on-line':
                record1 = record
            elif record1 is not None and record.tag == 'off-line':
                self.pairs.append(Pair(record1, record))
                record1 = None

    def calc_total_cost(self):
        for pair in self.pairs:
            self.total_cost += pair.cost


table = list(map(int, input().split()))
N = int(input())
users = dict()
for i in range(N):
    name, time, tag = input().split()
    if name not in users:
        users[name] = User(name, time, tag)
    else:
        users[name].records.append(Record(time, tag))
for user in users.values():
    user.make_pairs()
    user.calc_total_cost()
for k in sorted(users):
    v = users[k]
    if v.pairs:
        print(f"{v.name} {v.records[0].time.month:02d}")
    for pair in v.pairs:
        print(f"{pair.record1.time.strftime('%d:%H:%M')} {pair.record2.time.strftime('%d:%H:%M')} {pair.duration:.0f}"
              f" ${pair.cost:.2f}")
    if v.pairs:
        print(f"Total amount: ${v.total_cost:.2f}")
