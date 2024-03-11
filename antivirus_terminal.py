import hashlib
import json
import os
import time

import urllib3
from dotenv import load_dotenv
from pymisp import PyMISP
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# dotenv_path = '/media/nahin/newvolume2/4-1/security/Project/pythontest1/.env'
dotenv_path = load_dotenv()
# print(dotenv_path)

misp_url = 'https://localhost' 
misp_key = os.getenv("MISP_API_KEY")  
# print(misp_key)
verify_ssl = False

misp = PyMISP(misp_url, misp_key, verify_ssl)


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print("in on_created")
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def on_modified(self, event):
        print("in on_modified")
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def process_file(self, file_path):
        if os.path.exists(file_path):  # Check if file exists and not processed before
            print("in process_file")
            file_hash = self.calculate_hash(file_path, hashlib.md5)
            print(f"File modified: {file_path}")
            print(f"md5 Hash value: {file_hash}")
            
            attributes = misp.search(controller='attributes', type_attribute='md5', value=file_hash)

            print(json.dumps(attributes, indent=2))

    def calculate_hash(self, file_path, hash_algorithm):
        hasher = hash_algorithm()
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(65536)  # Read in 64k chunks
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()

def main():
    folder_to_watch = '/media/nahin/newvolume2/4-1/security/Project/pythontest1'
    

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()