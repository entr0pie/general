from  colorama import Fore as colors # For Colored Text
from json import loads         # To import the config.json file 
from os import system          # To exec commands in Shell
import os.path as custom_dir   # To verify directories

class selection: 
    def art(self, counter): 
        self.input = ""
        self.input += f"[link ({colors.YELLOW}{counter}{colors.WHITE})] ~> "

    def its_done(self, track):
        if track == "exit":
            exit()
        if track == "done": 
            return True 
        return False

    def main(self): 
        tracks, counter = [], 1
        while True: 
            self.art(counter)
            track = input(self.input)
            if self.its_done(track) is True: 
                break 
            tracks.append(track)
            counter += 1
        return tracks 

json_file = open("/home/neo/github/ytmp3-r/files/config.json")
json_content = loads(json_file.read())
path = json_content["root_path"]
history = json_content["history_file"]

class download: 
    def __init__(self, tracks): 
        self.tracks = tracks 

    def art(self, name): 
        self.playlist =  f">>> {colors.RED}wild{colors.WHITE}"
        self.playlist += f" Playlist Has Appeared! {colors.GREEN}"
        self.playlist += f"Adding:{colors.WHITE} {name}"

        self.download =  f">>> [{colors.GREEN}*{colors.WHITE}]"
        self.download += f" {colors.GREEN}Downloading:{colors.WHITE} {name}"

    def append_in_history(self, name): 
        hfile = open(history, "a")
        hfile.write(f"{name}\n")

    def main(self, save_on_history=True):
        path = json_content["root_path"]
        for name in self.tracks: 
            self.art(name)
            
            if save_on_history: 
                self.append_in_history(name) 
            
            if name[0] == "[": 
                path = json_content["root_path"]
                print(self.playlist)
                path = path + name
                if not custom_dir.exists(path): 
                    system(f"mkdir {path}")
            else: 
                print(self.download)
                command = f"cd {path} && youtube-dl -qx \
                        --audio-format mp3 {name}"
                system(command)

class file_parser: 
    def __init__(self, your_file): 
        self.file = your_file 
    
    def art(self, name): 
        self.parse = f"[{colors.YELLOW}*{colors.WHITE}] \
                PARSING: {colors.GREEN}{name}{colors.WHITE}"

    def main():
        file_obj, lines = open(self.file, "r"), file_obj.readlines()
        valid_tracks = []
        for line in lines: 
            art(line)
            line = line.replace("\n", "")
            print(self.parse)
            if len(line) == 0:
                pass
            else:
                valid_tracks.append(line)
        return valid_tracks 

