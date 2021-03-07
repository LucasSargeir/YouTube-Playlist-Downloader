import moviepy.editor
import os

def extract_audio_video(nome_video, excluir_video = False):

	video = moviepy.editor.VideoFileClip(nome_video)
	audio = video.audio
	audio.write_audiofile(nome_video.replace('.mp4', '.mp3'))

	if(excluir_video == True):
		os.remove(nome_video)


if __name__ == '__main__':
	
	file_path = input('Entre com o arquivo que deseja extrair o áudio:')
	print('Deseja excluir o vídeo original?')
	excluir_video_op = input('[S/N]:').upper()

	while excluir_video_op != 'S' and excluir_video_op != 'N':
		excluir_video_op = input('OPÇÃO INVÁLIDA!\n[S/N]:').upper()		

	if excluir_video_op == 'S':
		extract_audio_video(file_path, excluir_video = True)
	else:
		extract_audio_video(file_path)