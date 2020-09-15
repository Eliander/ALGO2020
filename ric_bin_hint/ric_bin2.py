import math

n = input("")
if n == "0":
    print(0)
    exit()
f = math.log2(int(n))
f = int(f % 10)
print(f)
exit()