# Transcrição de Vídeos do YouTube

Este projeto permite baixar o áudio de um vídeo do YouTube, transcrevê-lo para texto utilizando o modelo Whisper da OpenAI e gerar um resumo da transcrição. O resultado é salvo em um arquivo `resumo.md`.

## Funcionalidades
- Baixa o áudio de um vídeo do YouTube usando `yt-dlp`.
- Converte o áudio para o formato WAV com `ffmpeg`.
- Transcreve o áudio utilizando o modelo Whisper da OpenAI.
- Resume a transcrição utilizando o GPT-4 da OpenAI.
- Salva o resumo em um arquivo Markdown.

## Requisitos
Para executar este projeto, você precisará ter os seguintes itens instalados:
- Python 3.8+
- `yt-dlp`
- `ffmpeg`
- Chave de API da OpenAI com acesso aos modelos Whisper e GPT-4 (observação: o uso do GPT-4 requer uma assinatura ativa do GPT-4.0 da OpenAI).

## Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/transcritor-yt-video.git
   cd transcritor-yt-video
   ```


2. Crie um ambiente virtual e ative-o:
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows


3. Instale as dependências necessárias:
pip install -r requirements.txt


4. Configure sua chave de API da OpenAI: 
Abra o arquivo Python e substitua o valor de openai.api_key pela sua própria chave de API.


## Uso
Execute o script fornecendo a URL de um vídeo do YouTube como argumento:

```bash
python script.py "https://www.youtube.com/watch?v=exemplo"
```

### O script irá:

1. Baixar o áudio do vídeo.
2. Transcrever o áudio usando o Whisper.
3. Gerar um resumo da transcrição.
4. Salvar o resumo em resumo.md.

## Arquivos
- transcription.py: O script principal que baixa, transcreve e resume o áudio.
- requirements.txt: Contém as dependências Python necessárias para o projeto.
- venv/: A pasta do ambiente virtual (não incluída no repositório).
