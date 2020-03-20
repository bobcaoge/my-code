package command_pattern;

public class PartyCommand implements Command{
    private Command[] commands;

    public PartyCommand(Command[] commands){
        this.commands = commands;
    }
    @Override
    public void execute() {
        for (int i = 0; i < commands.length; i++) {
            commands[i].execute();
        }

    }

    @Override
    public void undo() {
        for (int i = 0; i < commands.length; i++) {
            commands[i].undo();
        }
    }
}
