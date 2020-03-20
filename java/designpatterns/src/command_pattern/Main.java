package command_pattern;

import command_pattern.domain.CeilingFan;
import command_pattern.domain.GarageDoor;
import command_pattern.domain.Light;
import command_pattern.domain.Stereo;

public class Main {
    public static void main(String[] args) {
        // 创建实物对象
        Light liveRoomLight = new Light("Live Room");
        Light ckLight = new Light("ck");
        Stereo stereo = new Stereo("");
        GarageDoor garageDoor = new GarageDoor("");
        CeilingFan ceilingFan = new CeilingFan("");

        //创建实物对应的命令对象
        LightOnCommand liveRoomLightOnCommand = new LightOnCommand(liveRoomLight);
        LightOffCommand liveRoomLightOffCommand = new LightOffCommand(liveRoomLight);
        LightOnCommand ckLightOnCommand = new LightOnCommand(ckLight);
        LightOffCommand ckLightOffCommand = new LightOffCommand(ckLight);
        CeilingFanOnCommand ceilingFanOnCommand = new CeilingFanOnCommand(ceilingFan);
        CeilingFanOffCommand ceilingFanOffCommand = new CeilingFanOffCommand(ceilingFan);
        StereoOnCommand stereoOnCommand = new StereoOnCommand(stereo);
        StereoOffCommand stereoOffCommand = new StereoOffCommand(stereo);
        GarageDoorOnCommand garageDoorOnCommand = new GarageDoorOnCommand(garageDoor);
        GarageDoorOffCommand garageDoorOffCommand = new GarageDoorOffCommand(garageDoor);

        //初始化遥控器
        RemoteLoader remoteLoader = new RemoteLoader();
        remoteLoader.setCommand(0, liveRoomLightOnCommand, liveRoomLightOffCommand);
        remoteLoader.setCommand(1, ckLightOnCommand, ckLightOffCommand);
        remoteLoader.setCommand(2, ceilingFanOnCommand, ceilingFanOffCommand);
        remoteLoader.setCommand(3, stereoOnCommand, stereoOffCommand);
        remoteLoader.setCommand(4, garageDoorOnCommand, garageDoorOffCommand);

        //打印当前遥控器状态
        System.out.println(remoteLoader.toString());
        //模拟遥控器按按钮
        remoteLoader.onButtonPushed(1);
        remoteLoader.onButtonPushed(0);
        remoteLoader.onButtonPushed(3);
        remoteLoader.onButtonPushed(2);
        remoteLoader.undo();
        remoteLoader.onButtonPushed(2);

        remoteLoader.offButtonPushed(0);
        remoteLoader.undo();
        remoteLoader.offButtonPushed(3);
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();
        remoteLoader.undo();

    }
}
