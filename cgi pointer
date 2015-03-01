#!/usr/local/bin/python     #set appropriate directory
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # Ends headers
print "<html><head><TITLE>CGI script output</TITLE></head>"  #Prints the entered script
print "<body><H1>Form values</H1>"
print "<table><tr><th>Key</th><th>Value</th></tr>"

for k in form.keys():
        print "<tr><td>%s</td><td>%s</td></tr>"%(k, form[k])

print "<table>"

print "</body></html>"

sql="SELECT expression from expression e inner join gene g on e.gene_id=g.gene-id where gene-id= %s"

db=MySQLdb.connect(....)
cursor=db.cursor()
cursor.execute(sql,form[geneid].value)

gene=Gene (form[geneid].value)
results=gne.getExpression()

print "<table><th>Sample</th><th?Expression</th></tr>"
for exp in results:
    print "<tr><td>%s</td><td>%s</td></tr>"%exp

print "</table>"

print "</table>"

print "</body></html>"
