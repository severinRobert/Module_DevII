

class Command:
    def __init__(self, command: list) -> None:
        self.command = self.clean_command(command)
        self.name = self.command[0]
        self.arguments = self.command[1:]
        
    
    def clean_command(self, command: list):
        new_command = []
        for i in command:
            if i != "":
                new_command.append(i)
        return new_command
    
    

    