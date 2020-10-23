from colorama import Fore as colors
class ArchiveParser:
    def __init__(self, archive):
        self.file = archive
    
    def art(self, name):
        self.obj = f"[{colors.YELLOW}*{colors.WHITE}] PARSING: {colors.GREEN}{name}{colors.WHITE}"
        self.title = f"[{colors.RED}*{colors.WHITE}] NOW PARSING FROM: {colors.GREEN}{name}{colors.WHITE}"

    def main(self): 
        file_obj = open(self.file, "r")
        file_content = file_obj.readlines()
        valid = []
        output = "" 
        for line in file_content: 
            self.art(line)
            
            if line[0] == "[": 
                output += self.title
            
            elif len(line) == 0: 
                pass
            
            else: 
                output += self.obj
                line = line.replace("\n", "")
                valid.append(line)
        print(output)
        
        return valid





