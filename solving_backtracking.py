# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:43:57 2022

@author: AKANO
"""

#N_QUEENS_PROBLEM

import time
from random import randint




def is_safe(present_row, present_col, assigned_cells):
    for row, col in assigned_cells:
        if (row, col) != (present_row, present_col):
            if (present_col + present_row == col + row) or (present_col - present_row == col - row):
                return False
            elif col == present_col:
                return False

    return True

# The function get_domain values for a given row
def get_domain(assigned_cells, row, domains):
    values = []
    for col in domains[row]:
        if is_safe(row, col, assigned_cells):
            values.append(col)

    return values


#
def update_domains(assigned_cells, domains, unassigned_cells, n):
    new_domains = {}
    next_row = len(assigned_cells)
    list = []

    for i in unassigned_cells:
        values = get_domain(assigned_cells, i, domains)
        if len(values) == 0:
            return {}, True, next_row
        new_domains[i] = values     

    if len(list)>0:
        index = randint(0, len(list)-1)
        next_row = list[index]

    return new_domains, False, next_row


# backtracking 
def backtracking(assigned_cells, row, n):
    # If all queens are placed, we are done
    if len(assigned_cells) == n:
        return assigned_cells

    # iterate through all columns for a particular row
    for col in range(n):
        #print(f'backtrack assign before = {assigned_cells} , {len(assigned_cells)}')
        assigned_cells.add((row, col))
        #print(f'assign before = {assigned_cells} , {len(assigned_cells)}')
        if is_safe(row, col, assigned_cells):             
            if backtracking(assigned_cells, row+1, n):
                return assigned_cells

        assigned_cells.remove((row, col))    

#lookahead function
def look_ahead(assigned_cells, domains, unassigned_cells, row, n):
    # If all queens are placed, we are done
    if len(assigned_cells) == n:
        return assigned_cells

    # iterate through all columns for a particular row
    for col in domains[row]:
        assigned_cells.add((row, col))
        #print(f'assign after = {assigned_cells} , {len(assigned_cells)}')
        unassigned_cells.remove(row)        
        new_domains, isempty, next_row = update_domains(assigned_cells, domains, unassigned_cells, n)
        #print(new_domains ,'\n')
        if not isempty:
            #print(f'assignment after not is empty function = {assigned_cells} , {len(assigned_cells)}')
            if look_ahead(assigned_cells, new_domains, unassigned_cells, row + 1, n):                
                return assigned_cells
        #print(f'assignment after is_safe function = {assigned_cells} , {len(assigned_cells)}')
        assigned_cells.remove((row, col))
        unassigned_cells.add(row)


def show_board(assigned_cells, board_size):
    if not assigned_cells:
        print("Zero solution is available")
        return
    board = [['0' for i in range(board_size)]for i in range(board_size)]
    for row, col in assigned_cells:
        board[row][col] = 'Q'
    for row in board:
        print(row)

# returns domains and a set of unassigned_cells
def init(n):
    domains = {}
    unassigned_cells = set()
    for i in range(n):
        unassigned_cells.add(i)
        values = []
        for j in range(n):
            values.append(j)

        domains[i] = values

    return domains, unassigned_cells

#calling the functions
#call the backtracking function
def call_backtracking():
    print("This program will solve n-queens problems by placing letter 'Q' where the queen ought to be placed")
    n =int(input("Enter the Number of Queens: "))
    assigned_cells = set()
    domains, unassigned_cells = init(n)
    start_time = time.time()
    assigned_cells = backtracking(assigned_cells, 0, n)
    time_taken = time.time() - start_time
    print(f"Solution Found, Total Time Taken: {(time_taken)} ") 
    show_board(assigned_cells, n)
    print(f'board size = {n} by {n}\nnum queens = {n}') 
    

def call_look_ahead():
    n =int(input("Enter the Number of Queens: "))
    assigned_cells = set()
    domains, unassigned_cells = init(n)
    start_time = time.time()
    assigned_cells = look_ahead(assigned_cells, domains, unassigned_cells, 0, n)
    time_taken = time.time() - start_time
    print(f"Solution Found, Total Time Taken for forward check: {str(time_taken)} ")         
    show_board(assigned_cells, n)
    print(f'board size = {n} by {n}\nnum queens = {n}')  
    

        
            
      
call_backtracking()          
call_look_ahead()           
          
                
                

           

    
           
