import keyboard
class Keyboard():
    buf = []
    @staticmethod
    def available():
        return len(Keyboard.buf) != 0

    @staticmethod
    def read():
        return Keyboard.buf.pop()
    
def get(name):
    Keyboard.buf.insert(0, name)
    
keyboard.on_press(get)
# pyglet.app.run()ad
while(True):
    if (Keyboard.available()):
        print(Keyboard.read().name)