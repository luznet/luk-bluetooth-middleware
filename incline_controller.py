import time
import threading

class InclineController:
    def __init__(self, min_incline=0, max_incline=12, step_delay=0.5, step_size=0.5):
        self.min_incline = min_incline
        self.max_incline = max_incline
        self.step_delay = step_delay
        self.step_size = step_size

        self.current_incline = 0
        self.target_incline = 0

        self._lock = threading.Lock()
        self._running = True

        # Start background thread
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def set_target(self, value):
        """Receive a new incline command from Zwift or another source."""
        safe_value = max(self.min_incline, min(self.max_incline, value))
        with self._lock:
            self.target_incline = safe_value
        print(f"[INFO] Target incline set to {safe_value}%")

    def _apply_incline(self, new_value):
        """
        Placeholder for your hardware communication.
        Replace this with your treadmill's actual command function.
        """
        print(f"[HARDWARE] Setting incline to {new_value}%")
        # Example: send_serial_command(f"INCLINE:{new_value}")

    def _run_loop(self):
        """Gradually moves incline toward the target."""
        while self._running:
            with self._lock:
                if self.current_incline < self.target_incline:
                    self.current_incline = min(
                        self.current_incline + self.step_size,
                        self.target_incline
                    )
                elif self.current_incline > self.target_incline:
                    self.current_incline = max(
                        self.current_incline - self.step_size,
                        self.target_incline
                    )
                else:
                    time.sleep(self.step_delay)
                    continue

                self._apply_incline(self.current_incline)

            time.sleep(self.step_delay)

    def stop(self):
        self._running = False
        self._thread.join()
