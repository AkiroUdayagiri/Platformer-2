from numpy import array
from PIL import Image
from fire import Fire
from block import Block
from constants import HEIGHT, WIDTH
from get_background import get_background

class LevelMaker:
    def __init__(self, level, level_background, level_block, blocks, fire):
        self.level = level
        self.level_background, self.bg_image = get_background(level_background)
        self.level_block = level_block
        self.block_size = 96
        self.blocks = blocks
        self.fire = fire
        self.objects = []

    def create_level(self):
        floor = [Block(i * self.block_size, HEIGHT - self.block_size, self.block_size)
                 for i in range(0, WIDTH // self.block_size)]
        self.objects = floor + self.blocks + self.fire
        print(self.objects)

        return self.objects

