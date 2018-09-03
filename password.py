
password = 'a123456'
i = 3
while i > 0:
	pwd = raw_input('please input password: ')
	if pwd == password:
		print('Login!')
		break
	else:
		i = i - 1
		print('password error! you have',i,'chance')

