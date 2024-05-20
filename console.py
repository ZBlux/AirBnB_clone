#!/usr/bin/python3
"""the console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


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

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        cls = classes[class_name]
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on the class name and id
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of
            all instances based or not on the class name
        """
        args = arg.split()
        if args and args[0] not in classes:
            print("** class doesn't exist **")
            return
        objects = []
        for obj in storage.all().values():
            if not args or args[0] == obj.__class__.__name__:
                objects.append(str(obj))
        print(objects)

    def do_update(self, arg):
        """Updates an instance based on the class name
            and id by adding or updating attribute
        """
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = ' '.join(args[3:]).strip('\"')

        try:
            cast_value = eval(attr_value)
        except (ValueError, SyntaxError, NameError):
            cast_value = attr_value

        setattr(obj, attr_name, cast_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
