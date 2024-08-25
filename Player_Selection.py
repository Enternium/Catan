# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:04:05 2024

@author: jackp
"""
import pygame



class Player_Button:
    def __init__(self, name, colour, font_colour, position):
        self.name = name
        self.colour = colour
        self.font_colour = font_colour
        self.position = position
        
        self.width = 360
        self.height = 400
        
        if self.position < 5:
            self.y = 50        
            self.x = 60 + self.width*self.position
        else:
            self.y = 50 + self.height
            self.x = 60 + self.width*(self.position - 5)
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.name_text = self.font.render(self.name, False, self.font_colour)
        self.name_text_rect = self.name_text.get_rect(center = (self.x + self.width/2, self.y + self.height/4))
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height/2), border_top_left_radius=5, border_top_right_radius=5)
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 2, border_radius = 5)
        surface.blit(self.name_text, self.name_text_rect)
        
        



def Run_Player_Selection(CONSTANTS):
    
    pygame.init()
    pygame.font.init()
    
    player_buttons = [Player_Button('Jack', (0, 0, 204), (255,255,255), 0),
                      Player_Button('Alex', (117,76,21), (255,255,255), 1),
                      Player_Button('Annie', (252,107,3), (0,0,0), 2),
                      Player_Button('Mark', (255,255,255), (0,0,0), 3),
                      Player_Button('Steven', (33,130,26), (0,0,0), 4),
                      Player_Button('Hillary', (222,46,16), (0,0,0), 5)]
    
    surface = pygame.display.set_mode((1920,1080)) 
    
    running = True
    
    while running:
        
        surface.fill((200, 200, 200))
        
        for button in player_buttons:
            button.draw(surface)
        
        for event in pygame.event.get(): 
          
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        pygame.display.flip() 

                
    pygame.quit()
        
Run_Player_Selection(False)