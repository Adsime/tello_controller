from threading import Thread
from controller import Controller
from pynput.keyboard import Key, Listener, KeyCode
import time
import math

class InputHandler:

    modifier_map = {
        KeyCode(char='d'): (0, 100),
        KeyCode(char='a'): (0, -100),
        KeyCode(char='w'): (1, 100),
        KeyCode(char='s'): (1, -100),
        Key.up: (2, 100),
        Key.down: (2, -100),
        Key.right: (3, 100),
        Key.left: (3, -100),
    }

    def __init__(self, controller: Controller):
        self.state = [0, 0, 0, 0]
        self.controller = controller
        self.pressedKeys = []
        self.start()

    def perform(self, key, modifier=1):
        try:
            try:
                key = char(key)
            except:
                pass
            idx, speed = self.modifier_map[key]
            self.state[idx] += modifier * speed
        except:
            return
        self.controller.rc(self.state)

    def on_press(self, key):
        if key in self.pressedKeys:
            return
        self.pressedKeys.append(key)

        if key == Key.esc:
            self.controller.land()
            exit()

        
        if KeyCode(char="t") == key:
            self.controller.takeoff()
            return
        if KeyCode(char="l") == key:
            self.controller.land()
            return
        if KeyCode(char="c") == key:
            self.controller.stream()
            return

        
        self.perform(key)
        

    def on_release(self, key):
        self.pressedKeys.remove(key)
        self.perform(key, -1)

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release, suppress=False) as l:
            l.join()


        """
        while 1:
            newState = [0, 0, 0, 0]
            for i, key in enumerate(self.modifier_map):
                self.perform(newState, key, math.floor(i/2))
            # General cases

            if newState != self.state:
                self.state = newState
                print(newState)
                self.controller.rc(newState)

            time.sleep(0.01)"""