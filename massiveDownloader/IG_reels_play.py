from pynput import mouse, keyboard
import pickle
import time

# Cargar los eventos desde el archivo
with open('events.pkl', 'rb') as f:
    events = pickle.load(f)

# Configuración de controladores
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

# Funciones para reproducir eventos
def replay_events():
    for event in events:
        event_type, *details = event
        
        if event_type == 'mouse':
            action_type = details[0]
            if action_type == 'move':
                x, y = details[1:]
                mouse_controller.position = (x, y)
            elif action_type == 'click':
                x, y, button, pressed = details[1:]
                mouse_controller.position = (x, y)
                if pressed:
                    mouse_controller.press(button)
                else:
                    mouse_controller.release(button)
            elif action_type == 'scroll':
                x, y, dx, dy = details[1:]
                mouse_controller.position = (x, y)
                mouse_controller.scroll(dx, dy)
        
        elif event_type == 'keyboard':
            key, action = details
            if action == 'press':
                keyboard_controller.press(key)
            else:
                keyboard_controller.release(key)
        
        time.sleep(0.01)  # Simular el tiempo de espera entre eventos

# Reproducir los eventos
print('Reproduciendo eventos')
replay_events()
