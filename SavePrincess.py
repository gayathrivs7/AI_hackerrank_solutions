#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here

    if grid[0][0]=='p':
        print('UP\nLEFT')
    elif grid[0][2]=='p':
        print('DOWN\nRIGHT')
    elif grid[2][0]=='p':
        print('DOWN\nLEFT')
    elif grid[2][2]=='p':
        print('DOWN\nRIGHT')


m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)