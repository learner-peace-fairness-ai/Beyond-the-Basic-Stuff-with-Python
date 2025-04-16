class AsciiArt:
    def __init__(self, characters):
        self._characters = characters
    
    @classmethod
    def from_file(cls, filename):
        with open(filename) as fr:
            characters = fr.read()
            return cls(characters)
    
    def display(self):
        print(self._characters)

    # 他の AsciiArt メソッドはここに書く


face1 = AsciiArt(
    " ________ \n" +
    "|  .  .  |\n"  +
    "| \\____/ |\n"  +
    "|________|"
)
face1.display()

face2 = AsciiArt.from_file("face.txt")
face2.display()
