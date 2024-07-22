# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:11:35 2024

@author: jackp
"""

import pygame
import math
import random

pygame.init()

surface = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
  
pygame.display.set_caption('Catan Data') 

CONSTANTS = {}

CONSTANTS['Width'], CONSTANTS['Height'] = pygame.display.get_surface().get_size()
 


class Hexagon:
    def __init__(self, points_rows, row, column, resource, number, edge_length):
        
        row *= 2
        
        if row <= 4:
        
            self.coordinates = [points_rows[row][column], points_rows[row+1][column+1], points_rows[row+2][column+1], points_rows[row+3][column+1], points_rows[row+2][column], points_rows[row+1][column]]
        
        elif row == 6:
            
            self.coordinates = [points_rows[row][column], points_rows[row+1][column+1], points_rows[row+2][column+1], points_rows[row+3][column], points_rows[row+2][column], points_rows[row+1][column]]
        
        else:
            
            self.coordinates = [points_rows[row][column+1], points_rows[row+1][column+1], points_rows[row+2][column+1], points_rows[row+3][column], points_rows[row+2][column], points_rows[row+1][column]]

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
                
            self.font = pygame.font.SysFont('Impact Regular', 70)
            self.text = self.font.render(str(number), False, num_col)
            self.text_rect = self.text.get_rect(center = (self.coordinates[0][0], self.coordinates[0][1] + edge_length))
            self.num_x = self.text_rect[0] + self.text_rect[2]/2
            self.num_y = self.text_rect[1] + self.text_rect[3]/2
            
            
    def draw(self, surface):
        
        pygame.draw.polygon(surface, self.colour, self.coordinates)
        pygame.draw.polygon(surface, (10,10,10), self.coordinates, width = 1)
        
        if self.number:
            pygame.draw.circle(surface, (231,207,158), (self.num_x, self.num_y), 30)
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
                if point in hexagon.coordinates:
                    nums.append(hexagon.number)
            count_sixes = nums.count(6)
            count_eights = nums.count(8)
            if count_sixes + count_eights > 1:
                legal = False
                
        if legal:
            break
    
    return HEXES
    
# GENERATE POINTS -------------------------------------------

edge_length = 85

short_diagonal = edge_length * math.sqrt(3)


starting_x = CONSTANTS['Width']/2 - 2*short_diagonal
starting_y = CONSTANTS['Height']/2 - 11/2*edge_length
points_rows = []


ranges = [5,6,6,7,7,8,8,9,9,8,8,7,7,6,6,5]
xs = [0,1,1,2,2,3,3,4,4,3,3,2,2,1,1,0]
ys = [0,1,3,4,6,7,9,10,12,13,15,16,18,19,21,22]

for i in range(len(ranges)):
    temp = []
    for j in range(ranges[i]):
        temp.append([starting_x - short_diagonal*xs[i]/2 + j*short_diagonal, starting_y + edge_length*ys[i]/2])
    points_rows.append(temp)

pure_points_list = []
for i in range(len(points_rows)):
    for j in range(len(points_rows[i])):
        pure_points_list.append(points_rows[i][j])


HEXES = map_maker(edge_length, pure_points_list, points_rows)



running = True
  
# game loop 
while running: 
    
    surface.fill((200, 200, 200)) 
    
    for row in points_rows:
        for point in row:
            pygame.draw.circle(surface, (0,0,0), point, 4)
            
    for hexagon in HEXES:
        hexagon.draw(surface)
        
        
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_r:
                HEXES = map_maker(edge_length, pure_points_list, points_rows)

                
                
                
    
    pygame.display.flip()             
pygame.quit()





