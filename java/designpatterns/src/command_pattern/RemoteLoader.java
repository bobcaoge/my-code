package command_pattern;

import java.util.Stack;

public class RemoteLoader {
    Command[] onCommand;
    Command[] offCommand;
    Stack<Command> executedCommands;
    public RemoteLoader(){
        this.onCommand = new Command[7];
        this.offCommand = new Command[7];
        this.executedCommands = new Stack<>();
        NoCommand noCommand = new NoCommand();
        for (int i = 0; i < onCommand.length; i++) {
            this.onCommand[i] = noCommand;
            this.offCommand[i] = noCommand;
        }
    }
    public void setCommand(int slot, Command onCommand, Command offCommand){
        this.onCommand[slot] = onCommand;
        this.offCommand[slot] = offCommand;
    }
    public void onButtonPushed(int slot){
        this.onCommand[slot].execute();
        this.executedCommands.push(this.onCommand[slot]);
    }

    public void offButtonPushed(int slot){
        this.offCommand[slot].execute();
        this.executedCommands.push(this.offCommand[slot]);
    }
    public void undo(){
        if (!this.executedCommands.empty()){
            this.executedCommands.pop().undo();
        }
    }

    @Override
    public String toString() {
        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < this.onCommand.length; i++) {
            sb.append("[slot"+i+"] "+onCommand[i].getClass().getName()+"\t"+offCommand[i].getClass().getName()+"\n");

        }
        return sb.toString();
    }
}
