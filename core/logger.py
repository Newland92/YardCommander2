from datetime import datetime
from pathlib import Path


class Logger:
    def __init__(self):

        log_folder = Path("logs")
        log_folder.mkdir(exist_ok=True)

        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

        self.file = open(
            log_folder / filename,
            "a",
            encoding="utf-8"
        )

    def write(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        line = f"[{timestamp}] {message}"

        print(line)

        self.file.write(line + "\n")
        self.file.flush()

    def close(self):

        self.file.close()