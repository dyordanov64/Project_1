# Проект 5 Управление на банкова сметка
# Описание:
# Проектът представлява обикновена банкова система. Той съдържа само
# административна част, без да се дава възможност на потребителя да влиза в система с
# потребителско име и парола. Административната част включва всички основни
# функции: създаване на нов акаунт, преглед на записа на притежателите на акаунти,
# теглене и депозит на сума, запитване за салдо. Потребителят трябва лесно да може да
# проверява общите записи на банковата сметка. Потребителят може да създаде акаунт,
# като предостави първоначална сума за депозиране. Той може да депозира и тегли пари
# само като предостави номера на потребителската си сметка и въведе сума.
# Потребителят може да проверява за клиенти и техният баланс по сметка.


import os
from time import sleep
import lib_1.my_IO as aux

# define our clear function
def clear_screen():
	# for windows
	if os.name == 'nt':
		_ = os.system('cls')
	# for mac and linux(here, os.name is 'posix')
	else:
		_ = os.system('clear')

# Функция за създаване на нов акаунт


#  ----Изработване на главното меню
def show_actions(line_width):
	print('='*line_width)
	print('='*line_width)
	print(f'---- {"Welcome to Times Bank":^{line_width-10}s} ----')
	print('*'*line_width)
	print(f'=<< {"1. Open new bank acount":<{line_width-8}s} >>=')
	print(f'=<< {"2. Whithdraw Money":<{line_width-8}s} >>=')
	print(f'=<< {"3. Deposit Money":<{line_width-8}s} >>=')
	print(f'=<< {"4. Check Customers & Balance":<{line_width-8}s} >>=')
	print(f'=<< {"5. Exit/Quit":<{line_width-8}s} >>=')
	print('*'*line_width)

account_list = [
	{ 
		'account_number' : '0000000001',
		'account_owner_full_name' : 'Даниел Йорданов',
		'account_pin' : '6401',
		'account_balance' : 0		
	},
	{
		'account_number' : '0000000002',
		'account_owner_full_name' : 'Пламен Иванов',
		'account_pin' : '3214',
		'account_balance' : 1000	
	},
	{
		'account_number' : '0000000003',
		'account_owner_full_name' : 'Стефан Тодоров',
		'account_pin' : '1632',
		'account_balance' : 2000
	},
	{
		'account_number' : '0000000002',
		'account_owner_full_name' : 'Атанас Стоянов',
		'account_pin' : '3341',
		'account_balance' : 5000	
	}
]

while True :
	show_actions(60)
	choice = aux.get_user_number(5)

	if choice == 1 : pass
	elif choice == 2 : pass
	elif choice == 3 : pass
	elif choice == 4 : pass
	else : quit()

	sleep(1)
	clear_screen()
	print('test')
