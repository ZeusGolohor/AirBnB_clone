#!/usr/bin/python3
"""
This module is used to create a command-line
entry point into the program.
"""
import cmd
import re
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class is used to create a commmad-line
    entry point into the program.
    """
    prompt = "(hbnb) "
    dictOfClasses = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def check_class(self, line):
        """
        A ethod used to check if a class name exist
        or is missing.
        """
        line = line.split()
        if (len(line) >= 1):
            if (line[0] in self.dictOfClasses):
                return (True)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return (False)

    def check_class_n_id(self, line):
        if (self.check_class(line) is True):
            line = line.split()
            if (len(line) >= 2):
                search_str = "{}.{}".format(line[0], line[1])
                if (search_str in storage._FileStorage__objects):
                    return (True)
                else:
                    print("** no instance found **")
            elif (len(line) == 1):
                print("** instance id missing **")

    def check_storage(self, line):
        """
        A method used to check storage for an entry.
        """
        line = line.split()
        search_str = "{}.{}".format(line[0], line[1])
        if (search_str in storage._FileStorage__objects):
            return (storage._FileStorage__objects[search_str])
        else:
            return (None)

    def do_EOF(self, line):
        """
        This method is used to handle an
        empty line passed to the program
        """
        return (True)

    def help_EOF(self):
        """
        This method print a string when
        the help EOF command is entered.
        """
        print(
            "This method is used to handle an " +
            "empty  line passed to the program."
        )
        print()

    def do_quit(self, line):
        """
        A method to exit the program.
        """
        return (True)

    def help_quit(self):
        """
        This method is used to print a string when the
        command help quit is entered.
        """
        print("Quit command to exit the program")
        print()

    def emptyline(self):
        """
        This method handles an empty line.
        """
        pass

    def do_create(self, line):
        """
        This method is used to create a new
        instance.
        """
        if (self.check_class(line) is True):
            line = line.split()
            className = self.dictOfClasses[line[0]]
            instance = className()
            instance.save()
            print(instance.id)

    def help_create(self):
        """
        This method is used to print an help message
        whne help create is typed into the terminal.
        """
        print("This command is used to create a new instance of a class")
        print("Usage: {}create className".format(self.prompt))
        print()

    def do_show(self, line):
        """
        This method is used to print the string representation of an
        instance.
        """
        if (self.check_class_n_id(line) is True):
            obj = self.check_storage(line)
            if (obj is not None):
                line = line.split()
                class_name = self.dictOfClasses[line[0]]
                instance = class_name(**obj)
                print(instance)

    def help_show(self):
        """
        This method is used to show a help message for the show
        command.
        """
        print("This command prints the string representation of an instance.")
        print("Usage: {}create ClassName id".format(self.prompt))
        print()

    def do_destroy(self, line):
        """
        This method is used to delete an instance.
        """
        if (self.check_class_n_id(line) is True):
            line = line.split()
            search_str = "{}.{}".format(line[0], line[1])
            del (storage._FileStorage__objects[search_str])

    def help_destroy(self):
        """
        A method used to display a message when the command
        help destroy is entered.
        """
        print("This command is used to destroy an instance of a class")
        print("Usage: {}destroy ClassName id".format(self.prompt))
        print()

    def do_all(self, line):
        """
        A method to print all instance of a class or all
        classes.
        """
        """
        line1 = line
        line1 = line.split()
        allClassIns = []
        objs = storage._FileStorage__objects
        if (len(line1) == 0):
            for key, value in objs.items():
                if self.dictOfClasses[value["__class__"]]:
                    className = self.dictOfClasses[value["__class__"]]
                    instance = className(**value)
                    allClassIns.append(str(instance))
            print(allClassIns)
        else:
            if (self.check_class(line) is True):
                for key, value in objs.items():
                    if (line1[0] == value["__class__"]):
                        className = self.dictOfClasses[line1[0]]
                        instance = className(**value)
                        allClassIns.append(str(instance))
                print(allClassIns)
        """
        line1 = line.split()
        allClassIns = []
        objs = storage._FileStorage__objects
        if (len(line1) == 0):
            for key, value in objs.items():
                if (value["__class__"] in self.dictOfClasses.keys()):
                    className = self.dictOfClasses[value["__class__"]]
                    instance = className(**value)
                    allClassIns.append(str(instance))

            if (len(allClassIns) > 0):
                print(allClassIns)
            elif (len(allClassIns) == 0):
                print("** no instance found **")
        else:
            if (len(line1) > 1):
                print("*** Unknown syntax: {}".format(line))
                print("Usage: {}all {}".format(self.prompt), line1[0])
            elif (self.check_class(line) is True):
                for key, value in objs.items():
                    if (value["__class__"] == line1[0]):
                        if (value["__class__"] in self.dictOfClasses.keys()):
                            className = self.dictOfClasses[value["__class__"]]
                            instance = className(**value)
                            allClassIns.append(str(instance))

                if (len(allClassIns) > 0):
                    print(allClassIns)
                elif (len(allClassIns) == 0):
                    print("** no instance found **")

    def help_all(self):
        """
        A method method to print a help message for the all
        command.
        """
        print(
            "This command is used to print all instances of a class " +
            "or all classes")
        print("Usage: {}all".format(self.prompt))
        print("Usage: {}all ClassName".format(self.prompt))
        print()

    def do_update(self, line):
        """
        This method is used to add or update an instance based on
        class name and id.
        """
        if (self.check_class_n_id(line) is True):
            line1 = line.replace('"', "")
            line1 = line1.split()
            if (len(line1) >= 3):
                if (len(line1) >= 4):
                    obj = self.check_storage(line)
                    if (obj is not None):
                        search_str = "{}.{}".format(line1[0], line1[1])
                        store = storage._FileStorage__objects
                        if (self.check_class(line) is True):
                            className = self.dictOfClasses[line1[0]]
                            instance = className(**store[search_str])
                            setattr(instance, line1[2], line1[3])
                            instance.save()
                else:
                    print("** value missing **")
            else:
                print("** attribute name missing ** ")

    def help_update(self):
        """
        This method is used to print an help message when the help command
        is entered.
        """
        print("This command is used to add or update an instance")
        print(
            "Usage: {}update <class name> <id> ".format(self.prompt) +
            "<attribute name> '<attribute value>'"
            .format(self.prompt)
        )
        print()

    def check_braks_all(self, line):
        """
        A method to check for l().
        """
        if (line[-3:] == "l()"):
            return (True)
        else:
            print("*** Unknown syntax: {}".format(line))

    def User_all(self, line):
        """
        A method used to handle the User.all() cmd command.
        used to print all users instances.
        """
        if (self.check_braks_all(line) is True):
            self.do_all("User")

    def BaseModel_all(self, line):
        """
        A method used to handle the BaseModel.all() cmd
        command used to print all BaseModel Instances.
        """
        if (self.check_braks_all(line) is True):
            self.do_all("BaseModel")

    def State_all(self, line):
        """
        A method used to handle the State.all() cmd
        command used to print all state Instances.
        """
        if (self.check_braks_all(line) is True):
            self.do_all("State")

    def User_count(self, line):
        """
        A method to print total number of User instance(s).
        """
        ins = 0
        store = storage._FileStorage__objects
        for key, value in store.items():
            if (value["__class__"] == "User"):
                ins = ins + 1
        print(ins)

    def default(self, line):
        """
        This method is used to handle complex commands.
        """
        dictOfMethods = {
            "User.all": self.User_all,
            "BaseModel.all": self.BaseModel_all,
            "State.all": self.State_all,
            "User.count": self.User_count
        }
        try:
            ptn = "[A-Za-z]{1,}.[a-z]{1,}(.)"
            cmmd = re.match(ptn, line).group(0)
        except AttributeError:
            print("*** Unknown syntax: {}".format(line))
        else:
            if (line[-1:] != ')'):
                print("*** Unknown syntax: {}".format(line))
            else:
                cmmd = cmmd[:-1]
                try:
                    func = dictOfMethods[cmmd]
                except KeyError:
                    print("** class doesn't exist **")
                else:
                    func(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
