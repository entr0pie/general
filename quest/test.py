from parser import ArchiveParser
from main import SelectOption

# [TEST-PARSER]
# obj = ArchiveParser("/home/neo/github/quest/files/default.txt")
# print(f"RETURNED: {obj.main()}")

# [TEST-MAIN]
obj = SelectOption("/home/neo/github/quest/files/default.txt")
print(f"RETURNED: {obj.main()}")


