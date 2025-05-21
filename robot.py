import wpilib
import wpilib.drive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        # <!-- start of drivetrain config -->
        # leader motors
        # frount left is motor 3
        # frount right is motor 2
        leftfrountMotor = wpilib.PWMSparkMax(3)
        rightfrountMotor = wpilib.PWMSparkMax(2)

        # defining the follower motors
        # back left is motor 1
        # back left is motor 0
        leftFollowerMotor = wpilib.PWMSparkMax(1)
        rightFollowerMotor = wpilib.PWMSparkMax(0)

        # set the follower motors to follow the leaders
        leftfrountMotor.addFollower(leftFollowerMotor)
        rightfrountMotor.addFollower(rightFollowerMotor)

        self.robotDrive = wpilib.drive.DifferentialDrive(leftfrountMotor, rightfrountMotor)
        self.driverController = wpilib.XboxController(0)

        # we need the right or left side to be inverted 
        rightfrountMotor.setInverted(True)
        # <!-- End of Drivetrain -->

        # <!-- Gun 1 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 1 config -->
        
        # <!-- Gun 2 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 2 config -->
        
        # <!-- Gun 3 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 3 config -->
        
        # <!-- Gun 4 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 4 config -->

        # <!-- Gun 5 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 5 config -->

        # <!-- Gun 6 Config -->
        # TODO: add stuff here
        # <!-- End of Gun 6 config -->

    def teleopPeriodic(self):
        # set the motors to be in tank drive
        self.robotDrive.tankDrive(
            self.driverController.getLeftY(), self.driverController.getRightY()
        )