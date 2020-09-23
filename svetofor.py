import time


class TrafficLight:
    _color = None
    _colors = {'red': '[31m', 'yellow': '[33m', 'green': '[32m'}

    def __init__(self):
        self._color = self._colors

    def running(self):
        i = 0
        while i < 5:

            for key, el in TrafficLight._colors.items():
                print(f"\033{el} {key}")
                i += 1
                time.sleep(1)


traffic = TrafficLight()
traffic.running()

