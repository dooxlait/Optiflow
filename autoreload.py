import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_app()

    def restart_app(self):
        if self.process:
            self.process.kill()
        print("Lancement de l'application...")
        self.process = subprocess.Popen([sys.executable, self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Fichier modifié : {event.src_path}, relancement...")
            self.restart_app()

if __name__ == "__main__":
    script_to_run = "main.py"  # ton point d'entrée
    event_handler = ReloadHandler(script_to_run)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
