from kivy.uix.floatlayout                      import   FloatLayout
from kivy.uix.popup                            import   Popup
from groundcontrol.ui_elements.otherFeatures                  import   OtherFeatures
from groundcontrol.ui_elements.powerFeatures                  import   PowerFeatures
from groundcontrol.data_structures.makesmithInitFuncs         import   MakesmithInitFuncs
from kivy.app                                  import   App
from groundcontrol.ui_elements.backgroundMenu                 import   BackgroundMenu
from groundcontrol.ui_elements.viewMenu import ViewMenu

class ScreenControls(FloatLayout, MakesmithInitFuncs):
    
    
    def setButtonAppearance(self):
        '''
        
        Called on creation to set up links to button background textures
        
        '''
        self.actionsBtn.btnBackground = self.data.iconPath + 'Generic.png'
        self.actionsBtn.textColor = self.data.fontColor
        self.settingsBtn.btnBackground = self.data.iconPath + 'Generic.png'
        self.settingsBtn.textColor = self.data.fontColor
        self.backgroundBtn.btnBackground = self.data.iconPath + 'Generic.png'
        self.backgroundBtn.textColor = self.data.fontColor
        self.powerBtn.btnBackground = self.data.iconPath + 'Generic.png'
        self.powerBtn.textColor = self.data.fontColor

    def openSettings(self):
        '''
        
        Open the settings panel to manually change settings
        
        '''
        
        #force the settings panel to update
        App.get_running_app().destroy_settings()
        
        #open the settings panel
        App.get_running_app().open_settings()
    
    def show_actions(self):
        '''
        
        Open A Pop-up To Allow User Actions
        
        Creates a new pop-up allows the user to do things like open a file.
        
        '''
        content = OtherFeatures()
        content.setUpData(self.data)
        content.close = self.close_actions
        self._popup = Popup(title="Actions", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()
    
    def show_power(self):
        '''
        
        Open A Pop-up To Allow Power Actions
        
        Creates a new pop-up allows the user to do things like shut down the system.
        
        '''
        content = PowerFeatures()
        content.setUpData(self.data)
        content.close = self.close_actions
        self._popup = Popup(title="Power", content=content,
                            size_hint=(0.2, 0.2))
        self._popup.open()

    def close_actions(self):
        '''
        Close pop-up
        '''
        self._popup.dismiss()
    
    def open_background(self):
        '''
        Open A Pop-up To Manage the Canvas Background
        '''
        content = BackgroundMenu(self.data)
        content.setUpData(self.data)
        content.close = self.close_actions
        self._popup = Popup(title="Background Picture", content=content,
                            size_hint=(0.5, 0.5))
        self._popup.open()
