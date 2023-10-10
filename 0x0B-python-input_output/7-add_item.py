#!/usr/bin/python3
"""script that adds all arguments to a Python list,
and then save them to a file"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    from sys import argv

    file_name = "add_item.json"
    my_list = load_from_json_file(file_name)
    for i in range(len(argv)):
        my_list.append(argv[i])
    save_to_json_file(my_list, file_name)
