

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        

        
    def __add__(self, other):
        if other is Vector2:
            return Vector2(self.x + other.x, self.y + other.y)
        if other is list or tuple and len(other) == 1:
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise Exception(f"Invalid Vector2 addition with {type(other)}")