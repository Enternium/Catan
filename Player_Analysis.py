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
            self.COLOUR = (133, 180, 255)
            self.font_colour = (0,0,0)
        elif colour in ['Orange', 'orange', 'O', 'o']:
            self.COLOUR = (230,138,0)
            self.font_colour = (0,0,0)
        elif colour in ['White', 'white', 'W', 'w']:
            self.COLOUR = (255,255,255)
            self.font_colour = (0,0,0)
        elif colour in ['Brown', 'brown', 'Br', 'br']:
            self.COLOUR = (117,76,21)
            self.font_colour = (255,255,255)
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
        
        self.name_text = self.font.render(self.name, False, self.font_colour)
        width, height = self.font.size(self.name)
        self.name_rect = (60 + (self.position + 0.5)*self.tab_width - width/2, 80, 0, 0)
        
        self.resource_texts = [self.tiny_font.render('Wood:', False, self.font_colour), self.tiny_font.render('Brick:', False, self.font_colour), self.tiny_font.render('Sheep:', False, self.font_colour), self.tiny_font.render('Wheat:', False, self.font_colour), self.tiny_font.render('Rock:', False, self.font_colour), self.tiny_font.render('Total:', False, self.font_colour)]
        self.resource_text_rects = [(60 + self.position*self.tab_width, 160), (60 + self.position*self.tab_width, 190), (60 + self.position*self.tab_width, 220), (60 + self.position*self.tab_width, 250), (60 + self.position*self.tab_width, 280), (60 + self.position*self.tab_width, 330)]
        
        self.create_numbers()
        shift = 150
        self.resource_numbers_texts_rects = [(60 + self.position*self.tab_width + shift, 160), (60 + self.position*self.tab_width + shift, 190), (60 + self.position*self.tab_width + shift, 220), (60 + self.position*self.tab_width + shift, 250), (60 + self.position*self.tab_width + shift, 280), (60 + self.position*self.tab_width + shift, 330)]
        
        self.create_settlement_list()
        
    def create_numbers(self):
        
        total = self.wood_count + self.brick_count + self.sheep_count + self.wheat_count + self.rock_count
        self.resource_numbers_texts = [self.tiny_font.render(str(self.wood_count), False, self.font_colour), self.tiny_font.render(str(self.brick_count), False, self.font_colour), self.tiny_font.render(str(self.sheep_count), False, self.font_colour), self.tiny_font.render(str(self.wheat_count), False, self.font_colour), self.tiny_font.render(str(self.rock_count), False, self.font_colour), self.tiny_font.render(str(total), False, self.font_colour)]
        
    def create_settlement_list(self):
        self.settlements_texts = []
        self.settlements_texts_rects = []
        
        list_ = [self.wood_nums, self.brick_nums, self.sheep_nums, self.wheat_nums, self.rock_nums]
        words = ['Wood', 'Brick', 'Sheep', 'Wheat', 'Rock']
        
        for j in range(5):
            for i in range(len(list_[j])):
                self.settlements_texts.append(self.tiny_font.render(f'{words[j]} {list_[j][i]}', False, self.font_colour))

        for i in range(len(self.settlements_texts)):
            self.settlements_texts_rects.append((60 + self.position*self.tab_width, 160 + i*30))
            
    
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
            
        self.create_settlement_list()
    
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
            
        pygame.draw.circle(surface, (0,150,0), (60 + (self.position + 0.5)*self.tab_width, 600), 54)
        pygame.draw.circle(surface, (0,250,0), (60 + (self.position + 0.5)*self.tab_width, 600), 50)
        pygame.draw.rect(surface, (0,0,0), (60 + (self.position + 0.5)*self.tab_width - 15, 597, 30, 6))
        pygame.draw.rect(surface, (0,0,0), (60 + (self.position + 0.5)*self.tab_width - 3, 585, 6, 30))
        
    def draw_robber(self, surface):
        pygame.draw.rect(surface, self.COLOUR, (60 + self.position*self.tab_width, 80, self.tab_width, 600))
        surface.blit(self.name_text, self.name_rect)
        
        for i in range(len(self.settlements_texts)):
            surface.blit(self.settlements_texts[i], self.settlements_texts_rects[i])


