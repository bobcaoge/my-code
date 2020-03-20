package command_pattern;

import command_pattern.domain.GarageDoor;

public class GarageDoorOffCommand implements Command{
    private GarageDoor garageDoor;

    public GarageDoorOffCommand(GarageDoor garageDoor) {
        this.garageDoor = garageDoor;
    }

    @Override
    public void execute() {
        this.garageDoor.off();
    }

    @Override
    public void undo() {
        this.garageDoor.on();
    }
}
