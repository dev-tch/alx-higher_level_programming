#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names_of_compiled_file = dir(hidden_4)
    for item in names_of_compiled_file:
        if item[:2] != "__":
            print(item)
