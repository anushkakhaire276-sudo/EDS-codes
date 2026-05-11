n = list(map(int,input().split()))
a = int(input())
f = False
for i in range(len(n)):
	if n[i] == a:
		print(i)
		f = True
		break

if not f:
	print("Not found")
