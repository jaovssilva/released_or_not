import requests
import json
import telepot
from telepot.loop import MessageLoop
import time

with open('data.json', 'r') as f:
	data = json.load(f)

telegram_bot = telepot.Bot(data['token'])


def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	if command == '/help':
		telegram_bot.sendMessage(chat_id, "O seguintes animes estão listados:\n"
											"/kimetsu - Verifica se saiu episódio do Kimetsu no Yaiba.\n"
											"/opm - Verifica se saiu episódio do One Punch Man.\n"
											"/dororo - Verifica se saiu episódio do Dororo.")

	if command == '/kimetsu':
		kimetsu_id = str(data['kimetsu'])
		kimetsu = requests.head(
			f'https://www.dreamanimes.com.br/online/legendado/kimetsu-no-yaiba/episodio/{kimetsu_id}')

		if kimetsu.status_code == 200:
			telegram_bot.sendMessage(chat_id, f'Saiu ep novo de Kimetsu no Yaiba! EP {kimetsu_id}.')
			print(f'Saiu ep novo de Kimetsu no Yaiba! EP {kimetsu_id}.')
			data['kimetsu'] += 1

			with open('data.json', 'w') as f:
				json.dump(data, f, sort_keys=False, indent=4)
		else:
			telegram_bot.sendMessage(chat_id, 'Ainda não saiu ep novo de Kimetsu no Yaiba.')
			print('Ainda não saiu ep novo de Kimetsu no Yaiba.')

	if command == '/opm':
		opm_id = str(data['opm'])
		if int(opm_id) < 10:
			opm = requests.head(f'https://myanimesonline.net/episodios/one-punch-man-2-episodio-0{opm_id}/')
		else:
			opm = requests.head(f'https://myanimesonline.net/episodios/one-punch-man-2-episodio-{opm_id}/')

		if opm.status_code == 200:
			telegram_bot.sendMessage(chat_id, f'Saiu ep novo de One Punch Man! EP {opm_id}.')
			print(f'Saiu ep novo de One Punch Man! EP {opm_id}.')
			data['opm'] += 1

			with open('data.json', 'w') as f:
				json.dump(data, f, sort_keys=False, indent=4)
		else:
			telegram_bot.sendMessage(chat_id, 'Ainda não saiu ep novo de One Punch Man.')
			print('Ainda não saiu ep novo de One Punch Man.')

	if command == '/dororo':
		dororo_id = str(data['dororo'])
		dororo = requests.head(f'https://ww4.animesonline.online/video/dororo-episodio-{dororo_id}/')

		if dororo.status_code == 200:
			telegram_bot.sendMessage(chat_id, f'Saiu ep novo de Dororo! EP {dororo_id}.')
			print(f'Saiu ep novo de Dororo! EP {dororo_id}.')
			data['dororo'] += 1

			with open('data.json', 'w') as f:
				json.dump(data, f, sort_keys=False, indent=4)
		else:
			telegram_bot.sendMessage(chat_id, 'Ainda não saiu ep novo de Dororo.')
			print('Ainda não saiu ep novo de Dororo.')


if __name__ == '__main__':
	MessageLoop(telegram_bot, handle).run_as_thread()

	while True:
		time.sleep(10)














