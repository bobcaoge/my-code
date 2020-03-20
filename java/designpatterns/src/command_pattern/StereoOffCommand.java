package command_pattern;

import command_pattern.domain.Stereo;

public class StereoOffCommand implements Command{
    private Stereo stereo;

    public StereoOffCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    @Override
    public void execute() {
        this.stereo.off();
    }

    @Override
    public void undo(){
        this.stereo.on();

    }
}
