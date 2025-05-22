import wpilib
import wpilib.drive
import helperFunctions.ServoConfig as ServoConfig

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """Robot initialization function"""

        # define the servo configuration class
        Servo = ServoConfig

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
        Servo.RobotServo.CannonConfig(self, "Gun1Fill", 4, "Gun1Fire", 5) # TODO: change the ports
        # <!-- End of Gun 1 config -->
        
        # <!-- Gun 2 Config -->
        # TODO: add stuff here
        Servo.RobotServo.CannonConfig(self, "Gun2Fill", 6, "Gun2Fire", 7) # TODO: change the ports
        # <!-- End of Gun 2 config -->
        
        # <!-- Gun 3 Config -->
        # TODO: add stuff here
        Servo.RobotServo.CannonConfig(self, "Gun1Fill", 8, "Gun1Fire", 9) # TODO: change the ports
        # <!-- End of Gun 3 config -->
        
        # <!-- Gun 4 Config -->
        # TODO: add stuff here
        Servo.RobotServo.CannonConfig(self, "Gun1Fill", 10, "Gun1Fire", 11) # TODO: change the ports
        # <!-- End of Gun 4 config -->

        # <!-- Gun 5 Config -->
        # TODO: add stuff here
        Servo.RobotServo.CannonConfig(self, "Gun1Fill", 12, "Gun1Fire", 13) # TODO: change the ports
        # <!-- End of Gun 5 config -->

        # <!-- Gun 6 Config -->
        # TODO: add stuff here
        Servo.RobotServo.CannonConfig(self, "Gun1Fill", 14, "Gun1Fire", 15) # TODO: change the ports
        # <!-- End of Gun 6 config -->

    def teleopPeriodic(self):
        # set the motors to be in tank drive
        self.robotDrive.tankDrive(
            self.driverController.getLeftY(), self.driverController.getRightY()
        )

        # TODO: add gun Firing stuff after talking to doig