num1=[1,2,3,4,5,6,7,8,9]
sign=['','+','-']
combo=[0]*9
def cal(i):
	for v in range(0,3):
		combo[i] = sign[v]
		if i>=8:
			tong=''
			for j in range(0,len(combo)):
				tong+=combo[j]+str(num1[j])
			if (eval(tong)==100):
				print(tong)
		else:
			cal(i+1)
cal(0)

