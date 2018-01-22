# Created by: Matthew Walsh
# Created on: dec 2017
# Created for: ICS3U

from scene import *
import ui

from main_menu_scene import *
from game_scene import *
import config
import time


class GameOverScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        center_of_screen = self.size/2
        self.background = SpriteNode('./assets/sprites/star_background.png',
                                     position = self.size / 2, 
                                     parent = self, 
                                     size = self.size)
        position_game_over_label = Vector2(self.size.x/2, self.size.y - 200)
        self.game_over_label = LabelNode(text = 'Planet earth was destroyed!',
                                         font = ('helvetica', 20),
                                         parent = self,
                                         position = position_game_over_label,
                                         scale = 2.00)
        return_to_menu_position = Vector2(self.size.x / 2, 250)
        self.return_to_menu_label = LabelNode(text = 'return to main menu',
                                              font = ('helvetica', 20),
                                              parent = self,
                                              position = return_to_menu_position)
        self.explosion = SpriteNode('./assets/sprites/explosion.png',
                                    parent = self,
                                    position = self.size/2)
        back_button_position = Vector2(self.size.x / 2, 125)
        self.back_button = SpriteNode('./assets/sprites/back_button.png',
                                      parent = self,
                                      position = back_button_position,
                                      scale = 0.75)
        score_label_position = Vector2(self.size.x / 2, self.size.y - 250)
        self.score_label = LabelNode(text = 'Your score was: ' + str(config.score),
                                     font = ('helvetica', 20),
                                     parent = self,
                                     position = score_label_position,
                                     scale = 2.00)
        # add background color
        
      
        
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
            
        # if back button is pressed, return to main menu scene
        if self.back_button.frame.contains_point(touch.location):
            config.main_menu = True
            self.dismiss_modal_scene()
        pass
    
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
