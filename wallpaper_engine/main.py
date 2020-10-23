from json import loads 
from os import system 
from time import sleep
config_file = open("config.json", "r")
config_file = config_file.read()
json_content = loads(config_file)

fps = json_content["frames_per_second"]
tf = json_content["total_frames"]
path = json_content["path"]
name = json_content["wallpaper_name"]
ext = json_content["extension"]

while True: 
    for frame in range(tf):
        command = f"feh --bg-scale {path}{name}{frame}{ext}"
        system(command)
        sleep(1 / fps)
