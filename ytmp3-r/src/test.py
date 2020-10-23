from base_r import * 
from os import system 

# print("## Testing selection class ##")
# s_object = selection()
# tracks = s_object.main()
# print(f"RETURNED: {tracks}")

# print("## Testing download class and history regist ##")
# d_object = download(tracks)
# d_object.main(save_on_history=True)
# print("=== BAT ===")
# system("bat ~/github/ytmp3-r/files/history.txt")
# print("=== BAT ===")

# print("## Testing download via file ##")
example_file = "[[some playlist]]\nnumber1\nnumber2\nnumber3" 
# fd_object = base.file_download(example_file)
# valid = fd_object.main()
# print(f"RETURNED: {valid}")

print("## Testing parser ##")
fp_object = file_parser(example_file)
valid = fp_object.main()
print(f"RETURNED: {valid}")
