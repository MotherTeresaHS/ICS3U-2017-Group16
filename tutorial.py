# Created by: Matthew Walsh
# Created on: dec 2017
# Created for: ICS3U

from scene import *
import ui

from main_menu_scene import *


class TutorialScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        center_of_screen = self.size/2
        
        # add background color
        self.background = SpriteNode(position = self.size / 2, 
                                     color = 'blue', 
                                     parent = self, 
                                     size = self.size)
        instruction_position = Vector2(self.size.x / 2, self.size.y - 250)
        self.instructions = LabelNode(text = 'Planet Earth is under attack by aliens.' + '\n' + 'Also to make things worse there are a ' + '\n' + 'large number of asteroids on collision course with earth.' + '\n' + 'Your job is to defend planet earth,' + '\n' + 'destroy the attackers by tapping them with your finger.',
                                      font=('Helvetica', 20),
                                      parent = self,
                                      position = instruction_position,
                                      scale = 1.50)
        asteroid_label_position = Vector2(self.size.x * 0.66, 200)
        self.asteroid_label = LabelNode(text = 'Asteroid',
                                        font = ('Helvetica', 20),
                                        parent = self,
                                        position = asteroid_label_position,
                                        scale = 1.50)
        alien_label_position = Vector2(self.size.x * 0.33, 200)
        self.alien_label = LabelNode(text = 'Alien',
                                     font = ('Helvetica', 20),
                                     parent = self,
                                     position = alien_label_position,
                                     scale = 1.50)
        asteroid_position = Vector2(self.size.x * 0.66, 100)
        self.asteroid = SpriteNode('./assets/sprites/asteroid.png',
                             position = asteroid_position,
                             parent = self,
                             size = self.size / 8)
        alien_position = Vector2(self.size.x * 0.33, 100)
        self.alien = SpriteNode('./assets/sprites/alien.png',
                             position = alien_position,
                             parent = self)
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
        
        # if start button is pressed, goto game scene
        if self.back_button.frame.contains_point(touch.location):
            self.dismiss_modal_scene()
    
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
