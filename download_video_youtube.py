from pytube import YouTube

def baixa_video(link, is_playlist = 0, output='./'):
	video = YouTube(link)
	print("\t-----------------[Sobre o vídeo]-----------------")
	print(f"\tLength : {video.length}")
	print(f"\tRating : {video.rating}")
	print(f"\tViews : {video.views}")
	print("\t-------------------------------------------------\n")

	streams = video.streams.filter(file_extension = "mp4")
	if is_playlist == 0:
		print("Escolha uma das opções abaixo:\n")
		for i in range(len(streams)):
			if streams[i].resolution != None:
				print(f"[{i+1:02}] - Qualidade: {streams[i].resolution}\t-\t{streams[i].fps}fps")
		print("\n[0] - Sair")
		index = int(input("\n-> ")) - 1
		if index == -1:
			print("Saindo...")
			return
	else:
		index = 0
	video.streams.get_by_itag(streams[index].itag).download(output_path = output)

if __name__ == "__main__":
	link = input("Entre com o link do vídeo a ser baixado: ")
	baixa_video(link)