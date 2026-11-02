# Lab 2 - runs the code part of the lab task (smart classroom agent)
import platform

from src import lab2_check, lab2_percepts


def main():
    print("AI Lab 2: Intelligent Agents & the PEAS Framework | Mohammed Emad ALaini")
    print("Python %s, standard library only" % platform.python_version())
    print()
    lab2_percepts.main()
    print()
    lab2_check.main()


if __name__ == "__main__":
    main()
