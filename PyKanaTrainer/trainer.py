from .data.kana import KanaData
import random

class KanaTrainer():
    def __init__(self):
        self.hiragana_to_romaji = KanaData.get_hirgana_to_romaji_dict()
        self.romaji_to_hiragana = KanaData.get_romaji_to_hiragana_dict()

    def get_random_hiragana_list(self) -> list:
        kana_list = list(self.romaji_to_hiragana.items())
        random.shuffle(kana_list)
        return kana_list

    def get_random_romaji_for_hiragana_list(self) -> list:
        romaji_list = list(self.hiragana_to_romaji.values())
        random.shuffle(romaji_list)
        return romaji_list

    def get_random_katakana_list(self) -> list:
        pass

    def get_random_romaji_for_katakana_list(self) -> list:
        pass
