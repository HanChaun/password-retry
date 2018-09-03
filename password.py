
password = 'a123456'
i = 3
while True:
	pwd = raw_input('please input password: ')
	if pwd == password:
		print('Login!')
		break
	else:
		i = i - 1
		print('password error! you have',i,'chance')

		if i == 0:
			break
