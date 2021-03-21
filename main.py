# -*- coding: utf-8 -*-
from PyKanaTrainer.trainer import KanaTrainer
import random
import os

term_size = os.get_terminal_size()
trainer = KanaTrainer()

print("#" * (int(term_size[0]/2)-10) + "  PyKanaTrainer  " + "#" * (int(term_size[0]/2)-10))
print(str(trainer.get_random_kana()))
