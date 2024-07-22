# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 13:28:12 2024

@author: jackp
"""

import pygame
import numpy as np
import Player_Analysis as PA


# GitHub Test

class Tab:
    def __init__(self, CONSTANTS):
        self.width = CONSTANTS['Width']*0.95 - 24
        self.height = 600
        self.x = 60
        self.y = CONSTANTS['Height']/2 - self.height/2 - 100
        
        
    def draw(self, surface):
        pygame.draw.rect(surface, (220, 220, 220), (self.x, self.y, self.width, self.height))
        

class Buttons:
    def __init__(self, CONSTANTS):
        
        self.con = CONSTANTS
        
        self.tot_width = self.con['Width']*0.9
        self.height = self.con['Height']*0.2
        self.x = self.con['Width']/2 - self.tot_width/2
        
        self.ind_width = self.tot_width/11
        
        self.col = (120,230,100)
        self.col = (100,100,130)
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.tiny_font = pygame.font.SysFont('Impact Regular', 40)
        
        self.count = [0,0,0,0,0,0,0,0,0,0,0]
        
        self.log = []
        
        self.button_colours = []
        self.button_rects = []
        for i in range(11):
            self.button_rects.append((self.x + (self.ind_width+2)*i, self.con['Height']*0.75, self.ind_width, self.height))
            self.button_colours.append(0)
        
        self.nums = []
        self.nums_rects = []
        self.nums_rects_bars = []
        
        for i in range(2,13):
            self.nums.append(self.font.render(str(i), False, (0,0,0)))
            self.nums_rects.append(self.nums[-1].get_rect(center=(self.x + (self.ind_width+2)*(i-2) + self.ind_width/2, self.con['Height']*0.75 + self.height*3/8)))
            self.nums_rects_bars.append(self.nums[-1].get_rect(center=(self.x + (self.ind_width+2)*(i-2) + self.ind_width/2, self.con['Height']/2 + 150)))
            
        self.percentages = []
        self.percentages_texts = []
        self.percentages_texts_rects = []        
        
        self.calc_exp()
        self.chunk = 0
        
        
    def click(self, mouse_pos):
        
        number = False
        
        for i in range(11):
            if self.x + (self.ind_width+2)*i < mouse_pos[0] < self.x + (self.ind_width+2)*(i + 1):
                if self.con['Height']*0.75 < mouse_pos[1] < self.con['Height']*0.75 + self.height:
                    self.count[i] += 1
                    self.log.append(i+2)
                    number = i + 2
                    break
        
        if number:
            self.calc_exp()
            
            max_val = max(max(self.count), max(self.expected_values)) # 450
            
            if max_val == 0:
                self.chunk = 0
            else:
                self.chunk = 450/max_val
        
        return number
        
    
    def remove_last(self):
        
        if len(self.log) > 0:
            value = self.log[-1]
            del self.log[-1]
            self.count[value-2] -= 1
            
            self.calc_exp()
    
    
    def calc_exp(self):
                        
        tot = sum(self.count)
        
        numerators = [1,2,3,4,5,6,5,4,3,2,1]
        
        self.expected_values = []
        for i in range(11):
            self.expected_values.append(tot * (numerators[i]/36))
        
        self.calc_percentages()
        
        
    def calc_percentages(self):
        
        self.percentages = []
        self.percentages_texts = []
        self.percentages_texts_rects = [] 
        
        for i in range(11):
            
            # Calculate percentages
            if self.expected_values[i] == 0:
                self.percentages.append(0)
            else:
                self.percentages.append(((self.count[i] - self.expected_values[i])/self.expected_values[i])*100)
                
            if self.percentages[-1] > 0:
                self.percentages_texts.append(self.tiny_font.render(f'+{str(round(self.percentages[i]))}%', False, (0,0,0)))
            else:
                self.percentages_texts.append(self.tiny_font.render(f'{str(round(self.percentages[i]))}%', False, (0,0,0)))
            
            self.percentages_texts_rects.append(self.percentages_texts[i].get_rect(center = (self.x + (self.ind_width+2)*(i) + self.ind_width/2, self.con['Height']*0.75 + self.height*8/9)))

        self.set_colours()
        
    
    def set_colours(self):
        
        maximum = max(self.percentages)
        minimum = min(self.percentages)
        
        for i in range(11):
            
            if self.percentages[i] == maximum:
                if maximum > 0:
                    self.button_colours[i] = (0,255,0)
                else:
                    self.button_colours[i] = (255,191,0)
            elif self.percentages[i] == minimum:
                if minimum > -100:
                    self.button_colours[i] = (255,0,0)
                else:
                    self.button_colours[i] = (100,100,100)
            elif self.percentages[i] > 0:
                self.button_colours[i] = (0,150,100)
            elif self.percentages[i] == -100:
                self.button_colours[i] = (100,100,100)
            elif self.percentages[i] < 0:
                self.button_colours[i] = (180,50,50)
            elif self.percentages[i] == 0:
                self.button_colours[i] = (255,191,0)
            
    
    def draw(self, surface, running):
        
        for i in range(11):
            
            x = self.x + (self.ind_width+2)*i
            
            # BUTTONS
            pygame.draw.rect(surface, self.button_colours[i], self.button_rects[i])
            
            # NUMBERS (BUTTONS)
            surface.blit(self.nums[i], self.nums_rects[i])
                                                                     
                                                                   
            text = self.mini_font.render(str(self.count[i]), False, (0,0,0))
            rect = text.get_rect(center = (self.x + (self.ind_width+2)*(i) + self.ind_width/2, self.con['Height']*0.75 + self.height*2/3))
            surface.blit(text, rect)
            # Percentages
            surface.blit(self.percentages_texts[i], self.percentages_texts_rects[i])
            
            if running == 'DAS':
                # BARS -----------------------
                pygame.draw.rect(surface, self.col, (x, self.con['Height']/2 + 150 - self.count[i]*self.chunk, self.ind_width, self.count[i]*self.chunk))
                pygame.draw.circle(surface, (0,0,0), (x + self.ind_width/2, self.con['Height']/2 + 150 - self.expected_values[i]*self.chunk), 5)
                surface.blit(self.nums[i], self.nums_rects_bars[i])
            
        # PRINT LOG ----------------------
        
        if len(self.log) > 0:
            for i in range(len(self.log)):
                if i < 19:
                    text = self.mini_font.render(str(self.log[-i-1]), False, (0,0,0))
                    rect = (0,i*50,0,0)
                    surface.blit(text, rect)
                    
                    
        # PRINT TOTAL --------------------
        
        pygame.draw.rect(surface, (255, 255, 255), (self.con['Width'] - 550, 10, 500, 60))
        total_text = self.mini_font.render('TOTAL ROLLS:', False, (0,0,0))
        total_num = self.mini_font.render(str(len(self.log)), False, (0,0,0))
        surface.blit(total_text,(self.con['Width'] - 540, 22,0,0))
        surface.blit(total_num,(self.con['Width'] - 150, 22,0,0))
        




class Menu_Buttons:
    def __init__(self, CONSTANTS):
        self.con = CONSTANTS
        
        self.x = 60
        self.y = 10
        self.width = 266
        self.height = 60
        
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.texts = [self.mini_font.render('Short Term', False, (0,0,0)), self.mini_font.render('Long Term', False, (0,0,0)), self.mini_font.render('Player', False, (0,0,0))]

    def check_button_colour(self, running):
        if running == 'DAS':
            self.colours = [(150,150,150), (255,255,255), (255,255,255)]
        elif running == 'Historical':
            self.colours = [(255,255,255), (150,150,150), (255,255,255)]
        elif running == 'PAS':
            self.colours = [(255,255,255), (255,255,255), (150,150,150)]
        else:
            self.colours = [(255,255,255), (255,255,255), (255,255,255)]
            
    def click(self, mouse_pos, running):
        outcomes = ['DAS', 'Historical', 'PAS']
        
        if self.y < mouse[1] < self.y + self.height:
            for i in [0,1,2]:
                if self.x + i*self.width + i*3 < mouse[0] < self.x + (i+1)* self.width + i*3:
                    return outcomes[i]
                
        return running
        
    def draw(self, surface, running):
        
        self.check_button_colour(running)
        
        for i in [0,1,2]:
            pygame.draw.rect(surface, self.colours[i], (self.x + i*self.width + i*3, self.y, self.width, self.height))
            surface.blit(self.texts[i], (self.x + i*self.width + i*3, self.y+10, self.width, self.height))
        


pygame.init()
pygame.font.init()

players = PA.get_player_info()

#surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
surface = pygame.display.set_mode((1440,960)) 
  
pygame.display.set_caption('Catan Data') 

CONSTANTS = {}

CONSTANTS['Width'], CONSTANTS['Height'] = pygame.display.get_surface().get_size()
CONSTANTS['Players'] = players


BUTTONS = Buttons(CONSTANTS)
MENU = Menu_Buttons(CONSTANTS)
MAIN_TAB = Tab(CONSTANTS)

# Variable to keep our game loop running 
running = 'DAS'
  
# game loop 
while running: 
    
    surface.fill((200, 200, 200)) 
    
    MAIN_TAB.draw(surface)
    BUTTONS.draw(surface, running)
    MENU.draw(surface, running)
    
    if running == 'PAS':
        for player in CONSTANTS['Players']:
            player.draw_tab(surface)
            
    elif running == 'ADD_1':
        adding_tab.draw(surface)
        
    elif running == 'Robber':
        for player in CONSTANTS['Players']:
            player.draw_robber(surface)
    
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            elif event.key == pygame.K_BACKSPACE:
                BUTTONS.remove_last()
                
            elif event.key == pygame.K_r:
                running = 'Robber'
                
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            
            if mouse[1] < 75:
                running = MENU.click(mouse, running)
                
            elif mouse[1] > CONSTANTS['Height']*0.75:
                number = BUTTONS.click(mouse)
                if number:
                    for player in CONSTANTS['Players']:
                        player.turn(number)
                
            elif running == 'PAS':
                if 573 < mouse[1] < 627:
                    for player in CONSTANTS['Players']:
                        name = player.click(mouse)
                        if name:
                            adding_tab = PA.Adding_Tab(CONSTANTS)
                            running = 'ADD_1'
                            break
            
            elif running == 'ADD_1':
                returned = adding_tab.click(mouse)
                
                if returned:
                    for player in CONSTANTS['Players']:
                        if player.name == name:
                            for i in range(3):
                                if returned[0][i] != 0:
                                    player.add_resource(returned[1][i], returned[0][i])
                                    
                    running = 'PAS'
                
                
    
    pygame.display.flip() 

            
pygame.quit()