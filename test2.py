
step=0
def cal(x,y):
	global step
	if (x==y):
		print(step)
		return
	elif (x<y) and ((y-x)>(2*x-y)):
		x=x*2
		step+=1
	elif (2*x-y)>(x-y/2):
		step+=x-y/2
		x=y/2
	print(step)
	cal(x,y)

cal(13,14)


