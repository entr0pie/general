from colorama import Fore 
from json import loads
from os import system
import os.path as verify_path
from time import sleep

class selection: 
    def art(self, counter):
        self.input_art = ""
        self.input_art += f"[url ({Fore.YELLOW}{counter}{Fore.WHITE})] ~> "
    
    def main(self):
        tracks = []
        counter = 1
        while True:
            self.art(counter)
            track = input(self.input_art)
            if track == "exit":
                exit()
            if track == "done":
                break
            tracks.append(track)
            counter += 1
        return tracks 

json_file = open("/home/neo/github/ytmp3-r/files/config.json")
json_file_string = json_file.read()
json_content = loads(json_file_string)
path = json_content["root_path"]
history_file= json_content["history_file"]

class download:  
    def art(self, name):
        self.playlist_art = f">>> {Fore.RED}wild{Fore.WHITE} " 
        self.playlist_art += f"Playlist Has Appeared! {Fore.GREEN}"
        self.playlist_art += f"Adding:{Fore.WHITE} {name}"   
        self.download_art = f">>> [{Fore.GREEN}*{Fore.WHITE}] "
        self.download_art += f"{Fore.GREEN}Downloading:{Fore.WHITE} {name}"
    
    def append_in_history(self, name): 
        file_obj = open(history_file, "a")
        file_obj.write(f"{name}\n")

    def main(self, tracks, save_on_history=False): 
        path = json_content["root_path"]
        for name in tracks:
            self.art(name)
            
            if save_on_history:
                self.append_in_history(name) 

            if name[0] == "[": 
                path = json_content["root_path"]
                print(self.playlist_art)
                name, name = name.replace("[", ""), name.replace("]", "")
                path = path + name 
                if not verify_path.exists(path): 
                    system(f"mkdir {path}")
            
            else: 
                print(self.download_art)
                ytdl_command = f"cd {path} && youtube-dl -qx \
                        --audio-format mp3 {name}"
                system(ytdl_command)
                sleep(0.3)

class file_download:
    def __init__(self, your_file): 
        self.file = your_file 
    
    def art(self):
        pass 
    
    def main(self): 
        file_content = file_parser(self.file).main()
        download_object = download()
        download_object.main()

class file_parser:
    def __init__(self, your_file): 
        self.file = your_file 

    def art(self, name): 
        self.parse_text = ""
        self.parse_text += "[{Fore.YELLOW}*{Fore.WHITE}] PARSING: {Fore.GREEN}{name}{Fore.WHITE}"

    def main():
        file_object = open(self.file, "r")
        lines = file_object.readlines()
        valid_tracks = []
        for line in lines: 
            art(line)
            line = line.replace("\n", "")
            print(self.parse_text)
            if len(line) == 0:
                pass 
            else:
                valid_tracks.append(line)
        return valid_tracks


