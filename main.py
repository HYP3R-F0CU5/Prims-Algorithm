m = int(input("m: "))

matrix = [list(int(x) for x in input().split()) for i in range(m)]

for x in range(m):
	a = [0]
	del matrix[a[-1]]
	#redo below line
	nums = [matrix[y][m] for y in range(len(matrix))]
	foo = nums.copy()
	foo.sort()
	a.append(nums.index(foo))

print(matrix)
