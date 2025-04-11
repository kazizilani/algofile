#Longest Common Subsequence Using Dynamic Programming

def locos(sequence_x, sequence_y):
    length_sequence_x = len(sequence_x)
    length_sequence_y = len(sequence_y)
    
    addtional_cells = 1
    total_rows = length_sequence_x + addtional_cells
    total_colls = length_sequence_y + addtional_cells


    table = []
    for i in range(total_rows):
        row = []
        for j in range(total_colls):
            row.append(0)
        table.append(row)


    # go through all the rows to compare every word that is 
    for row_index in range(total_rows):
        for coll_index in range(total_colls):

            #current letter in the sequence too
            previous_row_index = row_index - 1
            previous_coll_index = coll_index - 1


            #skip the 0th row and column        
            if row_index == 0 or coll_index == 0:
                table[row_index][coll_index] = 0
            
            # if the latter in two sequence matches then 
            # add 1 with the value from the left diagonal cell and store in the current cell
            elif sequence_x[previous_row_index] == sequence_y[previous_coll_index]:
                table[row_index][coll_index] = table[previous_row_index][previous_coll_index] + 1

            # if the letters do not match
            # choose the maximum value between from the immideate upper or immideate left cell
            else:
                table[row_index][coll_index] = max(table[previous_row_index][coll_index], table[row_index][previous_coll_index])
    
    

    # as last row + coll is where we find the longest subsequence length of the entire sequence
    last_cell_value = table[length_sequence_x][length_sequence_y]
    sequence_length = last_cell_value
    

    # we are backtracking to reconstruct the subsequence
    longest_common_sequence = []

    while length_sequence_x > 0 and length_sequence_y > 0: 
        # like before, it's the accessable sequence length
        current_row = length_sequence_x
        current_coll = length_sequence_y
        sequence_x_last_index = previous_row = length_sequence_x - 1
        sequence_y_last_index = previous_coll = length_sequence_y - 1

        # if the last avaible index is same in both
        if sequence_x[sequence_x_last_index] == sequence_y[sequence_y_last_index]:
            # if so, then insert the character in the array 
            longest_common_sequence.append(sequence_x[sequence_x_last_index])
            
            #then jumping to upper left cell (diagonal cell)
            length_sequence_x -=1
            length_sequence_y -= 1
        
        # checiking if the value of the upper cell larger or equal to lef cell
        elif table[previous_row][current_coll] >= table[current_row][previous_coll]:
            #if so, jumping to upper cell
            length_sequence_x -=1
        else:
            #if not, then jumping to the left cell
            length_sequence_y -=1
    
    # reversing the array to get the og value
    longest_common_sequence.reverse()

    # just printed the table for easier comprehension
    for row in table:
        print(row)
    
    # stringify the sequence and return
    return sequence_length, ''.join(longest_common_sequence)
            

# take input two strings
sequence_x = input("Enter Sequence X: ")
sequence_y = input("Enter Sequence Y: ")

# deconstruct the function
length, sequence = locos(sequence_x, sequence_y)

# print the function
print(f"Length of Longest Common Subsequence: {length}")
print(f"The Longest Common Subsequence: {sequence}")