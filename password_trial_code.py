# password trial code
sp = 'hank5134' # sp = set password
x = 1 # x = number of tirals
while True:
	ip = input('please enter the password: ') # ip = input password
	if ip == sp:
		print('password is correct.')
		break
	elif ip != sp and x < 4:
		print('password is incorrect.')
		y = 3 - x # remaining trials
		if y == 0:
			print('account is locked because password is not correctly input mor than 3 times.')
			break
		x = x + 1
		print('remaining trials: ', y)