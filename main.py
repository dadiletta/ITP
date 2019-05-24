# BUILD USING PYTHON 3

from ancestor import MrA
import logging


class Robot(MrA):
    """
    Our final project class. This inherits from Mr. A's starter which inherts from the
    GoPiGo3 class.
    """

    def __init__(self):
        """
        Constructor; our place to setup instance variables
        """
        super().__init__()  

        # run the menu loop
        self.menu()

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like to add an experimental method
        menu = {
                "s": ("Check status", self.status),
                "q": ("Quit", quit_now)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    def status(self):
        self.dist()
        self.angle()


#####################################################################
## FUNCTIONS are methods that float in the module (not in a class)

def error():
    """records general, less specific error"""
    logging.error("ERROR")
    print('ERROR')

def quit_now():
    """shuts down app"""
    raise SystemExit

# SETUP LOGGING TO HELP TRACK ERRORS
LOG_LEVEL = logging.INFO
LOG_FILE = "/home/pi/PnR-Final/log_robot.log"  # don't forget to make this file!
LOG_FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(filename=LOG_FILE, format=LOG_FORMAT, level=LOG_LEVEL)

# this is where the robot is instantiated. Our whole app is basicly this one line
if __name__ == "__main__":
    r = Robot()