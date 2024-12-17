from pytube import YouTube

# URL do vídeo do YouTube
url = input("Digite a URL do vídeo do YouTube: ")

try:
    # Criar um objeto YouTube
    yt = YouTube(url)

    # Exibir informações do vídeo
    print(f"Título: {yt.title}")
    print(f"Duração: {yt.length // 60} minutos e {yt.length % 60} segundos")

    # Selecionar a melhor stream de vídeo
    stream = yt.streams.get_highest_resolution()

    print("Baixando o vídeo...")
    # Baixar o vídeo
    stream.download()

    print("Download concluído!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
