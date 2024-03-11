import hashlib
import json
import os
import time
import tkinter as tk
from threading import Thread

import urllib3
from dotenv import load_dotenv
from pymisp import PyMISP
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

dotenv_path = load_dotenv()

misp_url = 'https://localhost' 
misp_key = os.getenv("MISP_API_KEY")
verify_ssl = False

misp = PyMISP(misp_url, misp_key, verify_ssl)

class LogViewer(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Log Viewer")
        
        self.log_text = tk.Text(master, wrap="word")
        self.log_text.pack(expand=True, fill="both")
        
    def update_logs(self, log_message):
        self.log_text.insert("end", log_message + "\n")
        self.log_text.see("end")

class MyHandler(FileSystemEventHandler):
    def __init__(self, log_viewer):
        super().__init__()
        self.log_viewer = log_viewer
    
    def on_created(self, event):
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        self.process_file(event.src_path)

    def process_file(self, file_path):
        if os.path.exists(file_path):
            file_hash_md5 = self.calculate_hash(file_path, hashlib.md5)
            file_hash_sha1 = self.calculate_hash(file_path, hashlib.sha1)
            file_hash_sha256 = self.calculate_hash(file_path, hashlib.sha256)
            
            log_message = f"File modified: {file_path}"
            log_message += f"\nmd5 Hash value: {file_hash_md5}"
            log_message += f"\nsha1 Hash value: {file_hash_sha1}"
            log_message += f"\nsha256 Hash value: {file_hash_sha256}"
            
            self.log_viewer.update_logs(log_message)
            
            attributes_md5 = misp.search(controller='attributes', type_attribute='md5', value=file_hash_md5)
            attributes_sha1 = misp.search(controller='attributes', type_attribute='sha1', value=file_hash_sha1)
            attributes_sha256 = misp.search(controller='attributes', type_attribute='sha256', value=file_hash_sha256)
            
            if len(attributes_md5['Attribute']) == 0 and len(attributes_sha1['Attribute']) == 0 and len(attributes_sha256['Attribute']) == 0:
                log_message = "No matches found in MISP"
            else:
                log_message = "Matches found in MISP"
                
            if len(attributes_md5['Attribute']) > 0:
                log_message += json.dumps(attributes_md5, indent=2)
            
            if len(attributes_sha1['Attribute']) > 0:
                log_message += json.dumps(attributes_sha1, indent=2)
                
            if len(attributes_sha256['Attribute']) > 0:
                log_message += json.dumps(attributes_sha256, indent=2)
                
                
            self.log_viewer.update_logs(log_message)

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
    folder_to_watch = os.getcwd()
    # folder_to_watch = '/media/nahin/newvolume2/4-1/security/Project/pythontest1'
    
    root = tk.Tk()
    log_viewer = LogViewer(root)
    log_viewer.pack(expand=True, fill="both")
    
    event_handler = MyHandler(log_viewer)
    observer = Observer()
    observer.schedule(event_handler, path=folder_to_watch, recursive=True)
    observer.start()

    try:
        root.mainloop()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
