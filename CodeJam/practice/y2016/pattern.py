

class Command(object):
    pass


class Model(object):

    def execute_command(self, command):
        if command.key == "name":
            self.name = command.value
        elif command.key == "number":
            self.number = int(command.value)
        else:
            print "Invalide command"
    pass


class View(object):

    def display(self, name, number):
        LENGTH = 10
        print "*" * LENGTH
        print "Student name: %s" % name
        print "Student number: %d" % number
        print "*" * LENGTH
        return

    def keyboard_input(self):
        return raw_input("Enter command: ")


class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_view(self):
        self.view.display(self.model.name, self.model.number)
        pass

    def update_keyin(self):
        kinput = self.view.keyboard_input()
        tokens = kinput.split()

        command = Command()
        command.key = tokens[0]
        command.value = tokens[1]

        self.model.execute_command(command)
        pass


def main():
    model = Model()
    model.name = "Robert"
    model.number = 10

    view = View()
    controller = Controller(model, view)

    controller.show_view()
    controller.update_keyin()
    controller.show_view()

    pass

if __name__ == "__main__":
    main()