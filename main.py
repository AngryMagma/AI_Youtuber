import pyttsx3
import pandas as pd
import time, random, os
from moviepy.editor import concatenate_audioclips, AudioFileClip


engine = pyttsx3.init()


file = pd.read_csv('jokes' + '.csv')

def GetJoke() :
    JokeID = random.randint(0, len(file))
    setup = file.iloc[JokeID]['Setup']
    punchline = file.iloc[JokeID]['PunchLine']
    return str(setup), str(punchline)

def concatenate_audio_moviepy(audio_clip_paths, output_path):
    clips = [AudioFileClip(c) for c in audio_clip_paths]
    final_clip = concatenate_audioclips(clips)
    final_clip.write_audiofile(output_path)


def SayJoke() :
    setup, punchline = GetJoke()
    engine.save_to_file(setup, 'setup.mp3')
    engine.save_to_file(punchline, 'punchline.mp3')
    engine.runAndWait()
    concatenate_audio_moviepy(['setup.mp3', 'nothing.mp3', 'punchline.mp3'], 'joke.mp3')
    os.remove('setup.mp3')
    os.remove('punchline.mp3')

    print(setup)
    print(punchline)
SayJoke()