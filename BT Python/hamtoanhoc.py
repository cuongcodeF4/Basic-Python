from time import clock

start=clock()
for i in range(1,100000):
    print(i)
end=clock()
duration=end-start
print("t=",duration)
