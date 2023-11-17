class Shape():
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def __str__(self):
        return "I am a " + self.color + " " + self.shape
    
    def changeColor(self, color):
        self.color = color
    
square = Shape("square", "red")
print(square)
square.changeColor("blue")
print(square)