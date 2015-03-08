#***********************************************************************************************
#Name of the project : Matrix Step By Step Calculator
#Description this program is made to take a given matrix to it's row echelon form
#and reduced row echelon form either with showing steps or instantly giving the answer
#Author : Arash Gholami
#Email: a_gholamy777@outlook.com
#Copyright (C) year 2015 
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#**********************************************************************************************************



#This is the windows version which means for refereshing the screen it has system('cls')
from fractions import Fraction
from os import system


class Matrix_modified_init(object):
    def __init__(self, m, n):

        self._m = int(m)
        self._n = int(n)
        self._matrix = []
        for i in range(self._m):
            self._matrix.extend([[]])
            
    def __repr__(self):

        return  repr(self._matrix)

    def __str__(self):

        return self.__repr__()



class Matrix(object):

    def __init__(self):

        while 1:   
            self._m = input('Please enter the number of rows: ')
            if self._m != '':
                break
        
            system('cls')
            
        while 1:
            self._n = input('Please enter the number of columns: ')
            if self._n != '':
                break
            system('cls')
            print('Please enter the number of rows:',self._m)

        self._m = int(self._m)
        self._n = int(self._n)
        self._matrix = []
        for i in range(self._m):
            self._matrix.extend([[]])

        self.initial_matrix()
 

    def __repr__(self):

        return  repr(self._matrix)


    def __str__(self):
        
        return self.__repr__()

    
    def initial_matrix(self):
        
        for row in range(self._m):

            for column in range(self._n):

                self._matrix[row].append('...')

            
    def get_entries(self):

        for row in range(self._m):
            
            for column in range(self._n):
                pointer= (row, column)
                self.matrix_get_anim(pointer[0], pointer[1])
                while 1:
                    entry = input('Please enter an entry for A{row},{col}: '.format(row=row+1,col=column+1))
                    if entry != '':
                        break
                    system('cls')
                                
                self._matrix[row][column] = Fraction(entry)
                 
    def print(self):
        
        entries = []
        num_col = ''
        for row in range(self._m):
        
            for column in range(self._n):
                
                entries.append(len(str(self._matrix[row][column])))


        largest_entry = max(entries)
        

        for row in range(self._m):
            if row == 0:
                new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
            elif row == self._m - 1:
                new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
            else:
                new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
            
            print(new_row.format(*self._matrix[row]))


    def matrix_get_anim(self, row, column):

        i=0
        while i<30:
            system('cls')
            self._matrix[row][column] =  '>.>'
            self.print()
            system('cls')
            self._matrix[row][column] = '<.<'
            self.print()
            i += 1

    def sort_row(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by sorting the rows in an appropriate way.

        >>>sort_row([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])


        '''

        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to
        #to others

            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(len(self._matrix[0])):#this chooses that entry of row to be
            #compared to others
                if notifier == 1:# notifies us if we have already exchanged with
                #appropriate row
                    break
                if self._matrix[idx][idx3] !=0 :#if the entry is not 0 leave it as it is a pivot
                    break
                    
                for idx2 in range(idx + 1, len(self._matrix)):
                #this chooses the other rows in order to be compared with the initial row
                    if self._matrix[idx][idx3] == 0 and self._matrix[idx2][idx3] !=0:#this exchanges the rows

                        for i in range(len(self._matrix[idx])):
                        
                            self._matrix[idx2][i],self._matrix[idx][i] = self._matrix[idx][i],self._matrix[idx2][i]
                     
                        notifier = 1
                        break

                        
    def sub_2rows(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by subtracting the upper rows from
        the rows  below them.

        >>>sub_2rows([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])
        '''
        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to others
        
        
            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(len(self._matrix[0])):#this chooses that entry of row to be compared to others
                if notifier == 1:# notifies us if we have already exchanged with appropriate row
                    break
                
                for idx2 in range(idx + 1, len(self._matrix)):

                
                    if self._matrix[idx][idx3] == 1 and self._matrix[idx2][idx3] == 1:

                        for i in range(len(self._matrix[idx])):
                            self._matrix[idx2][i] -= self._matrix[idx][i]
                        
                        notifier = 1

    def e_operation(self):
        '''(list of lists)

        this is supposed to do the first elementary operation which is deviding
        each entry of the row by the first nonzero entry.

        >>>e_operation_num1([[1, 2, 3], [2, 6, 9], [9, 3, 1]])
        '''

        for idx in range(len(self._matrix)):

            for col_idx in range(len(self._matrix[idx])):  #if the entry is not zero devide that entry and the following by that to maitain a row with pivot

                if  self._matrix[idx][col_idx] == 1   :
                    break
                
                if  self._matrix[idx][col_idx] != 0 :
                    devide_by = self._matrix[idx][col_idx]
                       #devide that entry and the following by the pivot entry then break
                    for col_idx2 in range(len(self._matrix[idx])):
                        self._matrix[idx][col_idx2] = self._matrix[idx][col_idx2] / devide_by
                    break




    '''def check_zero_row(self, row):
        return True if all elements in the row are zero'''

    '''for element in row :

            if element != 0:
                return False

        return True'''

    
    def to_reduced_row(self):

        for row1 in range(len(self._matrix)-1,-1,-1):

            pivot_col = self.find_pivot_column(row1)

            if pivot_col != 0 :#if the row has only zeros ignore it
                
                for row2 in range(row1 -1,-1,-1):

                    multiplicity_of_other_entry = self._matrix[row2][pivot_col]
                
                    for column in range(len(self._matrix[0])):
                    
                        self._matrix[row2][column] -= multiplicity_of_other_entry * self._matrix[row1][column]


    def find_pivot_column(self, row):

        for col in range(len(self._matrix[row])):

            if self._matrix[row][col] == 1:
                
                return  col
        return 0

    def check_row_e(self):
        ''' return True if the matrix is in row echelon form'''
        for idx in range(len(self._matrix[0])):

            num_zero_entries = 0#count the number of pivots that are not zero
            #below pivot entry and including it

            for idx2 in range(idx, len(self._matrix)):

                if abs(self._matrix[idx2][idx]) > 0:
                    num_zero_entries += 1

            if  num_zero_entries > 1 :
                return False

        return True

    
    def iteration(self):
        ''' this is being used to take the matrix to pre row echelon form
	to get to row echelon form after calling this call the following as well
	a.e_operation()
	a.sort_row()
	'''

        while 1:
            self.e_operation()  
            self.sort_row()
            self.sub_2rows()
            if self.check_row_e() == True :
                break

        self.e_operation()

        

    def rank_of_matrix(self):
        ''' return the rank of the matrix(number of pivots)  in ROW ECHELON form
        pivots should be 1'''
        rank = 0#count the number of pivots

        for idx in range(len(self._matrix[0])):

            for idx2 in range(idx, len(self._matrix)):

                if self._matrix[idx2][idx] == 1:
                    rank += 1


        return rank


    def Dimention_matcher(self, matrix2):
        '''return false if the corresponding rows and columns do not match'''
        if self._m == matrix2._m and self._n == matrix2._n:
            
            return True
        
        return False
    
    def __add__(self, matrix2):
        '''return a new matrix representing the addition of the previous ones'''
        '''if len(self._matrix) == 0 or len(self._matrix[0]) == 0 or len(matrix2._matrix) == 0 or len(matrix2._matrix[0]) == 0:
            raise Exception('at least one of the matrices is empty or has an empty row')

        elif len(self._matrix) == 1:
            return'''
        if not self.Dimention_matcher( matrix2):
            raise Exception('non unisized matrices')
        
        a = Matrix_modified_init(self._m, self._n)

        for row in range(len(self._matrix)):

            for col in range(len(self._matrix[0])):

                a._matrix[row].append( self._matrix[row][col] + matrix2._matrix[row][col])

        return a



    def __sub__(self, matrix2):
        '''return a new matrix representing the addition of the previous ones'''
        
        if not self.Dimention_matcher( matrix2):
            raise Exception('non unisized matrices')
        
        a = Matrix_modified_init(self._m, self._n)

        for row in range(len(self._matrix)):

            for col in range(len(self._matrix[0])):

                a._matrix[row].append( self._matrix[row][col] - matrix2._matrix[row][col])

        return a
        



    def __mul__(self, matrix2):
        '''return a new matrix representing the multiplication of the previous ones'''

        if self._n != matrix2._m :
               raise Exception('the number of columns of the first matrix is not equal to number of rows of the second one')

        a = Matrix_modified_init(self._m, matrix2._n)

        for row1 in range(self._m):

            for col2 in range(matrix2._n):

                sum_of_row1Xcol2 = 0

                for col1 in range(self._n):#col1 is the column of 1st and row of the second

                    sum_of_row1Xcol2 += self._matrix[row1][col1] * matrix2._matrix[col1][col2]
			
                a._matrix[row1].append(sum_of_row1Xcol2)

        return a
				
	
				


#----------------------------------instructional----Part-------------------------------------#


    
    def instructional_sort_row(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by sorting the rows in an appropriate way.

        >>>sort_row([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])


        '''

        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to
        #to others

            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(len(self._matrix[0])):#this chooses that entry of row to be
            #compared to others
                if notifier == 1:# notifies us if we have already exchanged with
                #appropriate row
                    break
                if self._matrix[idx][idx3] !=0 :#if the entry is not 0 leave it as it is a pivot
                    break
                    
                for idx2 in range(idx + 1, len(self._matrix)):
                #this chooses the other rows in order to be compared with the initial row
                    if self._matrix[idx][idx3] == 0 and self._matrix[idx2][idx3] !=0 :#this exchanges the rows


                        print('Sorting is about to happen on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                              
                        for i in range(len(self._matrix[idx])):
                        
                            self._matrix[idx2][i],self._matrix[idx][i] = self._matrix[idx][i],self._matrix[idx2][i]
                     
                        notifier = 1
                        
                        print('Sorting happend on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional

                        
                        break
    
    def instructional_sub_2rows(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by subtracting the upper rows from
        the rows  below them.

        >>>sub_2rows([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])
        '''
        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to others
        
        
            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(len(self._matrix[0])):#this chooses that entry of row to be compared to others
                if notifier == 1:# notifies us if we have already exchanged with appropriate row
                    break
                
                for idx2 in range(idx + 1, len(self._matrix)):

                
                    if self._matrix[idx][idx3] == 1 and self._matrix[idx2][idx3] == 1:
                
                        print('Subtracting upper from the lower is about to happenon rows', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                        
                        for i in range(len(self._matrix[idx])):
                            self._matrix[idx2][i] -= self._matrix[idx][i]

                        print('Subtracting just happend on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                        
                        notifier = 1




    def instructional_e_operation(self):
        '''(list of lists)

        this is supposed to do the first elementary operation which is deviding
        each entry of the row by the first nonzero entry.

        >>>e_operation_num1([[1, 2, 3], [2, 6, 9], [9, 3, 1]])
        '''

        for idx in range(len(self._matrix)):

            for col_idx in range(len(self._matrix[idx])):  #if the entry is not zero devide that entry and the following by that to maitain a row with pivot

                if  self._matrix[idx][col_idx] == 1   :
                    break
                
                elif  self._matrix[idx][col_idx] != 0   :

                    print('deviding by the first non_zero entry is about to happen on row:', idx+1)#instructional
                    self.step_by_step_print(idx)#instructional
                        
                    devide_by = self._matrix[idx][col_idx]
                       #devide that entry and the following by the pivot entry then break
                    for col_idx2 in range(len(self._matrix[idx])):
                        self._matrix[idx][col_idx2] = self._matrix[idx][col_idx2] / devide_by

                    print('deviding by the first non_zero entry just happend on row', idx+1)#instructional
                    self.step_by_step_print(idx)#instructional
                    
                    break



    def instructional_to_reduced_row(self):

        for row1 in range(len(self._matrix)-1,-1,-1):

            pivot_col = self.find_pivot_column(row1)
            if pivot_col != 0 :#if the row is only zeroes ignore it
                
                for row2 in range(row1 -1,-1,-1):

                    multiplicity_of_other_entry = self._matrix[row2][pivot_col]

                    print('Subtracting lower from the upper is about to happenon rows', row1+1, 'and', row2)#instructional
                    self.step_by_step_print(row1, row2)#instructional

                    for column in range(len(self._matrix[0])):
                    
                        self._matrix[row2][column] -= multiplicity_of_other_entry * self._matrix[row1][column]

                    print('Subtracting just happend on the following rows:', row1+1, 'and', row2)#instructional
                    self.step_by_step_print(row1, row2)#instructional
                        


    def iteration_for_instructional_functions(self):
        ''' this is being used to take the matrix to pre row echelon form
	to get to row echelon form after calling this call the following as well
	a.e_operation()
	a.sort_row()
	'''

        while 1:
            self.instructional_e_operation()  
            self.instructional_sort_row()
            self.instructional_sub_2rows()
            if self.check_row_e() == True :
                break

        self.instructional_e_operation()


                

    def step_by_step_print(self, a=-1, b=-1):
        
        entries = []
        num_col = ''
        for row in range(self._m):
        
            for column in range(self._n):
                
                entries.append(len(str(self._matrix[row][column])))


        largest_entry = max(entries)
        

        for row in range(self._m):
            if row == 0:
                
                if row == a or row == b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'+ ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
                    
            elif row == self._m - 1:
                
                if row == a or row ==b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']' + ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
            
                
            else:
                if row == a or row ==b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']' + ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + self._n*('{}' +largest_entry * ' ' ) + ']'
            
            print(new_row.format(*self._matrix[row]))
            
        input('press any button to proceed')
        system('cls')



class Augmented_Matrix(Matrix):

    def __init__(self, m=0, n=0, z=0):

        self._m = m
        self._n = n
        self._z = z
        self._n = self._n + self._z
        self._matrix = []
        for i in range(self._m):
            self._matrix.extend([[]])

        self.initial_matrix()


    def dimention_getter(self):

        while 1:   
            self._m = input('Please enter the number of rows: ')
            if self._m != '':
                break
        
            system('cls')
            
        while 1:
            self._n = input('Please enter the number of columns: ')
            if self._n != '':
                break
            system('cls')
            print('Please enter the number of rows:',self._m)

        while 1:
            self._z = input('Please enter the number of columns of the Augmented part: ')
            if self._z != '':
                break
            system('cls')
            print('Please enter the number of rows:',self._m)
            print('Please enter the number of columns:',self._n)

            

        self._m = int(self._m)
        self._z = int(self._z)
        self._n = int(self._n) + self._z


        for i in range(self._m):
            self._matrix.extend([[]])

        self.initial_matrix()

        

    def initial_matrix(self):
        
        for row in range(self._m):

            for column in range(self._n):

                self._matrix[row].append('...')



    def sort_row(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by sorting the rows in an appropriate way.

        >>>sort_row([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])


        '''

        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to
        #to others

            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(self._n - self._z):#this chooses that entry of row to be
            #compared to others
                if notifier == 1:# notifies us if we have already exchanged with
                #appropriate row
                    break
                if self._matrix[idx][idx3] !=0 :#if the entry is not 0 leave it as it is a pivot
                    break
                    
                for idx2 in range(idx + 1, len(self._matrix)):
                #this chooses the other rows in order to be compared with the initial row
                    if self._matrix[idx][idx3] == 0 and self._matrix[idx2][idx3] !=0:#this exchanges the rows

                        for i in range(len(self._matrix[idx])):
                        
                            self._matrix[idx2][i],self._matrix[idx][i] = self._matrix[idx][i],self._matrix[idx2][i]
                     
                        notifier = 1
                        break



    def e_operation(self):
        '''(list of lists)

        this is supposed to do the first elementary operation which is deviding
        each entry of the row by the first nonzero entry.

        >>>e_operation_num1([[1, 2, 3], [2, 6, 9], [9, 3, 1]])
        '''

        for idx in range(len(self._matrix)):

            for col_idx in range(self._n - self._z):  #if the entry is not zero devide that entry and the following by that to maitain a row with pivot

                if  self._matrix[idx][col_idx] == 1   :
                    break
                
                if  self._matrix[idx][col_idx] != 0 :
                    devide_by = self._matrix[idx][col_idx]
                       #devide that entry and the following by the pivot entry then break
                    for col_idx2 in range(len(self._matrix[idx])):
                        self._matrix[idx][col_idx2] = self._matrix[idx][col_idx2] / devide_by
                    break

   

    def sub_2rows(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by subtracting the upper rows from
        the rows  below them.

        >>>sub_2rows([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])
        '''
        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to others
        
        
            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(self._n - self._z):#this chooses that entry of row to be compared to others
                if notifier == 1:# notifies us if we have already exchanged with appropriate row
                    break
                
                for idx2 in range(idx + 1, len(self._matrix)):

                
                    if self._matrix[idx][idx3] == 1 and self._matrix[idx2][idx3] == 1:

                        for i in range(len(self._matrix[idx])):
                            self._matrix[idx2][i] -= self._matrix[idx][i]
                        
                        notifier = 1



    def find_pivot_column(self, row):

        for col in range(self._n - self._z):

            if self._matrix[row][col] == 1:
                
                return  col
        return 0

    
    def to_reduced_row(self):

        for row1 in range(len(self._matrix)-1,-1,-1):

            pivot_col = self.find_pivot_column(row1)
            if pivot_col != 0 :# if the row has only zeros ignore it
                
                for row2 in range(row1 -1,-1,-1):

                    multiplicity_of_other_entry = self._matrix[row2][pivot_col]
                
                    for column in range(len(self._matrix[0])):
                    
                        self._matrix[row2][column] -= multiplicity_of_other_entry * self._matrix[row1][column]



    def check_row_e(self):
        ''' return True if the matrix is in row echelon form'''
        for idx in range(self._n - self._z):

            num_zero_entries = 0#count the number of pivots that are not zero
            #below pivot entry and including it

            for idx2 in range(idx, len(self._matrix)):

                if abs(self._matrix[idx2][idx]) > 0:
                    num_zero_entries += 1

            if  num_zero_entries > 1 :
                return False

        return True


#-------------------------Instructional_Functions------------------------------------------------#

       
    def instructional_sort_row(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by sorting the rows in an appropriate way.

        >>>sort_row([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])


        '''

        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to
        #to others

            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(self._n - self._z):#this chooses that entry of row to be
            #compared to others
                if notifier == 1:# notifies us if we have already exchanged with
                #appropriate row
                    break
                if self._matrix[idx][idx3] !=0 :#if the entry is not 0 leave it as it is a pivot
                    break
                    
                for idx2 in range(idx + 1, len(self._matrix)):
                #this chooses the other rows in order to be compared with the initial row
                    if self._matrix[idx][idx3] == 0 and self._matrix[idx2][idx3] !=0 :#this exchanges the rows


                        print('Sorting is about to happen on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                              
                        for i in range(len(self._matrix[idx])):
                        
                            self._matrix[idx2][i],self._matrix[idx][i] = self._matrix[idx][i],self._matrix[idx2][i]
                     
                        notifier = 1
                        
                        print('Sorting happend on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional

                        
                        break
                         
    def instructional_e_operation(self):
        '''(list of lists)

        this is supposed to do the first elementary operation which is deviding
        each entry of the row by the first nonzero entry.

        >>>e_operation_num1([[1, 2, 3], [2, 6, 9], [9, 3, 1]])
        '''

        for idx in range(len(self._matrix)):

            for col_idx in range(self._n - self._z):  #if the entry is not zero devide that entry and the following by that to maitain a row with pivot

                if  self._matrix[idx][col_idx] == 1   :
                    break
                
                elif  self._matrix[idx][col_idx] != 0   :

                    print('deviding by the first non_zero entry is about to happen on row:', idx+1)#instructional
                    self.step_by_step_print(idx)#instructional
                        
                    devide_by = self._matrix[idx][col_idx]
                       #devide that entry and the following by the pivot entry then break
                    for col_idx2 in range(len(self._matrix[idx])):
                        self._matrix[idx][col_idx2] = self._matrix[idx][col_idx2] / devide_by

                    print('deviding by the first non_zero entry just happend on row', idx+1)#instructional
                    self.step_by_step_print(idx)#instructional
                    
                    break




    def instructional_to_reduced_row(self):

        for row1 in range(len(self._matrix)-1,-1,-1):

            pivot_col = self.find_pivot_column(row1)
            
            if pivot_col != 0 :# if the row has only zeros ignore it
                
                for row2 in range(row1 -1,-1,-1):

                    multiplicity_of_other_entry = self._matrix[row2][pivot_col]

                    print('Subtracting lower from the upper is about to happenon rows', row1+1, 'and', row2+1)#instructional
                    self.step_by_step_print(row1, row2)#instructional
                        
                    for column in range(len(self._matrix[0])):
                    
                        self._matrix[row2][column] -= multiplicity_of_other_entry * self._matrix[row1][column]

                    print('Subtracting just happend on the following rows:', row1+1, 'and', row2+1)#instructional
                    self.step_by_step_print(row1, row2)#instructional
                        

    def instructional_sub_2rows(self):
        '''(list of lists)--->(list of lists)

        this function will modify the Matrix by subtracting the upper rows from
        the rows  below them.

        >>>sub_2rows([[1, 2, 3, 4], [0, 1, 5, 6], [1, 4, 6, 9], [0, 0, 1, 2]])
        '''
        for idx in range(len(self._matrix)):#this chooses the 1 row from top to compare to others
        
        
            notifier = 0 #we want to be notified if we have already exchanged 2 rows

            for idx3 in range(self._n - self._z):#this chooses that entry of row to be compared to others

                if notifier == 1:# notifies us if we have already exchanged with appropriate row
                    break
                
                for idx2 in range(idx + 1, len(self._matrix)):

                
                    if self._matrix[idx][idx3] == 1 and self._matrix[idx2][idx3] == 1:
                
                        print('Subtracting upper from the lower is about to happenon rows', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                        
                        for i in range(len(self._matrix[idx])):
                            self._matrix[idx2][i] -= self._matrix[idx][i]

                        print('Subtracting just happend on the following rows:', idx+1, 'and', idx2+1)#instructional
                        self.step_by_step_print(idx, idx2)#instructional
                        
                        notifier = 1



    def print(self):
        
        entries = []
        num_col = ''
        for row in range(self._m):
        
            for column in range(self._n):
                
                entries.append(len(str(self._matrix[row][column])))


        largest_entry = max(entries)
        

        for row in range(self._m):
            if row == 0:
                new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
            elif row == self._m - 1:
                new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
            else:
                new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
            
            print(new_row.format(*self._matrix[row]))



    def step_by_step_print(self, a=-1, b=-1):
        
        entries = []
        num_col = ''
        for row in range(self._m):
        
            for column in range(self._n):
                
                entries.append(len(str(self._matrix[row][column])))


        largest_entry = max(entries)
        

        for row in range(self._m):
            if row == 0:
                
                if row == a or row == b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'+ ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
                    
            elif row == self._m - 1:
                
                if row == a or row ==b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']' + ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
            
                
            else:
                if row == a or row ==b:
                    new_row = '--> ' + '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']' + ' <--'
                else:
                    new_row = '[' + largest_entry * ' ' + (self._n - self._z)*('{}' +largest_entry * ' ' ) + '|' +largest_entry * ' ' + self._z*('{}' +largest_entry * ' ' ) + ']'
            
            print(new_row.format(*self._matrix[row]))
            
        input('press any button to proceed')
        system('cls')





class Vector(Matrix):

    def __init__(self):

        while 1:   
            self._m = input('Please indicate the Dimention: ')
            if self._m != '':
                break
        
            system('cls')
            

        self._m = int(self._m)
        self._n = 1
        self._matrix = []
        for i in range(self._m):
            self._matrix.extend([[]])

        self.initial_matrix()

    


 
    



                
    

if __name__ == '__main__':

    while 1:
          system('cls')
          print('Welcome to my program\n\n\nMatrix Step By Step Calculator  Copyright (C) 2015  Arash Gholami')
    
          response = input('choose from one of the options bellow:\n>>>>>1)Matrix fast calculator(noninstructional)\n>>>>>2)Step by step solver\n\npress q to exit\n\n----------response = ')

          if response == '1':
              
              while 1:
                  system('cls')
                  print('1)Matrix fast calculator(noninstructional)')
                
                  response = input('choose from one of the options bellow:\n>>>>>1)Regular Matrix\n>>>>>2)Augmented matrix\nor press b to go back to the main menu\n----------response = ')
                  
                  if response == 'b':
                       break
                  if response == '1':
                      
                      while 1:
                          system('cls')
                          print('1)Regular Matrix')
              
                          matrix = Matrix()
                          matrix.get_entries()
                          system('cls')
                          matrix.print()
                          input('press any button to continue')
                          matrix.iteration()
                          print('the row echelon form is:')
                          matrix.print() 
                          input('press any button to go to reduced row')
                          matrix.to_reduced_row()
                          print('the reduced row echelon form is:')
                          matrix.print()
                          response = input('press b to go back or any button to try again\n---------response = ')
                          if response == 'b':
                               break


                  if response == '2':

                      while 1:
                          system('cls')
                          print('Augmented Matrix')

                          matrix = Augmented_Matrix()
                          matrix.dimention_getter()
                          matrix.get_entries()
                          system('cls')
                          matrix.print()
                          input('press any button to continue')
                          matrix.iteration()
                          print('the row echelon form is:')
                          matrix.print() 
                          input('press any button to go to reduced row')
                          matrix.to_reduced_row()
                          print('the reduced row echelon form is:')
                          matrix.print()
                          response = input('press b to go back or any button to try again\n---------response = ')
                          if response == 'b':
                               break

                  


#--------------------Second option _-------------------------------------------------------------------------------------------------




          if response == '2':
              
              while 1:
                  system('cls')
                  print('2)Step by step solver')
                
                  response = input('choose from one of the options bellow:\n>>>>>1)Regular Matrix\n>>>>>2)Augmented matrix\nor press b to go back to the main menu\n---------response = ')
  
                  if response == 'b':
                       break
                  if response == '1':
                      
                      while 1:
                          system('cls')
                          print('1)Regular Matrix')
              
                          matrix = Matrix()
                          matrix.get_entries()
                          system('cls')
                          matrix.print()
                          input('press any button to continue')
                          matrix.iteration_for_instructional_functions()
                          print('the row echelon form is:')
                          matrix.print() 
                          input('press any button to go to reduced row')
                          matrix.instructional_to_reduced_row()
                          print('the reduced row echelon form is:')
                          matrix.print()
                          response = input('press b to go back or any button to try again\n---------response = ')
                          if response == 'b':
                               break


                  if response == '2':

                      while 1:
                          system('cls')
                          print('Augmented Matrix')

                          matrix = Augmented_Matrix()
                          matrix.dimention_getter()
                          matrix.get_entries()
                          system('cls')
                          matrix.print()
                          input('press any button to continue')
                          matrix.iteration_for_instructional_functions()
                          print('the row echelon form is:')
                          matrix.print() 
                          input('press any button to go to reduced row')
                          matrix.instructional_to_reduced_row()
                          print('the reduced row echelon form is:')
                          matrix.print()
                          response = input('press b to go back or any button to try again\n---------response = ')
                          if response == 'b':
                               break

                 
          if response == 'q':
              break


                          
                          

               
    
    '''a=Augmented_Matrix()
    a.dimention_getter()
    a.get_entries()
    system('cls')
    a.print()

    #a.iteration()
    a.iteration_for_instructional_functions()
    #a.e_operation()#to reach row echelon form
    #a.instructional_sort_row()
    #a.sort_row()
    input('now row reduced operation')
    a.instructional_to_reduced_row()


    #a.to_reduced_row()
    #a.sort_row()
    #print(a.rank_of_matrix())
       
    a.print()
    b= input()'''
