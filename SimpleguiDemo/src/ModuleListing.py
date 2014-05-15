'''
Created on May 14, 2014

@author: tdongsi
'''

import simpleguitk as simplegui

def info(object, spacing = 20, collapse = 1):
    """ Print methods and doc strings"""
    methodList = [method for method in dir(object) if callable(getattr(object,method))]
    
    processFunc = (lambda s: " ".join(s.split())) if collapse else (lambda s: s)
    
    print "\n".join( [ "%s %s" % 
                      (method.ljust(spacing), 
                       processFunc(str(getattr(object, method).__doc__))) 
                      for method in methodList] )

if __name__ == '__main__':
    info(simplegui)