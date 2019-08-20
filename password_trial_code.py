# password trial code
sp = 'hank5134' # sp = set password
x = 3 # x = remaining trials
while True:
	ip = input('please enter the password: ') # ip = input password
	if ip == sp:
		print('password is correct.')
		break
	else:
		x = x - 1
		print('password is incorrect.', 'there are', x, 'times left.')
		if x == 0:
			print('account is locked because password is not correctly input mor than 3 times.')
			break