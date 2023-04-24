# функция за въвеждане на коректна стойност за число
def get_user_number(max)->int:
	while True :
		try:
			x = int(input(f'Enter a number[1..{max}]: '))
			return x
		except:
			print('A NUMBER, please!!!')