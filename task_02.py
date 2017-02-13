import sys
import copy
import os


# Version 1
# Naive, recursion.
# Time complexity: O(2^n)

def find_rec(T, src_r, src_c, dest_r, dest_c, path_cost):
    '''
    Args:
        T: LIST - list of INT/FLOATs being a cost of visiting the point.
        src_r: INT - row number of the point where we start
        src_c: INT - col number of the point where we start
        dest_r: INT - row number of the point we want to visit
        dest_c: INT - col number of the point we want to visit
        path_cost: INT/FLOAT - curent path cost to the (src_r, src_c) point
    Output:
        INT/FLOAT - minimum path value from point (src_r, src_c) to (dest_r, dest_c)

    '''
    if src_r == len(T) or src_c == len(T[src_r]):
        return float('inf')
    if src_r == dest_r and src_c == dest_c:
        return path_cost + T[dest_r][dest_c]
    down = find_rec(T, src_r + 1, src_c, dest_r, dest_c, path_cost + T[src_r][src_c])
    right = find_rec(T, src_r, src_c + 1, dest_r, dest_c, path_cost + T[src_r][src_c])
    return min(down, right)
    
    



# Version 2
# Dynamic approach
# Time complexity: O(n^2)

def find_dynamic(T, dest_r, dest_c):
    '''
    Args:
        T:list - list of INT/FLOATs being a cost of visiting the point.
        dest_r: INT - row number of the point we want to visit
        dest_c: INT - col number of the point we want to visit
    Output:
        INT/FLOAT - minimum path value from point (0, 0) to (dest_r, dest_c)

    '''
    local_cost_tab = copy.deepcopy(T)
    # update costs of first row
    for c in range(1, dest_r + 1):
        local_cost_tab[0][c] = local_cost_tab[0][c - 1] + local_cost_tab[0][c]

    # update costs of first column
    for r in range(1, dest_c + 1):
        local_cost_tab[r][0] = local_cost_tab[r - 1][0] + local_cost_tab[r][0]

    # find min cost for each row and col, from 1, 1 to destination row and destination column
    for r in range(1, dest_r + 1):
        for c in range(1, dest_c + 1):
            local_cost_tab[r][c] = min(local_cost_tab[r - 1][c], local_cost_tab[r][c - 1]) + local_cost_tab[r][c]
    return local_cost_tab[dest_r][dest_c]
        

try:
    filepath = sys.argv[1]
except IndexError as e:
    print("Script requires input filepath as a mandatory argument!")
    exit()
else:
    # Ustawiamy defaultowy separator danych
    data_sep = ','
    # Oddzielamy sciezke pliku od nazwy pliku
    path, filename = os.path.split(filepath)
    # Dane wyjsciowe zapisywac bedziemy do pliku z ta sama nazwa, w rozszerzeniu .out
    outpath = os.path.join(path, filename + '.out')    
    with open(filepath, 'r') as infile, open(outpath, 'w') as outfile:
        # Tworzymy iterator linii
        fl_iter = iter(infile.readlines())
        try:
            # Dopoki mozna odczytywac linie
            while True:
                array = []
                # Odczytaj informacje o wielkosci macierzy
                size = int(next(fl_iter))
                # Zbierz kolejnych SIZE-rzedow, zapisujac je do array
                for _ in range(size):
                    array.append(list(map(int, next(fl_iter).split(data_sep))))
                # Uruchom funkcje, za docelowe wspolrzedne wybierajac prawy, dolny rog
                result = find_dynamic(array, dest_r = len(array) - 1, dest_c = len(array) - 1)
                # Wynik zapisz w pliku wyjsciowym
                outfile.write(str(result) + '\n')
        # Kiedy iterator skonczy prace, zwroci StopIteration error, ktory przejmujemy
        except StopIteration as e:
            print("Zakonczono powodzeniem.")
            
