# generate a sequence like [0, 2, 6, 12, 20, 30, 42, 56, 72, 90] using list comprehensionI
arr = [x+x**2 for x in range(0, 10)]
print(arr)
