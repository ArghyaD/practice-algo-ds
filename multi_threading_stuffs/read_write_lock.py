import threading

class ReadWriteLock:
    def __init__(self):
        self.mutex = threading.Lock()
        self.read_lock: threading.RLock = threading.RLock()
        self.write_lock = threading.Lock()
        self.writer_waiting = threading.Condition(self.mutex)

    def acquire_read(self):
        with self.read_lock:
            pass  # RLock allows multiple readers

    def release_read(self):
        with self.read_lock:
            pass  # RLock allows multiple readers

    def acquire_write(self):
        with self.write_lock:
            self.writer_waiting.acquire()
            while self.read_lock._is_owned():
                self.writer_waiting.wait()
            self.writer_waiting.release()

    def release_write(self):
        with self.write_lock:
            self.writer_waiting.acquire()
            self.writer_waiting.notify_all()
            self.writer_waiting.release()
