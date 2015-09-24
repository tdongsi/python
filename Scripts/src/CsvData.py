'''
Created on Sep 23, 2015

@author: cdongsi
'''

import csv

def generateUpdateStatement(input_file, output_file):
    # %s after set is the mapping column_name=column_value
    template = "UPDATE %s SET %s WHERE qbo_region_id=%s and %s is null;"
    
    table_name = 'dim_region'
    column_names = ['finance_chart_of_accounts_region',
                    'finance_enterprise_performance_management_region',
                    'finance_revenue_region']
    
    
    try:
        with open(input_file) as input, open(output_file, 'w') as output:
            output.truncate()
            reader = csv.reader(input)
            
            # The first line is the header
            header = reader.next()
            value_index = [0,4,3]
            print [header[i] for i in value_index]
            
            for row in reader:
                print [row[i] for i in value_index]
                
                column_to_value_strings = ["%s='%s'" % (column_names[i],row[value_index[i]]) for i in range(3)]
                set_values = ','.join(column_to_value_strings)
                id_value = row[1]
                
                command_string = template % (table_name, set_values, id_value, column_names[0])
#                 print command_string
                output.write( command_string )
                output.write("\n")
                
                
                
    except IOError:
        print 'Error reading file %s or opening %s' % (input_file, output_file)
    

def main():
    '''
    Read CSV data and manipulate it.
    '''
    inputfile = '../data/test_data.csv'
    outputfile = 'out.txt'
    
    generateUpdateStatement(inputfile,outputfile)
    

if __name__ == '__main__':
    main()