import os
from gtts import gTTS
import pygame
import mutagen.mp3


class Synthesizer:

    pygame.init()

    def __init__(self, dump_path: str):
        self.dump_path = dump_path

    """
    :param key: name of the mp3 file
    :param value: name of the sentence
    """
    def __setitem__(self, file_name: str, sentence: str):
        if not os.path.exists(self.dump_path):
            raise FileExistsError(self.dump_path)
        tts = gTTS(text=sentence, lang='de')
        tts.save(self.dump_path + '/' + file_name)

    def __getitem__(self, item: str):
        mp3 = mutagen.mp3.MP3(item)
        pygame.mixer.init(frequency=mp3.info.sample_rate)
        pygame.mixer.music.load(item)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass


if __name__ == '__main__':
    x = Synthesizer('../../../temp')
    x['test.mp3'] = 'Guten tag'
    x['good.mp3']
