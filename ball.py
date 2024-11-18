from main import SCREENSIZE


class Ball:
    def __init__(self, position=(SCREENSIZE[0]//2, SCREENSIZE[1]//2),vector=Vector2()):
        self.vector = vector
        self.position = position
        
    def update(self):
        self.position += self.vector