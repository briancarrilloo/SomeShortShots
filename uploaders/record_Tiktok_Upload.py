from pynput import mouse, keyboard
import pickle

# Lista para almacenar todos los eventos
events = []

def on_click(x, y, button, pressed):
    events.append(('mouse', 'click', x, y, button, pressed))

def on_move(x, y):
    events.append(('mouse', 'move', x, y))

def on_scroll(x, y, dx, dy):
    events.append(('mouse', 'scroll', x, y, dx, dy))

def on_press(key):
    try:
        events.append(('keyboard', key.char, 'press'))
    except AttributeError:
        events.append(('keyboard', key, 'press'))

def on_release(key):
    try:
        events.append(('keyboard', key.char, 'release'))
    except AttributeError:
        events.append(('keyboard', key, 'release'))

# Configuración de los listeners
mouse_listener = mouse.Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Iniciar los listeners
mouse_listener.start()
keyboard_listener.start()

# Grabar durante 10 segundos
import time
time.sleep(10)

# Detener los listeners
mouse_listener.stop()
keyboard_listener.stop()

# Guardar los eventos en un archivo
with open('events.pkl', 'wb') as f:
    pickle.dump(events, f)
