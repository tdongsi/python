'''
This module requires Datastax's Python driver

http://datastax.github.io/python-driver/installation.html

@author: tdongsi
'''

import MyLogger
import logging
from cassandra.cluster import Cluster

# create logger
myLogger = logging.getLogger('JmxRecord')

def recordCsv( csvFile, host, keyspace, table ):
    '''
    Record data from a CSV file into a Cassandra table.
    Use the CQL commands to create keyspace/table and insert values.
    
    The first column of the table will be sampleNo, followed by each column named
    corresponding to the headers in CSV file.
    '''
    
    try:
        with open( csvFile, "r" ) as f:
            lines = f.readlines()
            
        cluster = Cluster([host])
        session = cluster.connect()
        
        headerList = lines[0].strip().split(',')
        
        try:
            cmd = "DROP KEYSPACE %s" % keyspace
            myLogger.debug("CQL: %s", cmd)
            session.execute(cmd)
        except Exception:
            # Keyspace probably not existent
            myLogger.debug('Error executing %s', cmd)
        
        cmd = "CREATE KEYSPACE %s WITH REPLICATION = " \
            "{ 'class' : 'SimpleStrategy', 'replication_factor' : 3 }" % keyspace
        myLogger.debug("CQL: %s", cmd)
        session.execute(cmd)
        
        cmd = "CREATE TABLE %s.%s " % (keyspace, table)
        columnName =  "(sampleNo int PRIMARY KEY, {0} int, {1} int, {2} float) ".format(*headerList)
        cmd = cmd + columnName
        myLogger.debug("CQL: %s", cmd)
        session.execute(cmd)
        
        for idx in xrange(1,len(lines)):
            cmd = "INSERT INTO %s.%s " % (keyspace, table)
            cmd = cmd + "(sampleNo, %s) " % lines[0].strip() + \
                "VALUES (%d,%s)" % (idx,lines[idx].strip())
            myLogger.debug("CQL: %s", cmd)
            session.execute(cmd)
        
        session.shutdown()
        cluster.shutdown()
    except IOError:
        myLogger.error( 'Error opening file %s', csvFile )
    except Exception:
        myLogger.error('Error recording CSV file into a Cassandra Table')

def main():
    # Testing
    recordCsv('jmxMetrics.csv', 'localhost', 'JmxKeyspace', 'JmxRecord')

if __name__ == "__main__":
    ''' Usage: See the top comment for usage of this module.'''
    print 'Running the script'
    
    main()