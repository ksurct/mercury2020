import pyglet
# motors = [M1, M2, M3, M4]

window = pyglet.window.Window(width=10, height=10)
@window.event
def on_key_press(key, mod):
    key = chr(key)
    print("Pressed", key)

def rel(key):
    print("Something released")
    
#listener = keyboard.Listener(onpress=on_press, onrelease=rel)
#with keyboard.Listener(onpress=on_press, onrelease=rel) as l:
#    l.join()
pyglet.app.run()
import time
while (True):
    print("Hello")
    time.sleep(1)