n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
result = dict((i, a.count(i)) for i in a)
print (result)