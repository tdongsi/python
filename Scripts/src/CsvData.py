'''
Created on Sep 23, 2015

@author: cdongsi
'''

import csv

def main():
    '''
    Read CSV data and manipulate it.
    '''
    filename = '../data/test_data.csv'
    
    try:
        with open(filename) as file:
            reader = csv.reader(file)
            
            # The first line is the header
            header = reader.next()
            
            for row in reader:
                print ':'.join(row)
                
                
                
    except IOError:
        print 'Error reading file %s' % filename

if __name__ == '__main__':
    main()