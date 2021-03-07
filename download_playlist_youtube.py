from download_video_youtube import baixa_video
from extract_audio import extract_audio_video
from bs4 import BeautifulSoup
from functools import *
import moviepy.editor
import requests
import sys
import os


download_path = 'Playlist'

def get_playlist_name(url_playlist):
	r = requests.get(url_playlist).content

	soup = BeautifulSoup(r, 'html.parser')
	response = soup.find('title')

	return response.text.replace(' - YouTube', '')

def extrair_all_audio(path, apagar_video =True):
	filtraMp4 = lambda x: '.mp4' in x
	files = list(filter(filtraMp4, os.listdir(path)))
	for i in range(len(files)):
		os.system('clear')
		print(f"[{i + 1}] - Extraindo audio de -> {path + files[i]}\t\t\t[{i}\\{len(files)} - {i/len(files)*100:.2f}%]")
		extract_audio_video(os.path.join(path, files[i]), excluir_video = apagar_video)

def cria_estrutura_dir():
	local = '.'
	exist = os.listdir(local)
	folder = download_path

	if folder not in exist:
		local = os.path.join('.',folder)
		os.mkdir(local)
		os.system('cd '+ local)

def baixa_playlist(url_playlist, modo):

	r = requests.get(url_playlist).content

	soup = BeautifulSoup(r, 'html.parser')
	response = soup.find_all('script')

	data = ''

	for i in response:
		try:
			if 'var ytInitialData' in i.string:
				data = i.string
		except:
			pass


	if data != '':

		filtraUrls = lambda x: '/watch?' in x
		jsonData = data.replace('var ytInitialData = ', '')[:-2:1].split(':')
		filtraUrls2 = lambda x: 'index=' in x
		
		filteredData = filter(filtraUrls2, filter(filtraUrls,jsonData))
		

		completeUrls = lambda x: 'https://youtube.com'+x[1::].replace("\"", "\'").replace('\',\'webPageType\'', '')
		urls = list(map(completeUrls,filteredData))
		
		not_downloaded = []
		cria_estrutura_dir()
		
		os.system('clear')

		for i in range(len(urls)):
			try:
				print(f'Playlist: {url_playlist}\nNúmero de vídeos encontrados: {len(urls)}')
				print(f'Erros encontrados: {len(not_downloaded)}\nVídeos:')
				print(f'\t[{i+1}] - {urls[i]}')
				print(f'\tBaixando {i + 1}...\t\t\t\tConcluído [{i}\\{len(urls)} - {(i/len(urls))*100:.2f}% ]')
				baixa_video(urls[i], is_playlist = 1, output='./Playlist')
			except Exception as e:
				not_downloaded.append({'url': urls[i], 'erro': e})
			os.system('clear')

		print(f'Playlist: {url_playlist}\nNúmero de vídeos encontrados: {len(urls)}\nVídeos:')
		print(f'\tBaixado!!!\t\t[{len(urls)}\\{len(urls)} - 100% ]')

		if modo == 21:
			print('Extraindo audio...')
			extrair_all_audio(os.path.join('.', download_path), apagar_video = False)

		if modo == 22:
			print('Extraindo audio...')
			extrair_all_audio(os.path.join('.', download_path), apagar_video = True)


		return not_downloaded

	else:
		print('Não foi possível encontrar a playlist')



if __name__ == "__main__":
	
	if len(sys.argv) == 2:
		url_playlist = sys.argv[1]
	else:
		url_playlist = input('Entre com o link da playlist: ')

	playlist_name = get_playlist_name(url_playlist)

	op = 1
	op2 = 1

	errors = []

	while op != 4 :

		os.system("clear")

		print('------------[You Tube Playlist Downloader]------------\n')
		print('[1] - Download vídeos')
		print('[2] - Download áudios')
		print('[3] - Extrair áudios dos vídeos')
		print('[4] - Sair')

		print(f'\nPlaylist: {playlist_name}\nUrl: {url_playlist}\n')

		if len(errors) != 0:
			print('Erros no download:')
			for i in range(len(errors)):
				print(f"[{i}]\n---[url] -> {errors[i]['url']}\n---[erro] -> {errors[i]['erro']}")

		if op < 1 or op > 4:
			print('\nOPÇÃO INVÁLIDA, ENTRE COM UMA OPÇÃO VÁLIDA!')

		op = int(input('\nOPÇÃO: '))

		if op == 1:
			errors = baixa_playlist(url_playlist, 1)

		if op == 2:
			while op2 != 3:
				
				os.system("clear")
				
				print('------------------[Download Áudios]-------------------\n')
				print('[1] - Manter vídeos')
				print('[2] - Manter apenas os áudios')
				print('[3] - Voltar')

				if op2 < 1 or op2 > 3:
					print('\nOPÇÃO INVÁLIDA, ENTRE COM UMA OPÇÃO VÁLIDA!')

				op2 = int(input('\nOPÇÃO: '))

				if op2 == 1:
					errors = baixa_playlist(url_playlist, 21)
				if op2 == 2:
					errors = baixa_playlist(url_playlist, 22)
				if op2 == 3:
					op2 = 1
					break;

		if op == 3:
			while op2 != 3:
				
				os.system("clear")
				
				print('-------------------[Extrair Áudios]--------------------\n')
				print('[1] - Manter vídeos')
				print('[2] - Manter apenas os áudios')
				print('[3] - Voltar')

				if op2 < 1 or op2 > 3:
					print('\nOPÇÃO INVÁLIDA, ENTRE COM UMA OPÇÃO VÁLIDA!')

				op2 = int(input('\nOPÇÃO: '))

				if op2 == 1:
					extrair_all_audio(os.path.join('.', download_path), apagar_video = False)
				if op2 == 2:
					extrair_all_audio(os.path.join('.', download_path), apagar_video = True)
				if op2 == 3:
					op2 = 1
					break;

		if op == 4:
			print('Saindo...')
			