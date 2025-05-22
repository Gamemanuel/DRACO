import wpilib

class RobotServo():
    def CannonConfig(self, nameOfFillServo: str, FillServoPort: int, nameOfFiringServo: str, FiringServoPort: int):
        nameOfFillServo = wpilib.Servo(FillServoPort) # TODO: change this port
        nameOfFiringServo = wpilib.Servo(FiringServoPort) # TODO: change this port
        nameOfFillServo.setAngle(90)
        nameOfFiringServo.setAngle(90)

    # TODO: add more stuff here