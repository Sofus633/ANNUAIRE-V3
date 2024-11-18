

class Display:
    def __init__(self, todisplay=[]):
        self.todisplay = todisplay
        
    def clear(self):
        self.todispla = []
        
    def add(self, toadd, index=False):
        if index != False and index is int:
            self.todisplay.insert(index, toadd)
        elif index == False :
            self.todisplay.append(toadd)
        
    def disp(self):
        for val in self.todisplay:
            if vall is Ball