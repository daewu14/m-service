class Running:
    _instance = None
    _running = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_running(self):
        return self._running

    def increment(self):
        self._running += 1
