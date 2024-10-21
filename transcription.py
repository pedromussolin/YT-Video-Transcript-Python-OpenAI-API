import yt_dlp
import ffmpeg
import openai
import sys
import os

# Configuração do cliente da OpenAI
openai.api_key = "API_KEY"

# Função para baixar e converter áudio do vídeo
def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:/ffmpeg/bin',
        'outtmpl': 'audio.%(ext)s',  # Nome do arquivo de saída
        'noplaylist': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url, download=True)
    
    return 'audio.wav' 

# Função para transcrever o áudio usando OpenAI Whisper
def transcribe_audio(filename):
    with open(filename, "rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
        )
    return transcript['text']

# Função para criar um resumo do conteúdo transcrito
def summarize_transcript(transcript):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "system",
            "content": "Você é um assistente que resume vídeos de forma detalhada e objetiva. Responda com formatação Markdown."
        }, {
            "role": "user",
            "content": f"Descreva o seguinte vídeo: {transcript}"
        }]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    # Captura da URL do vídeo a partir dos argumentos do script
    url = sys.argv[1]
    
    # Download e conversão do áudio
    audio_filename = download_audio(url)
    if audio_filename:
        # Transcrição do áudio
        transcript = transcribe_audio(audio_filename)

        # Resumo do conteúdo
        summary = summarize_transcript(transcript)

        # Salvando o resumo em um arquivo Markdown
        with open("resumo.md", "w", encoding="utf-8") as md_file:
            md_file.write(summary)

        print("Resumo salvo em resumo.md")
        os.remove(audio_filename)  # Remove o arquivo .wav temporário
