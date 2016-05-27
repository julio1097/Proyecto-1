def prob_1 (n):
	if n % 2 == 2:
		return True
	else:
		return False
def prob_2 (n):
	conver = (n - 32) * 5/9
	return conver
def prob_3 (a,b):
	oper = a ** b
	return oper
def prob_4 (num, palabra):
	cas= (num -len(palabra))//2
	centrado= num*(cas + len (palabra))
	return "*"*cas+palabra+"*"cas2

