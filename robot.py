import wpilib
import wpilib.drive


class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        leftfrountMotor = wpilib.PWMSparkMax(3)
        rightfrountMotor = wpilib.PWMSparkMax(2)

        # Adding follower motors
        leftFollowerMotor = wpilib.PWMSparkMax(1)
        rightFollowerMotor = wpilib.PWMSparkMax(0)

        # Set followers to mirror the front motors
        leftfrountMotor.addFollower(leftFollowerMotor)
        rightfrountMotor.addFollower(rightFollowerMotor)

        self.robotDrive = wpilib.drive.DifferentialDrive(leftfrountMotor, rightfrountMotor)
        self.driverController = wpilib.XboxController(0)

        # We need to invert one side of the drivetrain so that positive voltages
        # result in both sides moving forward. Depending on how your robot's
        # gearbox is constructed, you might have to invert the left side instead.
        rightfrountMotor.setInverted(True)

    def teleopPeriodic(self):
        # Drive with tank drive.
        # That means that the Y axis of the left stick moves the left side
        # of the robot forward and backward, and the Y axis of the right stick
        # moves the right side of the robot forward and backward.
        self.robotDrive.tankDrive(
            self.driverController.getLeftY(), self.driverController.getRightY()
        )