class Adding_Tab:
    def __init__(self, CONSTANTS):
        self.width = CONSTANTS['Width']*0.95 - 24
        self.height = 600
        self.x = 60
        self.y = CONSTANTS['Height']/2 - self.height/2 - 100
        
        self.tab_width = self.width/4
        self.tab_gap = self.width/16
        
        self.resources = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
        
        self.numbers = [0,0,0]
        self.combinations = [2,3,4,5,6,8,9,10,11,12]
        
        self.font = pygame.font.SysFont('Impact Regular', 100)
        self.mini_font = pygame.font.SysFont('Impact Regular', 60)
        self.tiny_font = pygame.font.SysFont('Impact Regular', 50)
        self.font_colour = (0,0,0)
        
        self.resource_texts = [self.tiny_font.render('Wood', False, self.font_colour), self.tiny_font.render('Brick', False, self.font_colour), self.tiny_font.render('Sheep', False, self.font_colour), self.tiny_font.render('Wheat', False, self.font_colour), self.tiny_font.render('Rock', False, self.font_colour)]
        self.resource_heights = [self.tiny_font.size('Wood')[1], self.tiny_font.size('Brick')[1], self.tiny_font.size('Sheep')[1], self.tiny_font.size('Wheat')[1], self.tiny_font.size('Rock')[1]]
        
        self.numbers_texts = []
        self.numbers_widths = []
        self.numbers_heights = []
        for i in self.combinations:
            self.numbers_texts.append(self.tiny_font.render(str(i), False, (0,0,0)))
            width, height = self.tiny_font.size(str(i))
            self.numbers_widths.append(width)
            self.numbers_heights.append(height)
            
        # x, y, width, height
        self.confirm_box_dimensions = [self.x + self.width/2 - self.tab_width/2, self.y + self.height*5/6, self.tab_width, 60]
        self.confirm_box_narrow = [self.confirm_box_dimensions[0] + 2, self.confirm_box_dimensions[1] + 2, self.confirm_box_dimensions[2] - 4, self.confirm_box_dimensions[3] - 4]
    
    def convert_resouces(self, TF_list):
        if TF_list[0]:
            return 'wood'
        if TF_list[1]:
            return 'brick'
        if TF_list[2]:
            return 'sheep'
        if TF_list[3]:
            return 'wheat'
        if TF_list[4]:
            return 'rock'
        
        return 'None'
        
    
    def click(self, mouse):
        
        # CONFIRM BOX
        if self.confirm_box_dimensions[0] < mouse[0] < self.confirm_box_dimensions[0] + self.confirm_box_dimensions[2]:
            if self.confirm_box_dimensions[1] < mouse[1] < self.confirm_box_dimensions[1] + self.confirm_box_dimensions[3]:
                resources = [self.convert_resouces(self.resources[0]), self.convert_resouces(self.resources[1]), self.convert_resouces(self.resources[2])]
                return [self.numbers, resources]
           
        # 3 widths
        if self.x + self.tab_gap < mouse[0] < self.x + self.tab_gap + self.tab_width:
            
            # RESOURCES -------------------
            if self.y + self.height/12 < mouse[1] < self.y + self.height/12 + 50:
                self.resources[0] = [True, False, False, False, False]
            elif self.y + self.height/12 + 50 < mouse[1] < self.y + self.height/12 + 100:
                self.resources[0] = [False, True, False, False, False]
            elif self.y + self.height/12 + 100 < mouse[1] < self.y + self.height/12 + 150:
                self.resources[0] = [False, False, True, False, False]
            elif self.y + self.height/12 + 150 < mouse[1] < self.y + self.height/12 + 200:
                self.resources[0] = [False, False, False, True, False]
            elif self.y + self.height/12 + 200 < mouse[1] < self.y + self.height/12 + 250:
                self.resources[0] = [False, False, False, False, True]
            
            # NUMBERS -----------
            elif self.y + self.height*7/12 < mouse[1] < self.y + self.height*7/12 + 60:
                if self.x + self.tab_gap < mouse[0] < self.x + self.tab_gap + self.tab_width/5:
                    self.numbers[0] = 2
                elif self.x + self.tab_gap + self.tab_width/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*2/5:
                    self.numbers[0] = 3
                elif self.x + self.tab_gap + self.tab_width*2/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*3/5:
                    self.numbers[0] = 4
                elif self.x + self.tab_gap + self.tab_width*3/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*4/5:
                    self.numbers[0] = 5
                elif self.x + self.tab_gap + self.tab_width*4/5 < mouse[0] < self.x + self.tab_gap + self.tab_width:
                    self.numbers[0] = 6
                    
            elif self.y + self.height*7/12 + 60 < mouse[1] < self.y + self.height*7/12 + 120:
                if self.x + self.tab_gap < mouse[0] < self.x + self.tab_gap + self.tab_width/5:
                    self.numbers[0] = 8
                elif self.x + self.tab_gap + self.tab_width/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*2/5:
                    self.numbers[0] = 9
                elif self.x + self.tab_gap + self.tab_width*2/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*3/5:
                    self.numbers[0] = 10
                elif self.x + self.tab_gap + self.tab_width*3/5 < mouse[0] < self.x + self.tab_gap + self.tab_width*4/5:
                    self.numbers[0] = 11
                elif self.x + self.tab_gap + self.tab_width*4/5 < mouse[0] < self.x + self.tab_gap + self.tab_width:
                    self.numbers[0] = 12
        
        elif self.x + 2*self.tab_gap + self.tab_width < mouse[0] < self.x + 2*self.tab_gap + 2*self.tab_width:
            
            # RESOURCES -------------------
            if self.y + self.height/12 < mouse[1] < self.y + self.height/12 + 50:
                self.resources[1] = [True, False, False, False, False]
            elif self.y + self.height/12 + 50 < mouse[1] < self.y + self.height/12 + 100:
                self.resources[1] = [False, True, False, False, False]
            elif self.y + self.height/12 + 100 < mouse[1] < self.y + self.height/12 + 150:
                self.resources[1] = [False, False, True, False, False]
            elif self.y + self.height/12 + 150 < mouse[1] < self.y + self.height/12 + 200:
                self.resources[1] = [False, False, False, True, False]
            elif self.y + self.height/12 + 200 < mouse[1] < self.y + self.height/12 + 250:
                self.resources[1] = [False, False, False, False, True]
            
            # NUMBERS -----------
            elif self.y + self.height*7/12 < mouse[1] < self.y + self.height*7/12 + 60:
                if self.x + 2*self.tab_gap + self.tab_width  < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width/5:
                    self.numbers[1] = 2
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*2/5:
                    self.numbers[1] = 3
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*2/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*3/5:
                    self.numbers[1] = 4
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*3/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*4/5:
                    self.numbers[1] = 5
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*4/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width:
                    self.numbers[1] = 6
                    
            elif self.y + self.height*7/12 + 60 < mouse[1] < self.y + self.height*7/12 + 120:
                if self.x + 2*self.tab_gap + self.tab_width  < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width/5:
                    self.numbers[1] = 8
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*2/5:
                    self.numbers[1] = 9
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*2/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*3/5:
                    self.numbers[1] = 10
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*3/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width*4/5:
                    self.numbers[1] = 11
                elif self.x + 2*self.tab_gap + self.tab_width + self.tab_width*4/5 < mouse[0] < self.x + 2*self.tab_gap + self.tab_width + self.tab_width:
                    self.numbers[1] = 12
        
        elif self.x + 3*self.tab_gap + 2*self.tab_width < mouse[0] < self.x + 3*self.tab_gap + 3*self.tab_width:
            
            # RESOURCES -------------------
            if self.y + self.height/12 < mouse[1] < self.y + self.height/12 + 50:
                self.resources[2] = [True, False, False, False, False]
            elif self.y + self.height/12 + 50 < mouse[1] < self.y + self.height/12 + 100:
                self.resources[2] = [False, True, False, False, False]
            elif self.y + self.height/12 + 100 < mouse[1] < self.y + self.height/12 + 150:
                self.resources[2] = [False, False, True, False, False]
            elif self.y + self.height/12 + 150 < mouse[1] < self.y + self.height/12 + 200:
                self.resources[2] = [False, False, False, True, False]
            elif self.y + self.height/12 + 200 < mouse[1] < self.y + self.height/12 + 250:
                self.resources[2] = [False, False, False, False, True]
            
            # NUMBERS -----------
            elif self.y + self.height*7/12 < mouse[1] < self.y + self.height*7/12 + 60:
                if self.x + 3*self.tab_gap + 2*self.tab_width  < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width/5:
                    self.numbers[2] = 2
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*2/5:
                    self.numbers[2] = 3
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*2/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*3/5:
                    self.numbers[2] = 4
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*3/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*4/5:
                    self.numbers[2] = 5
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*4/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width:
                    self.numbers[2] = 6
                    
            elif self.y + self.height*7/12 + 60 < mouse[1] < self.y + self.height*7/12 + 120:
                if self.x + 3*self.tab_gap + 2*self.tab_width  < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width/5:
                    self.numbers[2] = 8
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*2/5:
                    self.numbers[2] = 9
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*2/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*3/5:
                    self.numbers[2] = 10
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*3/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*4/5:
                    self.numbers[2] = 11
                elif self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width*4/5 < mouse[0] < self.x + 3*self.tab_gap + 2*self.tab_width + self.tab_width:
                    self.numbers[2] = 12
        
        
        return False
        
    
    def draw(self, surface):
        
        for i in range(3):
            
            # RESOURCES -----------------------------
            for j in range(5):
                if self.resources[i][j]:
                    colour = (50,50,50)
                else:
                    colour = (120,120,120)
                pygame.draw.rect(surface, (0,0,0), (self.x + (i+1)*self.tab_gap + i*self.tab_width, self.y + self.height/12 + j*50, self.tab_width, 50))
                pygame.draw.rect(surface, colour, (self.x + (i+1)*self.tab_gap + i*self.tab_width + 2, self.y + self.height/12 + j*50 + 2, self.tab_width - 4, 50 - 4))
                surface.blit(self.resource_texts[j], (self.x + (i+1)*self.tab_gap + i*self.tab_width + 2, self.y + self.height/12 + j*50 + 25 - self.resource_heights[j]/2))

            
            
            # NUMBERS -------------------------
            for j in range(10):
                
                if self.numbers[i] == self.combinations[j]:
                    colour = (50,50,50)
                else:
                    colour = (120,120,120)
                    
                if j < 5:
                    pygame.draw.rect(surface, (0,0,0), (self.x + (i+1)*self.tab_gap + i*self.tab_width + j*self.tab_width/5, self.y + self.height*7/12, self.tab_width/5, 60))
                    pygame.draw.rect(surface, colour, (self.x + (i+1)*self.tab_gap + i*self.tab_width + j*self.tab_width/5 + 2, self.y + self.height*7/12 + 2, self.tab_width/5 - 4, 60 - 4))
                    surface.blit(self.numbers_texts[j], (self.x + (i+1)*self.tab_gap + i*self.tab_width + (j + 0.5)*self.tab_width/5 - self.numbers_widths[j]/2, self.y + self.height*7/12 + 30 - self.numbers_heights[j]/2, 0, 0))
                else:
                    pygame.draw.rect(surface, (0,0,0), (self.x + (i+1)*self.tab_gap + i*self.tab_width + (j-5)*self.tab_width/5, self.y + self.height*7/12 + 60, self.tab_width/5, 60))
                    pygame.draw.rect(surface, colour, (self.x + (i+1)*self.tab_gap + i*self.tab_width + (j-5)*self.tab_width/5 + 2, self.y + self.height*7/12 + 60 + 2, self.tab_width/5 - 4, 60 - 4))
                    surface.blit(self.numbers_texts[j], (self.x + (i + 1)*self.tab_gap + i*self.tab_width + (j - 5 + 0.5)*self.tab_width/5 - self.numbers_widths[j]/2, self.y + self.height*7/12 + 90 - self.numbers_heights[j]/2, 0, 0))

        pygame.draw.rect(surface, (20,240,20), self.confirm_box_dimensions)
        pygame.draw.rect(surface, (20,150,20), self.confirm_box_narrow)

        
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
            
            