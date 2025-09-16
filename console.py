#!/usr/bin/python3
import cmd
from models import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
    }
    storage = storage

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True
    
    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Show an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in HBNBCommand.storage.all():
                print(HBNBCommand.storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key in HBNBCommand.storage.all():
                del HBNBCommand.storage.all()[key]
                HBNBCommand.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Show all instances based on the class name"""
        args = arg.split()
        if len(args) == 0:
            print([str(obj) for key, obj in HBNBCommand.storage.all().items()])
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in HBNBCommand.storage.all().items()
                   if type(obj).__class__ == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        obj_dict = HBNBCommand.storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return

        obj = obj_dict[key]
        attr_name = args[2]
        attr_value = args[3]

        # try to cast value
        if attr_value.isdigit():
            attr_value = int(attr_value)
        else:
            try:
                attr_value = float(attr_value)
            except ValueError:
                pass  # keep as string

        if attr_name not in ["id", "created_at", "updated_at"]:
            setattr(obj, attr_name, attr_value)
            obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
