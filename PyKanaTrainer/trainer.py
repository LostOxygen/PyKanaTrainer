from .data.kana import KanaData
import random

class KanaTrainer():
    def __init__(self):
        self.hira_to_roma = KanaData.get_hirgana_to_romaji_dict()
        self.roma_to_hira = KanaData.get_romaji_to_hiragana_dict()

    def get_random_kana(self):
        return random.choice(list(self.hira_to_roma.keys()))
