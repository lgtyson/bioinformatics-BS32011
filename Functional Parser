# -*- coding: iso-8859-1 -*-
#takes the raw data file and creates 4 text files that can each be loaded into a table in mySQL
#!/usr/bin/python



infile = "GDS5093_full.soft" #This defines the name of the file to be opened as the infile, in this case my dataset from GEO

fh = open(infile)            #This opens the infile


line= fh.readline()          #Reads the lines defined
while line[:20] != '!dataset_table_begin':    #This sets the first line to be read by the script and opened into the files.
   line=fh.readline()

header= fh.readline().strip()                 #Strips the file header
colnames={}                                   # This captures the column names
index=0                                       #Sets the index value to 0 and begins the counter
for title in header.split('\t'):
  colnames[title]=index
  print '%s\t%s'%(title,index)
  index=index+1                             # Adds +1 to the index counter for each column read





genefile=open('genes.txt', 'w')               #The following three lines open the output files for each class, creating one per table
expressionfile=open('expression.txt','w')
probefile=open('probes.txt', 'w')

genefields=['Gene ID', 'Gene symbol', 'Gene title']  #This defines which columns go to which output file, this is done by assigning fields to the the headers, more can always be added by adding more fields and output files accordingly
samples=header.split('\t')[2:int(colnames['Gene title'])] #Removes the header and writes the line in a table format into the appropriate file text
probefields=['ID_REF','Gene ID']               #Identifiers for the new line by its header



#This is to take out columns from a new row
def buildrow(row, fields):
 '''Creates a tab separated list of values according to the columns listed in fields
      row: a list of values...... Pulls out from a row the selected columns 
      fields: a list of columns. Only the values in row corresponding to the columns in fields are output
        returns: A string that is a tab separated list of values terminated with a newline
        '''
    newrow=[]     # Creates a new row
    for f in fields:      #searches for
        newrow.append(row[int(colnames[f])])
    return "\t".join(newrow)+"\n"   #Enters the line, resetting the sequence until the whole file is read

#The following creates the rows for the expression file
row_count=0                            #Starts the row counter, set at value 0
def build_expression(row, samples):
    '''Builds tab separated rows for expression data. For each of the samples listed 
        it generates a line with the probe id, sample id and expression value.
        row: a list of values
        samples: a list of column headings corresponding to the samples
        '''
    exprrows=[]
    for s in samples:
        newrow=[s,]
        newrow.append(row[int(colnames['ID_REF'])]) # Add probe name
        newrow.append(row[int(colnames[s])])         # Add row name
        exprrows.append("\t".join(newrow))
    return "\n".join(exprrows)+"\n"                 



for line in fh.readlines():
    try:
        if line[0]=='!': 
              continue
        row=line.strip().split('\t') 
        genefile.write(buildrow(row, genefields))
        probefile.write(buildrow(row,probefields)) # Creates row for genes, and probe files
        expressionfile.write(build_expression(row, samples))
        row_count=row_count+1 #Adds +1 to the row counter
    except:
        pass



# The following three lines closes the newly created files

genefile.close()
probefile.close()
expressionfile.close()


print '%s row_count'%row_count        # This prints the row counter

