import time

for i in range(3):
    print(i*100)
    time.sleep(0.5)

for i in range(3):
    print(i*100, end='\r')
    time.sleep(0.5)

print()
