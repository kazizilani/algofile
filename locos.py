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


    for row_index in range(total_rows):
        for coll_index in range(total_colls):
            previous_row_index = row_index - 1
            previous_coll_index = coll_index - 1
            
            if row_index == 0 and coll_index == 0:
                table[row_index][coll_index] = 0
            
            elif sequence_x[previous_row_index] == sequence_y[previous_coll_index]:
                table[row_index][coll_index] = table[previous_row_index][previous_coll_index] + 1
            else:
                table[row_index][coll_index] = max(table[previous_row_index][coll_index], table[row_index][previous_coll_index])


    last_cell_value = table[length_sequence_x][length_sequence_y]
    sequence_length = last_cell_value
    
    longest_common_sequence = []
   

    while length_sequence_x > 0 and length_sequence_y > 0: 
        sequence_x_last_index = length_sequence_x - 1
        sequence_y_last_index = length_sequence_y - 1

        if sequence_x[sequence_x_last_index] == sequence_y[sequence_y_last_index]:
            longest_common_sequence.append(sequence_x[sequence_x_last_index])
            length_sequence_x -=1
            length_sequence_y -= 1
        
        elif table[sequence_x_last_index][length_sequence_y] >= table[length_sequence_x][sequence_y_last_index]:
            length_sequence_x -=1
        else:
            length_sequence_y -=1
    
    longest_common_sequence.reverse()
    
    return sequence_length, ''.join(longest_common_sequence)
            

sequence_x = input("Enter Sequence X: ")
sequence_y = input("Enter Sequence Y: ")

length, sequence = locos(sequence_x, sequence_y)


print(f"Length of Longest Common Subsequence: {length}")
print(f"The Longest Common Subsequence: {sequence}")