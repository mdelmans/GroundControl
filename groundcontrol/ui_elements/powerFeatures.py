from kivy.uix.screenmanager                 import Screen
from groundcontrol.data_structures.makesmithInitFuncs      import MakesmithInitFuncs
from subprocess import call


class PowerFeatures(Screen, MakesmithInitFuncs):
    def setUpData(self, data):
        self.data = data

    def power_off(self):
    	print("Bye")
        call("sudo shutdown -h now", shell=True)