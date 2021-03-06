#!/usr/bin/python
import MySQLdb
#None functioning script for a database to use filehandlers of the datasets created in tables to deal with a selected gene.



class DBHandler():        #this finds the file handler, resulting in only the needed resources being used, and not additional
    '''The static database connection - avoids overuse of resources'''
    connection=None
    dbname='XXXXXXXX'     # replace X with MySQL user name
    dbuser='XXXXXXXX'     # replace X with MySQL user name
    dbpassword='RRRRRRRRRRRRR'    # replace R with MySQL user password

    def __init__(self):      #initiates the database, establishes the connection
        if DBHandler.connection == None:
            DBHandler.connection = MySQLdb.connect(db=DBHandler.dbname, user=DBHandler.dbuser, passwd=DBHandler.dbpassword)

    def cursor(self):
        return DBHandler.connection.cursor()

class Gene():   #first class from the parser, this is currently set to gene
   
    Gene_Symbol=''
    Gene_Title=''
    Gene_ID=''
    probelist=[] #insert probes from parser/ database

    def __init__(self,Gene_ID):    #initiates handler for gene
        '''Init method for Gene'''
        db=DBHandler()     #sets handler to that of the gene file
        self.Gene_ID=Gene_ID        
        cursor=db.cursor()
        sql='SELECT Gene_Title, Gene_Symbol FROM Genes WHERE Gene_ID=%s'
        cursor.execute(sql,(Gene_ID,)) #queries the database for the handler
        result=cursor.fetchone()
        self.Gene_Title =result[0]
        self.Gene_Symbol=result[1]

        
        probesql='SELECT Gene_ID FROM Probes WHERE Gene_ID=%s'  # sets the search to select and return the probes
        cursor.execute(probesql,(Gene_ID,))

        #Needs completing
        for result in cursor.fetchall():
            self.probelist.append(result[0])

    def get_expression(self, Sample_ID):   #same as above but for expression
        db=DBHandler()
        cursor=db.cursor()
        sql='SELECT Expression_value FROM Expression WHERE ID_REF=%s AND Sample_ID=%s'
        cursor.execute(sql,(Sample_ID,))
        result=cursor.fetchone()
        self.Gene_Title =result[0]
        self.Gene_Symbol=result[1]
        return result

print('Finished')    #prints this title when search is complete
            
#script is still incomplete and needs finishing
