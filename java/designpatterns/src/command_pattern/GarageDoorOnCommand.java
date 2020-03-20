package command_pattern;

import command_pattern.domain.GarageDoor;

public class GarageDoorOnCommand implements Command{
    private GarageDoor garageDoor;

    public GarageDoorOnCommand(GarageDoor garageDoor) {
        this.garageDoor = garageDoor;
    }

    @Override
    public void execute() {
        this.garageDoor.on();
    }

    @Override
    public void undo() {
        this.garageDoor.off();
    }
}
