import random
import os
import fpdf
from datetime import datetime,timedelta
files = []

turns = ['leftright','updown','dup','ddown']

for x in os.listdir():
    if x.endswith('.txt'):
        if 'Arial.pkl' in os.listdir():
            os.remove('Arial.pkl')

        pdf = fpdf.FPDF('P', 'mm', 'A4')
        pdf.set_auto_page_break(0)
        pdf.add_page()
        path = os.path.abspath('Fonts/Arial.ttf')
        f = pdf.add_font('AR','',path,uni=True)
        pdf.set_font('AR','',size = 12)

        filename = x
        words = [line.strip() for line in open(f'{filename}')]
        words = [str(x) for x in words if x.strip()]
        grid_size_x = int(input('Enter the GRID X Horizontal Size: '))
        grid_size_y = int(input('Enter the GRID Y Vertical Size: '))
        dict_ = str(input('Enter the Dictionary Values with a Space: '))
        dict_ = list(dict_)
        dict_ = [x for x in dict_ if not x == ' ']

        grid = [[' ' for _ in range(grid_size_x + 1)] for _ in range(grid_size_y + 1)]
        for word in words:
            while True:
                if len(word) >= grid_size_y or len(word) >= grid_size_x:
                    print(F'!! {word} size cannot fit inside the grid positions. Please Enter a new size ')
                    grid_size_x = int(input('Enter the GRID X Horizontal Size: '))
                    grid_size_y = int(input('Enter the GRID Y Vertical Size: '))
                
                else:
                    break

            word_length = len(word)
            placed = False

            while not placed:
                turn = random.choice(turns)

                if turn == 'leftright':
                    x_step = 1
                    y_step = 0

                if turn == 'updown':
                    x_step = 0
                    y_step = 1

                if turn == 'ddown':
                    x_step = 1
                    y_step = 1

                if turn == 'dup':
                    x_step = 1
                    y_step = -1
                
                x_pos = random.randrange(grid_size_x)
                x_pos = x_pos - 1 if x_pos > grid_size_x else x_pos
                y_pos = random.randrange(grid_size_y)
                y_pos = y_pos - 1 if y_pos > grid_size_y else y_pos

                end_x = x_pos + word_length*x_step
                end_y = y_pos + word_length*y_step

                if end_x < 0 or end_x >= grid_size_x:
                    continue

                if end_y < 0 or end_y >= grid_size_y:
                    continue        

                failed = False
                for i in range(word_length):
                    char = word[i]

                    new_pos_x = x_pos + i*x_step
                    new_pos_y = y_pos + i*y_step
                    char_at_pos = grid[new_pos_x][new_pos_y]
                    
                    if char_at_pos != ' ':
                        if char_at_pos == char:
                            continue
                        else:
                            failed = True
                            break
                
                if failed:
                    continue
                else:
                    for i in range(word_length):
                        char = word[i]
                        new_pos_x = x_pos + i*x_step
                        new_pos_y = y_pos + i*y_step
                        grid[new_pos_x][new_pos_y] = char
                    
                    placed = True
                

        for x in range(grid_size_x + 1):
            pdf.write(5,'  '.join(grid[x]) + "\n" ) 

        pdf.output(f"{filename.replace('.txt','')}_SOLUTION.pdf")
        print(f"Generated: {filename.replace('.txt','')}_SOLUTION.pdf")
        for x in range(grid_size_x + 1):
            for y in range(grid_size_y + 1):
                if grid[x][y] == ' ':
                    grid[x][y] = random.choice(dict_).upper()
        
        pdf = fpdf.FPDF('P', 'mm', 'A4')
        pdf.set_auto_page_break(0)
        pdf.add_page()
        path = os.path.abspath('Fonts/Arial.ttf')
        pdf.add_font('AR','',path,uni=True)
        pdf.set_font('AR','',size = 12)

        for x in range(grid_size_x + 1):
            print('\t'*5 + ' '.join(grid[x]))
            pdf.write(5,'  '.join(grid[x]) + '\n') 

        pdf.output(f"{filename.replace('.txt','')}.pdf")
        print(f"Generated: {filename.replace('.txt','')}.pdf")
        

input()






