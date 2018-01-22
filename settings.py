# Created by: Matthew Walsh
# Created on: dec 2017
# Created for: ICS3U

from scene import *
import ui

from main_menu_scene import *


class SettingsScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background 
        self.background = SpriteNode('./assets/sprites/star_background.png',
        	                           position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
                                     
        sound_on_position = Vector2(self.size.x * 0.33, self.size.y * 0.66)
        self.sound_on_button = LabelNode(text = 'Sound: ON',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = sound_on_position,
                                      scale = 2.00)
        sound_off_position = Vector2(self.size.x * 0.66, self.size.y * 0.66)
        self.sound_off_button = LabelNode(text = ' Sound: OFF',
                                           font = ('helvetica', 20),
                                           parent = self,
                                           position = sound_off_position,
                                           scale = 2.00)
        #credits
        credit1_position = Vector2(self.size.x / 2, self.size.y / 2)
        self.credit1 = LabelNode(text = 'explosion sprite: Gussprint',
                                 font = ('helvetica', 20),
                                 parent = self,
                                 position = credit1_position,
                                 scale = 1.00)
        back_button_position = self.size
        back_button_position.x = 100
        back_button_position.y = back_button_position.y - 100
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                       parent = self,
                                       position = back_button_position)
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        pass
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto main menu scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
        # toggle sound om
        if self.sound_on_button.frame.contains_point(touch.location):
            config.sound = True
        # toggle sound off
        if self.sound_off_button.frame.contains_point(touch.location):
            config.sound = False
    
    def did_change_size(self):
        # this method is called, when user changes the orientation of the screen
        # thus changing the size of each dimension
        pass
    
    def pause(self):
        # this method is called, when user touches the home button
        # save anything before app is put to background
        pass
    
    def resume(self):
        # this method is called, when user place app from background 
        # back into use. Reload anything you might need.
        pass
