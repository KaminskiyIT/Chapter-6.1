#! python3
# pw.py - Программа для незащищенного копирования паролей.

PASSWORDS = {'email': 'F7mbzdjkbmzx88gjhsjJHGYbn7',
	     'blog': 'KHkbjkjhIUhJHKjnjBIUhkjnbj',
	     'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Использование: python pw.py [имя учетной записи] - копирование пароля учетной записи')
	sys.exit()

account = sys.argv[1] # первый аргумент командной строки - это
					  # имя учетной записи
					  
if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Пароль для ' + account + ' скопирован буфер.')
else:
	print('Учетная запись ' + account + ' отсутствует в списке.')
