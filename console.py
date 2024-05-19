#!/usr/bin/python3
"""the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter Hbnb
    Attributes:
        prompt : the command prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """ do nothing on empty input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
