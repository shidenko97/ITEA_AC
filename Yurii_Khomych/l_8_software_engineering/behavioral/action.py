class Light:
    def turn_on(self):
        print("Turn on the light")

    def turn_off(self):
        print("Turn off the light")


class CommandBase:
    def execute(self):
        raise NotImplementedError()


class LightCommandBase(CommandBase):
    def __init__(self, light):
        self.light = light


class TurnOnLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_on()


class TurnOffLightCommand(LightCommandBase):
    def execute(self):
        self.light.turn_off()


class Switch:
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        self.on_cmd.execute()

    def off(self):
        self.off_cmd.execute()


light = Light()
switch = Switch(
    on_cmd=TurnOnLightCommand(light), off_cmd=TurnOffLightCommand(light)
)
switch.on()
switch.off()
