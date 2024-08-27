# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:04:05 2024

@author: jackp
"""
import pygame
from Player_Analysis import Player


class Player_Button:
    def __init__(self, name, colour, position, ticked):
        self.name = name
        self.position = position
        self.colour_text = colour
        self.ticked = ticked
        
        if colour in ['Blue', 'blue', 'Bl', 'bl']:
            self.colour = (0, 0, 204)
            self.font_colour = (255,255,255)
        elif colour in ['Orange', 'orange', 'O', 'o']:
            self.colour = (252,107,3)
            self.font_colour = (0,0,0)
        elif colour in ['White', 'white', 'W', 'w']:
            self.colour = (255,255,255)
            self.font_colour = (0,0,0)
        elif colour in ['Brown', 'brown', 'Br', 'br']:
            self.colour = (117,76,21)
            self.font_colour = (255,255,255)
        elif colour in ['Red', 'red', 'R', 'r']:
            self.colour = (222,46,16)
            self.font_colour = (0,0,0)
        elif colour in ['Green', 'green', 'G', 'g']:
            self.colour = (33,130,26)
            self.font_colour = (0,0,0)
        else:
            self.colour = (255,255,255)
            self.font_colour = (0,0,0)
        
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
        
        self.tickbox_width = self.width/6
        self.tickbox_height = self.tickbox_width
        
        self.tickbox_x = self.x + self.width/2 - self.tickbox_width/2
        self.tickbox_y = self.y + self.height*4/5
        
        self.tick_coordinates = [self.x + self.width/2, self.y + self.height*4/5 + self.tickbox_height/2]
        
        
    def click(self, mouse):
        
        if self.tickbox_x < mouse[0] < self.tickbox_x + self.tickbox_width:
            if self.tickbox_y < mouse[1] < self.tickbox_y + self.tickbox_height:
                if self.ticked:
                    self.ticked = False
                else:
                    self.ticked = True
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height/2), border_top_left_radius=5, border_top_right_radius=5)
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 2, border_radius = 5)
        surface.blit(self.name_text, self.name_text_rect)
        
        pygame.draw.rect(surface, (0,0,0), (self.tickbox_x, self.tickbox_y, self.tickbox_width, self.tickbox_height), width = 2, border_radius = 5)
        
        if self.ticked:
            pygame.draw.circle(surface, (0,0,0), self.tick_coordinates, self.tickbox_width/2 - 1)
        
        
class Go_Button:
    def __init__(self):
        self.width = 600
        self.height = 140
        
        self.x = 960 - self.width/2
        self.y = 1040 - self.height
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.name_text = self.font.render('Continue', False, (0,0,0))
        self.name_text_rect = self.name_text.get_rect(center = (self.x + self.width/2, self.y + self.height/2))
        
    def click(self, mouse):
        if self.x < mouse[0] < self.x + self.width:
            if self.y < mouse[1] < self.y + self.height:
                return False
            
        return True
        
    def draw(self, surface):
        pygame.draw.rect(surface, (100,255,100), (self.x, self.y, self.width, self.height), border_radius = 10)
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 5, border_radius = 10)
        surface.blit(self.name_text, self.name_text_rect)


def Run_Player_Selection():
    
    pygame.init()
    pygame.font.init()
        
    player_buttons = [Player_Button('Jack', 'Blue', 0, True),
                      Player_Button('Alex', 'Brown', 1, True),
                      Player_Button('Annie', 'Orange', 2, True),
                      Player_Button('Mark', 'White', 3, True),
                      Player_Button('Steven', 'Green', 4, False),
                      Player_Button('Hillary', 'Red', 5, False)]
    
    go_button = Go_Button()
    
    surface = pygame.display.set_mode((1920,1080)) 
    
    running = True
    
    while running:
        
        surface.fill((200, 200, 200))
        
        for button in player_buttons:
            button.draw(surface)
        go_button.draw(surface)
        
        for event in pygame.event.get(): 
          
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for button in player_buttons:
                    button.click(mouse)
                running = go_button.click(mouse)
                
                    
        pygame.display.flip() 

    
    count = 0
    for button in player_buttons:
        if button.ticked:
            count += 1

    if count <= 4:
        game_mode = 4
    else:
        game_mode = 6

    player_list = []
    for button in player_buttons:
        if button.ticked:
            player_list.append(Player(button.name, button.colour_text, len(player_list), mode = game_mode))
            
    pygame.display.quit()
    
    return player_list

