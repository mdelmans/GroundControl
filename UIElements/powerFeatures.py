from kivy.uix.screenmanager                 import Screen
from kivy.properties                        import ObjectProperty
from DataStructures.makesmithInitFuncs      import MakesmithInitFuncs
from subprocess import call


class PowerFeatures(Screen, MakesmithInitFuncs):
    def setUpData(self, data):
        self.data = data

    def power_off(self):
        call("sudo nohup shutdown -h now", shell=True)
