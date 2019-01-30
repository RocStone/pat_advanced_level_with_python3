"""
2019-01-30 15-57-20 周三：start
2019-01-30 17-19-35 周三: finished
坑：按照现实流程，假如你在下午三点开始业务，一直到下午五点下班了还没搞定，服务人员会继续为你服务，而不是赶走你，但是五点之后就不接受
    更多服务请求了，这已经是第二次我发现这些题目都要考虑现实情况，否则就不能满分。
"""
from collections import deque
from datetime import datetime, timedelta


class System:
    def __init__(self):
        global N, M
        self.inside = [deque(maxlen=M) for i in range(N)]
        self.outside = deque()

    def init(self):
        global N, M, K
        for i in range(N * M + 1, K + 1):
            self.outside.append(i)

        no = 1
        for i in range(M):
            for j in range(N):
                self.inside[j].append(no)
                if no == K:
                    return
                no += 1

    def run(self):
        global N, finish_times, p_times
        start_time = datetime.strptime('8:00', '%H:%M')
        for i in range(1, 540):
            for j in range(N):
                if len(self.inside[j]) != 0:
                    no = self.inside[j][0]
                    p_times[no] -= 1
                    if p_times[no] == 0:
                        self.inside[j].popleft()
                        finish_times[no] = start_time + timedelta(minutes=i)
                        if len(self.outside) != 0:
                            self.inside[j].append(self.outside.popleft())
        # 处理剩余队列的所有开头用户
        for i in range(N):
            if len(self.inside[i]) != 0:
                no = self.inside[i][0]
                finish_times[no] = start_time + timedelta(minutes=539+p_times[no])

    def print_result(self):
        global q_people, finish_times, flag_time
        for each in q_people:
            if finish_times[each] == flag_time:
                print('Sorry')
            else:
                print(finish_times[each].strftime('%H:%M'))


N, M, K, Q = list(map(int, input().split()))
p_times = [0]
p_times.extend(list(map(int, input().split())))
q_people = list(map(int, input().split()))
flag_time = datetime.strptime('8888', '%Y')
finish_times = [flag_time] * (K + 1)
system = System()
system.init()
system.run()
system.print_result()
