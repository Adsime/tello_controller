from threading import Thread
from controller import Controller
from pynput.keyboard import Key, Listener, KeyCode
import time
import math

class InputHandler:

    def __init__(self, controller: Controller):
        self.state = [0, 0, 0, 0]
        self.controller = controller
        self.pressedKeys = []
        self.start()

        self.action_map = {

            # Movement
            KeyCode(char='d'): lambda x: self.perform_movement(0, x * 100),
            KeyCode(char='a'): lambda x: self.perform_movement(0, x * -100),
            KeyCode(char='w'): lambda x: self.perform_movement(1, x * 100),
            KeyCode(char='s'): lambda x: self.perform_movement(1, x * -100),
            Key.up: lambda x: self.perform_movement(2, x * 100),
            Key.down: lambda x: self.perform_movement(2, x * -100),
            Key.right: lambda x: self.perform_movement(3, x * 100),
            Key.left: lambda x: self.perform_movement(3, x * -100),

            # Meta actions
            Key.esc: self.safe_quit,
            KeyCode(char="t"): lambda x: self.controller.takeoff,
            KeyCode(char="l"): lambda x: self.controller.land,
            KeyCode(char="c"): lambda x: self.controller.stream,
            KeyCode(char="f"): lambda x: self.controller.speed(100),
            KeyCode(char="r"): lambda x: self.controller.speed(10),
        }

    def safe_quit(self):
        self.controller.land()
        exit()

    def perform_movement(self, state_idx, speed):
        self.state[state_idx] += speed
        self.controller.rc(self.state)

    def on_press(self, key):
        if key in self.pressedKeys:
            return
        self.pressedKeys.append(key)
        self.action_map[key](1)

    def on_release(self, key):
        self.pressedKeys.remove(key)
        if not self.pressedKeys:
            self.controller.stop()
            self.state = [0, 0, 0, 0]
            return
        self.action_map[key](-1)

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