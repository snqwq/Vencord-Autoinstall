import datetime

class Logger:
    def __init__(self, path=None):
        self.entries = []
        self.path = path

    def append(self, entry):
        print(entry)
        self.entries.append(entry)
    
    def save(self, path=None):
        if path is not None:
            self.path = path
        if self.path is None:
            raise ValueError("No path specified for logger.")
        
        with open(self.path, "a") as f:
            f.write(f"Log entry at {datetime.datetime.now().isoformat()}:\n")
            for entry in self.entries:
                f.write(f"{entry}\n")

    def __iter__(self):
        return iter(self.entries)

