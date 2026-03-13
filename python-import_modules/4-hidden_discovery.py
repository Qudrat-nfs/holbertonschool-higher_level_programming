#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    all_names = dir(hidden_4)
    for name in sorted(all_names):
        if not name.startswith("__"):
            print(name)
