import yt_dlp

def baixar_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',  # Seleciona o melhor vídeo e áudio até 720p
        'merge_output_format': 'mp4',  # Mescla vídeo e áudio em um arquivo MP4
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

url_video = "https://www.youtube.com/watch?v=W-g6StRy1zY&t=122s"
baixar_video(url_video)