package command_pattern;

public class NoCommand implements Command{
    @Override
    public void execute() {
        System.out.println("there is nothing to execute this command!");
    }

    @Override
    public void undo() {
        System.out.println("there is nothing to execute this command!");
    }
}
