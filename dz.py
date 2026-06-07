age = int(input())
16
day = age * 365
hour = day * 24
minute = hour * 60
seconds = minute * 60
t = ('Вы находитесь на планете земля {} секунд!')
t.format(seconds)
print(t)
