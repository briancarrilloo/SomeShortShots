# Este script se debe ejecutar desde un reel dentro del perfil de un usuario. Abrir en segundo plano un bloc de notas donde el script pegará las URL que vaya encontrando.

from pynput import mouse, keyboard
import pickle
import time

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

time.sleep(5)

print('Recording...')
# Iniciar los listeners
mouse_listener.start()
keyboard_listener.start()

# Grabar durante 10 segundos
time.sleep(10)

# Detener los listeners
mouse_listener.stop()
keyboard_listener.stop()
print('Finished!')

# Guardar los eventos en un archivo
with open('events.pkl', 'wb') as f:
    pickle.dump(events, f)
