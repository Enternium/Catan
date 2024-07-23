# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:11:35 2024

@author: jackp
"""

import pygame
import math
import random




class Hexagon:
    def __init__(self, points_rows, row, column, resource, number, edge_length):
        
        self.robbed = False
        
        row *= 2
        
        if row <= 4:
        
            self.coordinates = [points_rows[row][column].coord, points_rows[row+1][column+1].coord, points_rows[row+2][column+1].coord, points_rows[row+3][column+1].coord, points_rows[row+2][column].coord, points_rows[row+1][column].coord]
        
        elif row == 6:
            
            self.coordinates = [points_rows[row][column].coord, points_rows[row+1][column+1].coord, points_rows[row+2][column+1].coord, points_rows[row+3][column].coord, points_rows[row+2][column].coord, points_rows[row+1][column].coord]
        
        else:
            
            self.coordinates = [points_rows[row][column+1].coord, points_rows[row+1][column+1].coord, points_rows[row+2][column+1].coord, points_rows[row+3][column].coord, points_rows[row+2][column].coord, points_rows[row+1][column].coord]

        self.resource = resource
        self.number = number
        
        if self.resource == 'wood':
            self.colour = (117,139,90)
        elif self.resource == 'sea':
            self.colour = (5,155,218)
        elif self.resource == 'sheep':
            self.colour = (116,187,69)
        elif self.resource == 'rock':
            self.colour = (158,143,139)
        elif self.resource == 'brick':
            self.colour = (172,91,38)
        elif self.resource == 'wheat':
            self.colour = (237,187,64)
        else:
            self.colour = (255,255,255)
            
        if self.number:
            
            if self.number in [6,8]:
                num_col = (184,40,26)
            else:
                num_col = (20,10,0)
                
            self.font_size = int(edge_length * (3/4))
            self.circle_size = int(edge_length * (3/8))
                
            self.font = pygame.font.SysFont('Impact Regular', self.font_size)
            self.text = self.font.render(str(number), False, num_col)
            self.robbed_text = self.font.render(str(number), False, (250,250,250))
            self.text_rect = self.text.get_rect(center = (self.coordinates[0][0], self.coordinates[0][1] + edge_length))
            self.num_x = self.text_rect[0] + self.text_rect[2]/2
            self.num_y = self.text_rect[1] + self.text_rect[3]/2
            
            
    def click(self, mouse):
        if self.number:
            if (mouse[0] - self.num_x)**2 + (mouse[1] - self.num_y)**2 < self.circle_size**2:
                return True
        return False
    
    def draw(self, surface):
        
        pygame.draw.polygon(surface, self.colour, self.coordinates)
        pygame.draw.polygon(surface, (10,10,10), self.coordinates, width = 1)
        
        if self.number:
            if self.robbed:
                pygame.draw.circle(surface, (0,0,0), (self.num_x, self.num_y), self.circle_size)
                surface.blit(self.robbed_text, self.text_rect)
            else:
                pygame.draw.circle(surface, (231,207,158), (self.num_x, self.num_y), self.circle_size)
                surface.blit(self.text, self.text_rect)



def seed_maker():
    temp = []
    for i in range(5):
        temp.append('wood')
    for i in range(4):
        temp.append('brick')
    for i in range(5):
        temp.append('sheep')
    for i in range(4):
        temp.append('rock')
    for i in range(5):
        temp.append('wheat')
    for i in range(19):
        temp.append('sea')
        
    random.shuffle(temp)
    
    numbers = [2,3,3,3,4,4,4,5,5,5,6,6,8,8,9,9,9,10,10,10,11,11,12]
    
    random.shuffle(numbers)
    
    return temp, numbers


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.coord = [x,y]
        
        self.colour = (0,0,0)
        
        self.hexes = []
        
        self.player = False
        self.structure = False
        
        self.radius = 4
        self.settlement_rect = (self.x - self.radius*4, self.y - self.radius*2, self.radius*8, self.radius*4)
        
        self.city_rect_1 = (self.x - self.radius*4, self.y, self.radius*8, self.radius*4)
        self.city_rect_2 = (self.x, self.y - self.radius*4, self.radius*4, self.radius*4)
        
    def clear_hexes(self):
        self.hexes = []
    
    def allocate_hex(self, hexagon):
        self.hexes.append(hexagon)
        
    def assign_player(self, player, structure):
        self.player = player
        self.colour = player.COLOUR
        self.structure = structure
        
    def click(self, mouse, player, structure):
        if self.x - self.radius < mouse[0] < self.x + self.radius:
            if self.y - self.radius*2 < mouse[1] < self.y + self.radius*2:
                self.assign_player(player, structure)
                return self.hexes
            
        return False
        
    def draw(self, surface):
        if self.structure == 'Settlement':
            pygame.draw.rect(surface, self.colour, self.settlement_rect)
        elif self.structure == 'City':
            pygame.draw.rect(surface, self.colour, self.city_rect_1)
            pygame.draw.rect(surface, self.colour, self.city_rect_2)
        else:
            pygame.draw.circle(surface, self.colour, (self.x, self.y), self.radius)


def point_generator(edge_length, center):

    # GENERATE POINTS -------------------------------------------
        
    short_diagonal = edge_length * math.sqrt(3)
    
    
    starting_x = center[0] - 2*short_diagonal
    starting_y = center[1] - 11/2*edge_length
    points_rows = []
    
    
    ranges = [5,6,6,7,7,8,8,9,9,8,8,7,7,6,6,5]
    xs = [0,1,1,2,2,3,3,4,4,3,3,2,2,1,1,0]
    ys = [0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22]
    
    for i in range(len(ranges)):
        temp = []
        for j in range(ranges[i]):
            temp.append(Point(starting_x - short_diagonal*xs[i]/2 + j*short_diagonal, starting_y + edge_length*ys[i]/2))
        points_rows.append(temp)
    
    pure_points_list = []
    for i in range(len(points_rows)):
        for j in range(len(points_rows[i])):
            pure_points_list.append(points_rows[i][j])
            
    return points_rows, pure_points_list   


def map_maker(edge_length, pure_points_list, points_rows):
    # GENERATE MAP ------------------------------
    while True:
        seed, numbers = seed_maker()
        HEXES = []
        columns = [5,6,7,8,7,6,5]
        for i in range(7):
            for j in range(columns[i]):
                if i == 3 and j in [0,7]:
                    HEXES.append(Hexagon(points_rows, i, j, 'sea', False, edge_length))
                else:
                    resource = seed[-1]
                    if resource == 'sea':
                        number = False
                    else:
                        number = numbers[-1]
                        numbers.pop()
                    HEXES.append(Hexagon(points_rows, i, j, resource, number, edge_length))
                    seed.pop()
               
        # CHECK IF LEGAL -----------------
        legal = True
        for point in pure_points_list:
            nums = []
            for hexagon in HEXES:
                if point.coord in hexagon.coordinates:
                    nums.append(hexagon.number)
            count_sixes = nums.count(6)
            count_eights = nums.count(8)
            if count_sixes + count_eights > 1:
                legal = False
                
        if legal:
            break
    
    return HEXES
    

class Map:
    def __init__(self, edge_length, center):
        self.edge_length = edge_length
        self.center = center
                    
        self.points_rows, self.pure_points_list = point_generator(self.edge_length, self.center)
        
        self.gen_map()
        
    def gen_map(self):
        self.HEXES = map_maker(self.edge_length, self.pure_points_list, self.points_rows)
        
        for point in self.pure_points_list:
            point.clear_hexes()
        
        self.allocate_hexes_to_points()
        
    def allocate_hexes_to_points(self):
        for point in self.pure_points_list:
            for hexagon in self.HEXES:
                if point.coord in hexagon.coordinates:
                    point.allocate_hex(hexagon)
        
    def calc_robbery(self, players, number):
        for point in self.pure_points_list:
            if point.player:
                for hexagon in point.hexes:
                    if hexagon.robbed:
                        if hexagon.number == number:
                            for player in players:
                                if player == point.player:
                                    
                                    if point.structure == 'Settlement':
                                        amount = 1
                                    else:
                                        amount = 2
                                    
                                    player.robbed(hexagon.resource, amount)
                                    
                                    
        return players
    
    def draw(self, surface):
        for hexagon in self.HEXES:
            hexagon.draw(surface)
        
        for point in self.pure_points_list:
            point.draw(surface)




def Run_here():
    pygame.init()
    
    #surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
    surface = pygame.display.set_mode((1440,960))  
    
    pygame.display.set_caption('Catan Data') 
    
    CONSTANTS = {}
    
    CONSTANTS['Width'], CONSTANTS['Height'] = pygame.display.get_surface().get_size()
    running = True
      
    MAP = Map(80, (CONSTANTS['Width']/2, CONSTANTS['Height']/2))
    
    # game loop 
    while running: 
        
        surface.fill((200, 200, 200)) 
                
        MAP.draw(surface)
            
        for event in pygame.event.get(): 
          
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    MAP.gen_map()
    
                    
                    
                    
        
        pygame.display.flip()             
    pygame.quit()
    

