# Created by: Matthew Walsh
# Created on: dec 2017
# Created for: ICS3U
# main game scene where the game is played

from scene import *
import ui
from numpy import random
from game_over import *
import sound

class GameScene(Scene):
    def setup(self):
        # this method is called, when user moves to this scene
        
        # updated to not use deepcopy
        self.size_of_screen_x = self.size.x
        self.size_of_screen_y = self.size.y
        self.screen_center_x = self.size_of_screen_x/2
        self.screen_center_y = self.size_of_screen_y/2
        
        self.score_position = Vector2(self.screen_center_x, self.size_of_screen_y - 50)
        self.asteroids = []
        self.aliens = []
        self.scale_size = 0.75
        self.alien_attack_rate = 1
        self.asteroid_attack_rate = 1
        self.alien_attack_speed = 30.0
        self.asteroid_attack_speed = 30.0
        self.score = 0
        self.difficulty = 1
        
        
        # add background color
        background_position = Vector2(self.screen_center_x, 
                                      self.screen_center_y)
        self.background = SpriteNode('./assets/sprites/star_background.png',
                                        parent = self,
                                        position = background_position,
                                        size = self.size)
        
                                     
        planet_position = Vector2(self.screen_center_x, self.screen_center_y)
        self.planet = SpriteNode('./assets/sprites/asteroid.png',
                                    parent = self,
                                    position = planet_position,
                                    size = self.size/8)
        self.score_label = LabelNode(text = 'score: ' + str(self.score),
                                     font = ('helvetica', 20),
                                     parent = self,
                                     position = self.score_position)
                                    
                                    
                                       
                                       
        
    def update(self):
        # this method is called, hopefully, 60 times a second
        
        # every update, randomly check if a new alien should be created
        alien_create_chance = random.randint(1, 120)
        if alien_create_chance <= self.alien_attack_rate:
            self.add_alien()
            
        asteroid_create_chance = random.randint(1, 120)
        if asteroid_create_chance <= self.asteroid_attack_rate:
            self.add_asteroid()
            
            
        if len(self.aliens) > 0:
            #print('missile check')
            for alien in self.aliens:
               if alien.frame.intersects(self.planet.frame):
               	sound.play_effect('./assets/sounds/BarrelExploding.wav')
               	self.game_over()
        else:
            pass
            #print(len(self.aliens))
            
        if len(self.asteroids) > 0:
        	  for asteroid in self.asteroids:
        		   if asteroid.frame.intersects(self.planet.frame):
        		   	sound.play_effect('./assets/sounds/BarrelExploding.wav')
        		   	self.game_over()
               	  
        else:
        	  pass
        
        
                    
                    # since game over, move to next scene
       
    
    def touch_began(self, touch):
        # this method is called, when user touches the screen
        
        pass
    
    def touch_moved(self, touch):
        # this method is called, when user moves a finger around on the screen
        pass
    
    def touch_ended(self, touch):
        # this method is called, when user releases a finger from the screen
        
        # if start button is pressed, goto game scene
        for alien in self.aliens:
        	if alien.frame.contains_point(touch.location):
        		self.aliens.remove(alien)
        		self.score = self.score + 1
        		sound.play_effect('./assets/sounds/laser1.wav')
        		self.show_score()
        		alien.remove_from_parent()
        		
        for asteroid in self.asteroids:
        	if asteroid.frame.contains_point(touch.location):
        		self.asteroids.remove(asteroid)
        		self.score = self.score + 1
        		sound.play_effect('./assets/sounds/laser1.wav')
        		self.show_score()
        		asteroid.remove_from_parent()
    
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
    
        
    def add_alien(self):
        # add a new alien to come down
        
        alien_start_position = Vector2()
        alien_start_position.x = random.randint(0, self.size_of_screen_x)
        alien_start_y = random.randint(0, 100)
        if alien_start_y > 50:
        	alien_start_position.y = 0
        else:
        	alien_start_position.y = self.size.y
        
        
        alien_end_position = Vector2(self.screen_center_x, self.screen_center_y)
        
        
        self.aliens.append(SpriteNode('./assets/sprites/alien.png',
                             position = alien_start_position,
                             parent = self))
        
        # make missile move forward
        alienMoveAction = Action.move_to(alien_end_position.x, 
                                         alien_end_position.y, 
                                         self.alien_attack_speed,
                                         TIMING_SINODIAL)
        self.aliens[len(self.aliens)-1].run_action(alienMoveAction)
    
    def add_asteroid(self):
        # add a new alien to come down
        
        asteroid_start_position = Vector2()
        asteroid_start_position.x = random.randint(0, self.size_of_screen_x)
        asteroid_start_y = random.randint(1, 3)
        if asteroid_start_y == 1:
        	asteroid_start_position.y = 0
        else:
        	asteroid_start_position.y = self.size.y
        
        
        asteroid_end_position = Vector2(self.screen_center_x, self.screen_center_y)
        
        
        self.asteroids.append(SpriteNode('./assets/sprites/asteroid.png',
                             position = asteroid_start_position,
                             parent = self,
                             size = self.size / 8))
        
        # make missile move forward
        asteroidMoveAction = Action.move_to(asteroid_end_position.x, 
                                         asteroid_end_position.y, 
                                         self.asteroid_attack_speed,
                                         TIMING_SINODIAL)
        self.asteroids[len(self.asteroids)-1].run_action(asteroidMoveAction)
        
    def show_score(self):
    	self.score_label.remove_from_parent()
    	if self.score == 50 * self.difficulty:
      	 self.alien_attack_rate = self.alien_attack_rate * 2
      	 self.asteroid_attack_rate = self.asteroid_attack_rate * 2
      	 self.difficulty = self.difficulty + 1
    	self.score_label = LabelNode(text = 'score: ' + str(self.score),
                                     font = ('helvetica', 20),
                                     parent = self,
                                     position = self.score_position)
                                     
    def game_over(self):
    	self.alien_attack_rate = 0
    	self.asteroid_attack_rate = 0
    	for alien in self.aliens:
    		self.aliens.remove(alien)
    		alien.remove_from_parent()
    	for asteroid in self.asteroids:
    		self.asteroids.remove(asteroid)
    		asteroid.remove_from_parent()
    	self.present_modal_scene(GameOverScene())
      
      
