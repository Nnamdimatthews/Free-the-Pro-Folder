n = int(input("enter a value: "))
j = int(input("enter value 2 :"))
g = int(input("enter value 3: "))

avg = (n + j + g) / 3
print("avg =", avg)

if avg > n and avg > j and avg > g:
    print("%d is higher than %d, %d, %d" %(avg, n, j, g))
elif avg > n and avg > j:
    print("%d is higher than %d, %d" %(avg, n, j))
elif avg > n and avg > g:
    print("%d is higher than %d, %d" %(avg, n, g))
elif avg > j and avg > g:
    print("%d is higher than %d, %d" %(avg, j, g))
elif avg > n:
    print("%d is just higher than %d" %(avg, n))
elif avg > j:
    print("%d is just higher than %d" %(avg, j))
elif avg > g:
    print("%d is just higher than %d" %(avg, g))
else:
  print("invalid input")