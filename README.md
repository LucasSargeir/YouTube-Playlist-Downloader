# YouTube Playlist Downloader

**Tecnologias:**

- Python (3.8).

  

**Dependências:**

- BeautifulSoup;
- Moviepy;
- Requests;
- Pytube.



## Descrição

Com o objetivo de facilitar o download de vídeos e músicas do YouTube construi esse script em Python que varre uma playlist baixando cada vídeo incluido nela.

O script oferece algumas opções de download, podendo baixar os vídeos, os audios ou ambos. Além disso, caso já tenha baixado os vídeos ele permite que você extraia os áudios deles.

Os vídeos são baixados para a mesma pasta onde o script se encontra, para que não bagunce os arquivos do diretório é criado uma pasta Playlist(caso não exista) para armazenar os arquivos.



## Execução

A execução do script é muito simples, basta executar o script python. No shell você pode executa-lo com o comando abaixo:

```bash
python download_playlist_youtube.py
```

A execução padrão irá solicitar a url da playlist, mas caso queira pular essa etapa, basta  passar a url como parâmetro de comando de linha, veja o exemplo abaixo:

```bash
python download_playlist_youtube.py <link_da_sua_playlist>
```



## Módulos

O script conta com 2 módulos, o módulo de download de vídeo e o módulo de extração de áudio. 

##### Módulo de Dowload de Vídeo

Esse módulo é utilizado para baixar cada vídeo individualmente. Caso haja a necessidade de baixar apenas um vídeo você pode utiliza-lo executando o comando abaixo:

```bash
python download_video_youtube.py
```

Após a execução do comando será solicitado o link do vídeo, depois será apresentado todas as opções disponíveis para download, escolha o número que indica a opção desejada e o download começará.

> **Obs:** Por padrão quando baixamos os vídeos por uma playlist a primeira opção de download é escolhida.



##### Módulo de Extração de Áudio

Esse módulo é utilizado para extrair o áudio dos vídeos baixados individualmente. Caso haja a necessidade de extrair o áudio de um vídeo especifico você pode utiliza-lo executando o comando abaixo:

```bash
python extract_audio.py
```

Após a execução do comando será solicitado o caminho do vídeo que deseja extrair o áudio, após, perguntará se deseja manter ou não o vídeo original. Especificados os valores a extração começará.

> **Obs:** O módulo moviepy, utilizado para extração, utiliza o ffmpeg, tenha certeza de que ele está instalado na sua máquina.



## Possiveis Erros

- Playlist Privada

  O script utiliza de web scrapping para encontrar os links dos vídeos para download. Tenha certeza de que a playlist está pública ou não listada para baixá-la.