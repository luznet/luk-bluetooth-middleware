import time 

class Watchdog:
    def __init__(self, timeout_seconds=10, on_timeout=None):
        self.timeout = timeout_seconds
        self.on_timeout = on_timeout
        self.last_signal = time.time()

    def signal(self):
        self.last_signal = time.time()

    def check(self):
        if time.time() - self.last_signal > self.timeout:
            print("[FAILSAFE] No commands received — resetting incline.")
            if self.on_timeout:
                self.on_timeout()
            self.signal()
