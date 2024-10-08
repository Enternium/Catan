# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 10:21:52 2024

@author: jackp
"""

import numpy as np
import pygame


class Player:
    def __init__(self, name, colour, position, mode):
        self.name = name
        self.position = position
        self.mode = mode
        
        if colour in ['Blue', 'blue', 'Bl', 'bl']:
            self.COLOUR = (0, 0, 204)
            self.font_colour = (255,255,255)
        elif colour in ['Orange', 'orange', 'O', 'o']:
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
        self.gold_nums = []
        
        self.wood_count = 0
        self.brick_count = 0
        self.sheep_count = 0
        self.wheat_count = 0
        self.rock_count = 0
        self.gold_count = 0
        
        self.wood_exp = 0
        self.brick_exp = 0
        self.sheep_exp = 0
        self.wheat_exp = 0
        self.rock_exp = 0
        self.gold_exp = 0
        
        self.wood_robbed = 0
        self.brick_robbed = 0
        self.sheep_robbed = 0
        self.wheat_robbed = 0
        self.rock_robbed = 0
        self.gold_robbed = 0
        
        self.exp_multipliers = []
        for num in [1,2,3,4,5,6,5,4,3,2,1]:
            self.exp_multipliers.append(num/36)
        
        self.tab_width = 1800/7
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.tiny_font = pygame.font.SysFont('Impact Regular', 50)
        self.baby_font = pygame.font.SysFont('Impact Regular', 26)
        
        self.name_text = self.font.render(self.name, False, self.font_colour)
        width, height = self.font.size(self.name)
        self.name_rect = (60 + (self.position + 0.5)*self.tab_width - width/2, 90, 0, 0)
        
        self.resource_texts = []
        for text in ['Wood', 'Brick', 'Sheep', 'Wheat', 'Rock', 'Total']:
            self.resource_texts.append(self.tiny_font.render(text, False, self.font_colour))
            
        self.subtitles_texts = []
        for text in ['Collected', 'Robbed']:
            self.subtitles_texts.append(self.mini_font.render(text, False, self.font_colour))
            
        self.robbed_shift = 300
            
        self.subtitles_rects = [self.subtitles_texts[0].get_rect(center = ((self.position + 0.5)*self.tab_width + 60, 200)), self.subtitles_texts[1].get_rect(center = ((self.position + 0.5)*self.tab_width + 60, 200 + self.robbed_shift))]
        
            
        self.create_numbers()
            
        shift = 200
        shift_e = 250
        
        self.resource_text_rects = []
        self.resource_text_rects_2 = []
        self.resource_numbers_texts_rects = []
        self.robbed_numbers_texts_rects = []
        self.expected_numbers_texts_rects = []
        for y in [220, 250, 280, 310, 340, 420]: # 370
            self.resource_text_rects.append((60 + self.position*self.tab_width, y))
            self.resource_text_rects_2.append((60 + self.position*self.tab_width, y + self.robbed_shift))
            self.resource_numbers_texts_rects.append((self.position*self.tab_width + shift, y))
            self.robbed_numbers_texts_rects.append((self.position*self.tab_width + shift, y + self.robbed_shift))
            self.expected_numbers_texts_rects.append((self.position*self.tab_width + shift_e, y))
            
        if self.mode == 6:
            self.gold_text = self.tiny_font.render('Gold', False, self.font_colour)
            self.gold_text_rects = [(60 + self.position*self.tab_width, 370), (60 + self.position*self.tab_width, 370 + self.robbed_shift)]
            self.gold_numbers_texts_rects = [(self.position*self.tab_width + shift, 370), (self.position*self.tab_width + shift, 370 + self.robbed_shift), (self.position*self.tab_width + shift_e, 370)]


    def create_numbers(self):
        
        total = self.wood_count + self.brick_count + self.sheep_count + self.wheat_count + self.rock_count + self.gold_count
        self.resource_numbers_texts = [self.tiny_font.render(str(self.wood_count), False, self.font_colour), self.tiny_font.render(str(self.brick_count), False, self.font_colour), self.tiny_font.render(str(self.sheep_count), False, self.font_colour), self.tiny_font.render(str(self.wheat_count), False, self.font_colour), self.tiny_font.render(str(self.rock_count), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
        total = self.wood_robbed + self.brick_robbed + self.sheep_robbed + self.wheat_robbed + self.rock_robbed + self.gold_robbed
        self.robbed_numbers_texts = [self.tiny_font.render(str(self.wood_robbed), False, self.font_colour), self.tiny_font.render(str(self.brick_robbed), False, self.font_colour), self.tiny_font.render(str(self.sheep_robbed), False, self.font_colour), self.tiny_font.render(str(self.wheat_robbed), False, self.font_colour), self.tiny_font.render(str(self.rock_robbed), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
        total = self.wood_exp + self.brick_exp + self.sheep_exp + self.wheat_exp + self.rock_exp + self.gold_exp
        self.expected_numbers_texts = [self.tiny_font.render(str(np.round(self.wood_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.brick_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.sheep_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.wheat_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.rock_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(total, decimals = 1)), False, self.font_colour)]
        
        if self.mode == 6:
            self.gold_numbers_texts = [self.tiny_font.render(str(self.gold_count), False, self.font_colour),
                                       self.tiny_font.render(str(self.gold_robbed), False, self.font_colour),
                                       self.tiny_font.render(str(np.round(self.gold_exp, decimals = 1)), False, self.font_colour)]
                                      
        
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
        for j in self.gold_nums:
            self.gold_exp += self.exp_multipliers[j-2]
        
        
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
                
        for i in range(len(self.gold_nums)):
            if self.gold_nums[i] == dice_total:
                self.gold_count += 1
                
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
            
        elif resource == 'gold':
            self.gold_nums.append(number)
                    
    def remove_resource(self, resource, number):
        
        if resource == 'wood':
            self.wood_nums.remove(number)
            
        elif resource == 'brick':
            self.brick_nums.remove(number)
            
        elif resource == 'sheep':
            self.sheep_nums.remove(number)
            
        elif resource == 'wheat':
            self.wheat_nums.remove(number)
            
        elif resource == 'rock':
            self.rock_nums.remove(number)
            
        elif resource == 'gold':
            self.gold_nums.remove(number)
        
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
        elif resource == 'gold':
            self.gold_robbed += amount
            self.gold_count -= amount
    
        self.create_numbers()
        
    def click(self, mouse):
        if 60 + (self.position + 0.5)*self.tab_width - 27 < mouse[0] < 60 + (self.position + 0.5)*self.tab_width + 27:
            return self.name
        else:
            return False
            
    def draw_tab(self, surface):
        pygame.draw.rect(surface, self.COLOUR, (60 + self.position*self.tab_width, 90, self.tab_width, 700))
        surface.blit(self.name_text, self.name_rect)
        
        for i in range(len(self.resource_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects[i])
            surface.blit(self.resource_numbers_texts[i], self.resource_numbers_texts_rects[i])
            surface.blit(self.expected_numbers_texts[i], self.expected_numbers_texts_rects[i])
            
        pygame.draw.rect(surface, self.font_colour, (self.position*self.tab_width + 242, 215, 2, 205))
            
        for i in range(len(self.robbed_numbers_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects_2[i])
            surface.blit(self.robbed_numbers_texts[i], self.robbed_numbers_texts_rects[i])
            
        for i in range(len(self.subtitles_rects)):
            surface.blit(self.subtitles_texts[i], self.subtitles_rects[i])
            
        if self.mode == 6:
            for i in range(len(self.gold_text_rects)):
                surface.blit(self.gold_text, self.gold_text_rects[i])
                
            for i in range(len(self.gold_numbers_texts)):
                surface.blit(self.gold_numbers_texts[i], self.gold_numbers_texts_rects[i])
            
        
class Total_Tab:
    def __init__(self, mode):
        
        self.mode = mode
        
        self.name = 'TOTAL'
        self.position = 6
        
        self.COLOUR = (0, 0, 0)
        self.font_colour = (255,255,255)
       
        self.set_zero()
        
        self.tab_width = 1800/7
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.tiny_font = pygame.font.SysFont('Impact Regular', 50)
        self.baby_font = pygame.font.SysFont('Impact Regular', 26)
        
        self.name_text = self.font.render(self.name, False, self.font_colour)
        width, height = self.font.size(self.name)
        self.name_rect = (60 + (self.position + 0.5)*self.tab_width - width/2, 90, 0, 0)
        
        self.resource_texts = []
        for text in ['Wood', 'Brick', 'Sheep', 'Wheat', 'Rock', 'Total']:
            self.resource_texts.append(self.tiny_font.render(text, False, self.font_colour))
            
        self.subtitles_texts = []
        for text in ['Collected', 'Robbed']:
            self.subtitles_texts.append(self.mini_font.render(text, False, self.font_colour))
            
        self.robbed_shift = 300
            
        self.subtitles_rects = [self.subtitles_texts[0].get_rect(center = ((self.position + 0.5)*self.tab_width + 60, 200)), self.subtitles_texts[1].get_rect(center = ((self.position + 0.5)*self.tab_width + 60, 200 + self.robbed_shift))]
        
        self.create_numbers()
                        
        shift = 180
        shift_e = 250
        
        self.resource_text_rects = []
        self.resource_text_rects_2 = []
        self.resource_numbers_texts_rects = []
        self.robbed_numbers_texts_rects = []
        self.expected_numbers_texts_rects = []
        for y in [220, 250, 280, 310, 340, 420]:
            self.resource_text_rects.append((60 + self.position*self.tab_width, y))
            self.resource_text_rects_2.append((60 + self.position*self.tab_width, y + self.robbed_shift))
            self.resource_numbers_texts_rects.append((self.position*self.tab_width + shift, y))
            self.robbed_numbers_texts_rects.append((self.position*self.tab_width + shift, y + self.robbed_shift))
            self.expected_numbers_texts_rects.append((self.position*self.tab_width + shift_e, y))
            
        if self.mode == 6:
            self.gold_text = self.tiny_font.render('Gold', False, self.font_colour)
            self.gold_text_rects = [(60 + self.position*self.tab_width, 370), (60 + self.position*self.tab_width, 370 + self.robbed_shift)]
            self.gold_numbers_texts_rects = [(self.position*self.tab_width + shift, 370), (self.position*self.tab_width + shift, 370 + self.robbed_shift), (self.position*self.tab_width + shift_e, 370)]

            
    def create_numbers(self):
        
        total = self.wood_count + self.brick_count + self.sheep_count + self.wheat_count + self.rock_count + self.gold_count
        self.resource_numbers_texts = [self.tiny_font.render(str(self.wood_count), False, self.font_colour), self.tiny_font.render(str(self.brick_count), False, self.font_colour), self.tiny_font.render(str(self.sheep_count), False, self.font_colour), self.tiny_font.render(str(self.wheat_count), False, self.font_colour), self.tiny_font.render(str(self.rock_count), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
        total = self.wood_robbed + self.brick_robbed + self.sheep_robbed + self.wheat_robbed + self.rock_robbed + self.gold_robbed
        self.robbed_numbers_texts = [self.tiny_font.render(str(self.wood_robbed), False, self.font_colour), self.tiny_font.render(str(self.brick_robbed), False, self.font_colour), self.tiny_font.render(str(self.sheep_robbed), False, self.font_colour), self.tiny_font.render(str(self.wheat_robbed), False, self.font_colour), self.tiny_font.render(str(self.rock_robbed), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
        total = self.wood_exp + self.brick_exp + self.sheep_exp + self.wheat_exp + self.rock_exp + self.gold_exp
        self.expected_numbers_texts = [self.tiny_font.render(str(np.round(self.wood_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.brick_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.sheep_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.wheat_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(np.round(self.rock_exp, decimals = 1)), False, self.font_colour), self.tiny_font.render(str(int(np.round(total, decimals = 0))), False, self.font_colour)]
    
        if self.mode == 6:
            self.gold_numbers_texts = [self.tiny_font.render(str(self.gold_count), False, self.font_colour),
                                       self.tiny_font.render(str(self.gold_robbed), False, self.font_colour),
                                       self.tiny_font.render(str(np.round(self.gold_exp, decimals = 1)), False, self.font_colour)]
    
    def set_zero(self):
        
        self.wood_count = 0
        self.brick_count = 0
        self.sheep_count = 0
        self.wheat_count = 0
        self.rock_count = 0
        self.gold_count = 0
        
        self.wood_exp = 0
        self.brick_exp = 0
        self.sheep_exp = 0
        self.wheat_exp = 0
        self.rock_exp = 0
        self.gold_exp = 0
        
        self.wood_robbed = 0
        self.brick_robbed = 0
        self.sheep_robbed = 0
        self.wheat_robbed = 0
        self.rock_robbed = 0
        self.gold_robbed = 0
    
    def update(self, players):
        
        self.set_zero()
        
        for player in players:
            self.wood_count += player.wood_count
            self.brick_count += player.brick_count
            self.sheep_count += player.sheep_count
            self.wheat_count += player.wheat_count
            self.rock_count += player.rock_count
            self.gold_count += player.gold_count
            
            self.wood_exp += player.wood_exp
            self.brick_exp += player.brick_exp
            self.sheep_exp += player.sheep_exp
            self.wheat_exp += player.wheat_exp
            self.rock_exp += player.rock_exp
            self.gold_exp += player.gold_exp
            
            self.wood_robbed += player.wood_robbed
            self.brick_robbed += player.brick_robbed
            self.sheep_robbed += player.sheep_robbed
            self.wheat_robbed += player.wheat_robbed
            self.rock_robbed += player.rock_robbed
            self.gold_robbed += player.gold_robbed
            
        self.create_numbers()
    
    def draw_tab(self, surface):
        pygame.draw.rect(surface, self.COLOUR, (60 + self.position*self.tab_width, 90, self.tab_width, 700))
        surface.blit(self.name_text, self.name_rect)
        
        for i in range(len(self.resource_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects[i])
            surface.blit(self.resource_numbers_texts[i], self.resource_numbers_texts_rects[i])
            surface.blit(self.expected_numbers_texts[i], self.expected_numbers_texts_rects[i])
            
        pygame.draw.rect(surface, self.font_colour, (self.position*self.tab_width + 242, 215, 2, 205))
            
        for i in range(len(self.robbed_numbers_texts)):
            surface.blit(self.resource_texts[i], self.resource_text_rects_2[i])
            surface.blit(self.robbed_numbers_texts[i], self.robbed_numbers_texts_rects[i])
            
        for i in range(len(self.subtitles_rects)):
            surface.blit(self.subtitles_texts[i], self.subtitles_rects[i])
            
        if self.mode == 6:
            for i in range(len(self.gold_text_rects)):
                surface.blit(self.gold_text, self.gold_text_rects[i])
                
            for i in range(len(self.gold_numbers_texts)):
                surface.blit(self.gold_numbers_texts[i], self.gold_numbers_texts_rects[i])
        
        
def get_player_info(Default = False):  
    
    if Default:
        num_players = 'Default'
    else:         
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
        if self.player.mode == 6:
            self.width = self.width*(23/32)
            
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

class Clear_Button:
    def __init__(self, CONSTANTS, MAIN_TAB):
        self.con = CONSTANTS
        self.MT = MAIN_TAB
        
        self.colour = (250,250,250)
        self.font_colour = (20,20,20)
        
        self.height = self.MT.height/6
        self.width = self.MT.width*11/48
        if len(self.con['Players']) > 0:
            if self.con['Players'][0].mode == 6:
                self.width = self.width*(23/32)
                
        self.x = self.MT.x
        self.y = self.MT.y + self.height
        
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.baby_font = pygame.font.SysFont('Impact Regular', 26)
        
        self.name_text = self.mini_font.render('Clear', False, self.font_colour)
        self.name_text_rect = self.name_text.get_rect(center = (self.x + self.width/2, self.y + self.height/4))
        
        self.button_texts = [self.baby_font.render('Clear', False, self.font_colour)]
        self.button_texts_rects = [self.button_texts[0].get_rect(center = (self.x + self.width/2, self.y + self.height*3/4))]
        
    def click(self, mouse):
        if self.y + self.height/2 < mouse[1] < self.y + self.height:
            if self.x < mouse[0] < self.x + self.width:
                return True
        else:
            return False
    
    def draw(self, surface, clear_assigner):
        
        pygame.draw.rect(surface, self.colour, (self.x, self.y, self.width, self.height))
        
        pygame.draw.rect(surface, (0,0,0), (self.x, self.y, self.width, self.height), width = 2)
        
        if clear_assigner:
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width, self.height/2), width = 6)
        else:
            pygame.draw.rect(surface, (0,0,0), (self.x, self.y + self.height/2, self.width, self.height/2), width = 2)
          
            
        surface.blit(self.name_text, self.name_text_rect)
        
        for i in range(len(self.button_texts)):
            surface.blit(self.button_texts[i], self.button_texts_rects[i])
            
            
class Robber_Map_Button:
    def __init__(self, CONSTANTS, MAIN_TAB):
        self.con = CONSTANTS
        self.MT = MAIN_TAB
        
        self.colour = (50,50,50)
        self.font_colour = (250,250,250)
        
        self.height = self.MT.height/6
        self.width = self.MT.width*11/48
        if len(self.con['Players']) > 0:
            if self.con['Players'][0].mode == 6:
                #self.width = self.width*(23/32)
                pass
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