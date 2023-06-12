import librosa
import json

## by DieguinDG ##

def detectar_batidas(audio_path):
    # Carregar o áudio
    y, sr = librosa.load(audio_path)

    # Detectar as batidas
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    # Converter os frames de batida para milissegundos inteiros
    beat_times = (librosa.frames_to_time(beat_frames, sr=sr) * 1000).astype(int)

    beat_times = beat_times.tolist()
    beat_times.insert(0, 0)

    return beat_times

def salvar_anotacoes_batidas(batidas, output_path):
    data = {
        'beats': batidas
    }

    with open(output_path, 'w') as file:
        json.dump(data, file)

# Caminho para o arquivo de áudio
audio_path = 'audio.ogg' ## you can use .ogg, .wav, .mp3, etc.

# Detectar as batidas
batidas = detectar_batidas(audio_path)

# Caminho para o arquivo JSON de saída
output_path = 'beats.json'

# Salvar as anotações das batidas em um arquivo JSON
salvar_anotacoes_batidas(batidas, output_path)
