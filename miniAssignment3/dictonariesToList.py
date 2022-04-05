
original_Dictionary= {'HU': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

res = []
for key, val in original_Dictionary.items():
	res.append([key] + val)


print("The converted list is : " + str(res))
