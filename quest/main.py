from parser import ArchiveParser
from colorama import Fore as colors

class SelectOption:
    def __init__(self, archive):
        self.file = archive

    def art(self, name="none", index="none", _type="none"):
        self.to_do =  f"> [{colors.YELLOW}{index}{colors.WHITE}] {name}"
        self.done = f"> [{colors.YELLOW}{index}{colors.WHITE}] "
        self.done += f"{colors.GREEN}{name}{colors.WHITE}"
        self.type = f"{colors.MAGENTA}>>>{colors.WHITE} TYPE: {_type}"
        self.input = f"{colors.MAGENTA}(?) > {colors.WHITE} "

    def main(self):
        parser = ArchiveParser(self.file)
        to_do = parser.main()
        done = []
       
        while True: 
            self.art(_type="TO-DO")
            print(self.type)
            for task_number in range(len(to_do)):
                self.art(name=to_do[task_number], index=task_number)
                print(self.to_do)
        
            self.art(_type="DONE")
            print(self.type)
            for task_number in range(len(done)):
                self.art(name=done[task_number], index=task_number)
                print(self.done)

            self.art()
            index = input(self.input)
            if index == "done" or len(to_do) == 0:
                break 
            done.append(to_do[int(index)])
            to_do.pop(int(index))

        return to_do



