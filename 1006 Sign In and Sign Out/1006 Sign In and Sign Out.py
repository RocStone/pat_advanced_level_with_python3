from datetime import datetime


M = int(input())
earliest_name = ''
latest_name = ''
earliest_time = datetime.strptime('23:59:59', '%H:%M:%S')
latest_time = datetime.strptime('00:00:00', '%H:%M:%S')
for i in range(M):
    name, sign_in, sign_out = input().split()
    sign_in = datetime.strptime(sign_in, '%H:%M:%S')
    sign_out = datetime.strptime(sign_out, '%H:%M:%S')
    if earliest_time > sign_in:
        earliest_time = sign_in
        earliest_name = name
    if latest_time < sign_out:
        latest_time = sign_out
        latest_name = name

print('{} {}'.format(earliest_name, latest_name))
