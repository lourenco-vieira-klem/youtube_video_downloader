# YOUTUBE VIDEO DOWNLOADER

Script útil para o download de vídeos do Youtube.

## Criação do ambiente virtual.

```bash
pipenv install -r requirements.txt
```
```bash
pipenv shell
```

## Execute o comando abaixo para realizar o download do arquivo de vídeo desejado.

```bash
python main.py https://www.youtube.com/watch?v=UX6K7waag5Q

## Não pode ser uma url de playlist.
```

## Escolha a opção desejada entre os options_ids apresentados.
```bash
option_id: 0 | mime_type: video/3gpp | resolution: 144p | file_size_in_mb 2.102 | file_codecs: ['mp4v.20.3', 'mp4a.40.2']
option_id: 1 | mime_type: video/mp4 | resolution: 360p | file_size_in_mb 15.14 | file_codecs: ['avc1.42001E', 'mp4a.40.2']
option_id: 2 | mime_type: video/mp4 | resolution: 720p | file_size_in_mb 38.781 | file_codecs: ['avc1.64001F', 'mp4a.40.2']
option_id: 3 | mime_type: video/mp4 | resolution: 1080p | file_size_in_mb 99.754 | file_codecs: ['avc1.640028']
option_id: 4 | mime_type: video/webm | resolution: 1080p | file_size_in_mb 66.437 | file_codecs: ['vp9']
option_id: 5 | mime_type: video/mp4 | resolution: 720p | file_size_in_mb 35.107 | file_codecs: ['avc1.4d401f']
option_id: 6 | mime_type: video/webm | resolution: 720p | file_size_in_mb 34.68 | file_codecs: ['vp9']
option_id: 7 | mime_type: video/mp4 | resolution: 480p | file_size_in_mb 18.77 | file_codecs: ['avc1.4d401e']
option_id: 8 | mime_type: video/webm | resolution: 480p | file_size_in_mb 17.752 | file_codecs: ['vp9']
option_id: 9 | mime_type: video/mp4 | resolution: 360p | file_size_in_mb 11.466 | file_codecs: ['avc1.4d401e']
option_id: 10 | mime_type: video/webm | resolution: 360p | file_size_in_mb 10.049 | file_codecs: ['vp9']
option_id: 11 | mime_type: video/mp4 | resolution: 240p | file_size_in_mb 4.94 | file_codecs: ['avc1.4d4015']
option_id: 12 | mime_type: video/webm | resolution: 240p | file_size_in_mb 4.875 | file_codecs: ['vp9']
option_id: 13 | mime_type: video/mp4 | resolution: 144p | file_size_in_mb 2.354 | file_codecs: ['avc1.4d400c']
option_id: 14 | mime_type: video/webm | resolution: 144p | file_size_in_mb 2.415 | file_codecs: ['vp9']
option_id: 15 | mime_type: audio/mp4 | resolution: None | file_size_in_mb 1.388 | file_codecs: ['mp4a.40.5']
option_id: 16 | mime_type: audio/mp4 | resolution: None | file_size_in_mb 3.681 | file_codecs: ['mp4a.40.2']
option_id: 17 | mime_type: audio/webm | resolution: None | file_size_in_mb 1.404 | file_codecs: ['opus']
option_id: 18 | mime_type: audio/webm | resolution: None | file_size_in_mb 1.844 | file_codecs: ['opus']
option_id: 19 | mime_type: audio/webm | resolution: None | file_size_in_mb 3.645 | file_codecs: ['opus']

choose an option from the options_ids: 

## Apenas opções existentes na listagem são aceitas.
## Deve ser inserido um número inteiro.
```

## Uma pasta downloads será criada e todos os downloads realizados são salvos nela.