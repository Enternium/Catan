# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:21:52 2024

@author: jackp
"""

import numpy as np
import pygame


class Player:
    def __init__(self, name, colour, position):
        self.name = name
        self.position = position
        
        if colour in ['Blue', 'blue', 'Bl', 'bl']:
            #self.COLOUR = (133, 180, 255)
            self.COLOUR = (0, 0, 204)
            #self.font_colour = (0,0,0)
            self.font_colour = (255,255,255)
        elif colour in ['Orange', 'orange', 'O', 'o']:
            #self.COLOUR = (230,138,0)
            self.COLOUR = (252,107,3)
            self.font_colour = (0,0,0)
        elif colour in ['White', 'white', 'W', 'w']:
            self.COLOUR = (255,255,255)
            self.font_colour = (0,0,0)
        elif colour in ['Brown', 'brown', 'Br', 'br']:
            self.COLOUR = (117,76,21)
            self.font_colour = (255,255,255)
        elif colour in ['Red', 'red', 'R', 'r']:
            self.COLOUR = (222,46,16)
            self.font_colour = (0,0,0)
        elif colour in ['Green', 'green', 'G', 'g']:
            self.COLOUR = (33,130,26)
            self.font_colour = (0,0,0)
        else:
            self.COLOUR = (255,255,255)
            self.font_colour = (0,0,0)
        
        self.wood_nums = []
        self.brick_nums = []
        self.sheep_nums = []
        self.wheat_nums = []
        self.rock_nums = []
        
        self.wood_count = 0
        self.brick_count = 0
        self.sheep_count = 0
        self.wheat_count = 0
        self.rock_count = 0
        
        self.wood_exp = 0
        self.brick_exp = 0
        self.sheep_exp = 0
        self.wheat_exp = 0
        self.rock_exp = 0
        
        self.wood_robbed = 0
        self.brick_robbed = 0
        self.sheep_robbed = 0
        self.wheat_robbed = 0
        self.rock_robbed = 0
        
        self.exp_multipliers = np.zeros(11)
        
        self.exp_multipliers[0] = 0.027777777777777800
        self.exp_multipliers[1] = 0.055555555555555600
        self.exp_multipliers[2] = 0.083333333333333300
        self.exp_multipliers[3] = 0.111111111111111000
        self.exp_multipliers[4] = 0.138888888888889000
        self.exp_multipliers[5] = 0.166666666666667000
        self.exp_multipliers[6] = 0.138888888888889000
        self.exp_multipliers[7] = 0.111111111111111000
        self.exp_multipliers[8] = 0.083333333333333300
        self.exp_multipliers[9] = 0.055555555555555600
        self.exp_multipliers[10] = 0.027777777777777800
        
        self.tab_width = 224
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.tiny_font = pygame.font.SysFont('Impact Regular', 50)
        self.baby_font = pygame.font.SysFont('Impact Regular', 26)
        
        self.name_text = self.font.render(self.name, False, self.font_colour)
        width, height = self.font.size(self.name)
        self.name_rect = (60 + (self.position + 0.5)*self.tab_width - width/2, 80, 0, 0)
        
        self.resource_texts = [self.tiny_font.render('Wood:', False, self.font_colour), self.tiny_font.render('Brick:', False, self.font_colour), self.tiny_font.render('Sheep:', False, self.font_colour), self.tiny_font.render('Wheat:', False, self.font_colour), self.tiny_font.render('Rock:', False, self.font_colour), self.tiny_font.render('Total:', False, self.font_colour)]
        self.resource_text_rects = [(60 + self.position*self.tab_width, 160), (60 + self.position*self.tab_width, 190), (60 + self.position*self.tab_width, 220), (60 + self.position*self.tab_width, 250), (60 + self.position*self.tab_width, 280), (60 + self.position*self.tab_width, 330)]
        self.resource_text_rects_2 = [(60 + self.position*self.tab_width, 380), (60 + self.position*self.tab_width, 410), (60 + self.position*self.tab_width, 440), (60 + self.position*self.tab_width, 470), (60 + self.position*self.tab_width, 500), (60 + self.position*self.tab_width, 550)]
      
        self.create_numbers()
        shift = 150
        self.resource_numbers_texts_rects = [(60 + self.position*self.tab_width + shift, 160), (60 + self.position*self.tab_width + shift, 190), (60 + self.position*self.tab_width + shift, 220), (60 + self.position*self.tab_width + shift, 250), (60 + self.position*self.tab_width + shift, 280), (60 + self.position*self.tab_width + shift, 330)]
        self.robbed_numbers_texts_rects = [(60 + self.position*self.tab_width + shift, 380), (60 + self.position*self.tab_width + shift, 410), (60 + self.position*self.tab_width + shift, 440), (60 + self.position*self.tab_width + shift, 470), (60 + self.position*self.tab_width + shift, 500), (60 + self.position*self.tab_width + shift, 550)]

        
    def create_numbers(self):
        
        total = self.wood_count + self.brick_count + self.sheep_count + self.wheat_count + self.rock_count
        self.resource_numbers_texts = [self.tiny_font.render(str(self.wood_count), False, self.font_colour), self.tiny_font.render(str(self.brick_count), False, self.font_colour), self.tiny_font.render(str(self.sheep_count), False, self.font_colour), self.tiny_font.render(str(self.wheat_count), False, self.font_colour), self.tiny_font.render(str(self.rock_count), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
        total = self.wood_robbed + self.brick_robbed + self.sheep_robbed + self.wheat_robbed + self.rock_robbed
        self.robbed_numbers_texts = [self.tiny_font.render(str(self.wood_robbed), False, self.font_colour), self.tiny_font.render(str(self.brick_robbed), False, self.font_colour), self.tiny_font.render(str(self.sheep_robbed), False, self.font_colour), self.tiny_font.render(str(self.wheat_robbed), False, self.font_colour), self.tiny_font.render(str(self.rock_robbed), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
    
    def turn(self, dice_total):
        

        for j in self.wood_nums:
            self.wood_exp += self.exp_multipliers[j-2]
        for j in self.brick_nums:
            self.brick_exp += self.exp_multipliers[j-2]
        for j in self.sheep_nums:
            self.sheep_exp += self.exp_multipliers[j-2]
        for j in self.wheat_nums:
            self.wheat_exp += self.exp_multipliers[j-2]
        for j in self.rock_nums:
            self.rock_exp += self.exp_multipliers[j-2]
        
        
        for i in range(len(self.wood_nums)):
            if self.wood_nums[i] == dice_total:
                self.wood_count += 1
                
        for i in range(len(self.brick_nums)):
            if self.brick_nums[i] == dice_total:
                self.brick_count += 1
                
        for i in range(len(self.sheep_nums)):
            if self.sheep_nums[i] == dice_total:
                self.sheep_count += 1
                
        for i in range(len(self.wheat_nums)):
            if self.wheat_nums[i] == dice_total:
                self.wheat_count += 1
                
        for i in range(len(self.rock_nums)):
            if self.rock_nums[i] == dice_total:
                self.rock_count += 1
                
        self.create_numbers()
                
    def add_resource(self, resource, number):
        
        if resource == 'wood':
            self.wood_nums.append(number)
            
        elif resource == 'brick':
            self.brick_nums.append(number)
            
        elif resource == 'sheep':
            self.sheep_nums.append(number)
            
        elif resource == 'wheat':
            self.wheat_nums.append(number)
            
        elif resource == 'rock':
            self.rock_nums.append(number)
                    
    def robbed(self, resource, amount):
        
        if resource == 'wood':
            self.wood_robbed += amount
            self.wood_count -= amount
        elif resource == 'brick':
            self.brick_robbed += amount
            self.brick_count -= amount
        elif resource == 'sheep':
            self.sheep_robbed += amount
            self.sheep_count -= amount
        elif resource == 'wheat':
            self.wheat_robbed += amount
            self.wheat_count -= amount
        elif resource == 'rock':
            self.rock_robbed += amount
            self.rock_count -= amount
    
        self.create_numbers()
        
    def click(self, mouse):
        if 60 + (self.position + 0.5)*self.tab_width - 27 < mouse[0] < 60 + (self.position + 0.5)*self.tab_width + 27:
            return self.name
        else:
            return False
            
    def draw_tab(self, surface):
        pygame.draw.rect(surface, self.COLOUR, (60 + self.position*self.tab_width, 80, self.tab_width, 600))
        surface.blit(self.name_text, self.name_rect)
        
        for i in range(len(self.resource_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects[i])
            surface.blit(self.resource_numbers_texts[i], self.resource_numbers_texts_rects[i])
            
        for i in range(len(self.robbed_numbers_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects_2[i])
            surface.blit(self.robbed_numbers_texts[i], self.robbed_numbers_texts_rects[i])
            
        

        
def get_player_info():           
    num_players = input('How many players?')
    
    if num_players == 'Default':
        players = [Player('Jack', 'Blue', 0), Player('Alex', 'Brown', 1), Player('Annie', 'Orange', 2), Player('Mark', 'White', 3)]
    else:
        players = []
        for i in range(int(num_players)):
            name = input('Input player name:')
            colour = input('Input player colour:')
            players.append(Player(name, colour, i))
        
    return players
            
          
class Player_Map_Button:
    def __init__(self, player, CONSTANTS, MAIN_TAB, position):
        self.player = player
        self.con = CONSTANTS
        self.MT = MAIN_TAB
        self.position = position
        
        self.colour = self.player.COLOUR
        self.font_colour = self.player.font_colour
        self.height = self.MT.height/6
        self.width = self.MT.width*11/48
        self.x = self.MT.x + self.MT.width - self.width
        self.y = self.MT.y + self.height*self.position
        
        self.name_text = self.player.mini_font.render(self.player.name, False, self.font_colour)
        self.name_text_rect = self.name_text.get_rect(center = (self.x + self.width/2, self.y + self.height/4))
        
        self.button_texts = [self.player.baby_font.render('Add Settlement', False, self.font_colour), self.player.baby_font.render('Add City', False, self.font_colour)]
        self.button_texts_rects = [self.button_texts[0].get_rect(center = (self.x + self.width/4, self.y + self.height*3/4)), self.button_texts[1].get_rect(center = (self.x + self.width*3/4, self.y + self.height*3/4))]
        
    def click(self, mouse):
        if self.y + self.height/2 < mouse[1] < self.y + self.height:
            if self.x < mouse[0] < self.x + self.width/2:
                return 'Settlement', self.player
            elif self.x + self.width/2 < mouse[0] < self.x + self.width:
                return 'City', self.player
            
        return False, False
    
    def draw(self, surface, player_assigner, structure_assigner):
        
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height))
        
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 2)
        
        if player_assigner == self.player and structure_assigner == 'Settlement':
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width/2, self.height/2), width = 6)
        else:
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width/2, self.height/2), width = 2)
            
        if player_assigner == self.player and structure_assigner == 'City':
            pygame.draw.rect(surface, (0,0,0), (self.x + self.width/2, self.y + self.height/2, self.width/2, self.height/2), width = 6)
        else:
            pygame.draw.rect(surface, (0,0,0), (self.x + self.width/2, self.y + self.height/2, self.width/2, self.height/2), width = 2)
            
            
        surface.blit(self.name_text, self.name_text_rect)
        
        for i in range(len(self.button_texts)):
            surface.blit(self.button_texts[i], self.button_texts_rects[i])
        
        
        
def gen_Player_Map_Button_list(player_list, CONSTANTS, MAIN_TAB):
    temp = []
    for i in range(len(player_list)):
        temp.append(Player_Map_Button(player_list[i], CONSTANTS, MAIN_TAB, i))
    return temp

class Robber_Map_Button:
    def __init__(self, CONSTANTS, MAIN_TAB):
        self.con = CONSTANTS
        self.MT = MAIN_TAB
        
        self.colour = (50,50,50)
        self.font_colour = (250,250,250)
        self.height = self.MT.height/6
        self.width = self.MT.width*11/48
        self.x = self.MT.x
        self.y = self.MT.y
        
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.baby_font = pygame.font.SysFont('Impact Regular', 26)
        
        self.name_text = self.mini_font.render('Robber', False, self.font_colour)
        self.name_text_rect = self.name_text.get_rect(center = (self.x + self.width/2, self.y + self.height/4))
        
        self.button_texts = [self.baby_font.render('Move Robber', False, self.font_colour), self.baby_font.render('Move Pirate', False, self.font_colour)]
        self.button_texts_rects = [self.button_texts[0].get_rect(center = (self.x + self.width/4, self.y + self.height*3/4)), self.button_texts[1].get_rect(center = (self.x + self.width*3/4, self.y + self.height*3/4))]
        
    def click(self, mouse):
        if self.y + self.height/2 < mouse[1] < self.y + self.height:
            if self.x < mouse[0] < self.x + self.width/2:
                return True
        else:
            return False
    
    def draw(self, surface, robber_assigner, pirate_assigner):
        
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height))
        
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 2)
        
        if robber_assigner:
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width/2, self.height/2), width = 6)
        else:
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width/2, self.height/2), width = 2)
            
        if pirate_assigner:
            pygame.draw.rect(surface, (0,0,0), (self.x + self.width/2, self.y + self.height/2, self.width/2, self.height/2), width = 6)
        else:
            pygame.draw.rect(surface, (0,0,0), (self.x + self.width/2, self.y + self.height/2, self.width/2, self.height/2), width = 2)
            
            
        surface.blit(self.name_text, self.name_text_rect)
        
        for i in range(len(self.button_texts)):
            surface.blit(self.button_texts[i], self.button_texts_rects[i])