line = input()
l_line = list(line)
result = 0
for number in l_line:
    result += int(number)
l_result = list(str(result))
output = []
alphabet = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for number in l_result:
    output.append(alphabet[int(number)])
print(' '.join(output))
