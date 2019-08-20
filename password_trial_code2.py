# 不使用while true完成此程式
sp = 'hank5134' # sp = set password
x = 3 # x = trials left
while x > 0:
	x = x - 1
	ip = input('please enter the password: ')
	if ip == sp:
		print('password is correct.')
		break
	else:
		print('password is not correct.')
		if x > 0:
			print('trials remaining: ', x)
		else:
			print('account is locked.')