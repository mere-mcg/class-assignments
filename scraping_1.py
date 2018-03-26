import urllib2, csv
#Import urllib2 is a Python module that lets you download web pages. CSV (comma separated values) is a file type, which allows data to be saved in a table format. This line is instructing to import a CSV file form a URL.  

from bs4 import BeautifulSoup
#Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with a parser. bs4 is the fourth version of Beautiful Soup. This line is importing the Beautiful Soup library. Beautiful Soup is mainly used to extract tables, lists and paragraphs and also allows you to put filters on to extract information from web pages. It doesn't actually fetch the web page. That's why urllib2 is used in combination with it.

outfile = open('jaildata.csv', 'w')
#This line creates a file object, which links Python to my computer's file system. The parameter 'jaildata.csv' names the file. The second parameter is how we will use the file. In this case, 'w' is short for writing. By writing this line of code, we're saying we're creating and writing a file.

writer = csv.writer(outfile)
#This line will convert the imported csv file data into delimited strings. 

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#Here, we're storing the URL of the website I'm working with in a variable. 

html = urllib2.urlopen(url).read()
#On this line, we're now opening the file from the URL we've declared and reading its HTML. 

soup = BeautifulSoup(html, "html.parser")
#This line parses the data we've pulled and puts it in a variable called soup. 

tbody = soup.find('tbody', {'class': 'stripe'})
#We're instructing Beautiful Soup to go through the data in the variable soup and find strings tagged by 'tbody' with the class 'stripe' and store in a variable called tbody. 

rows = tbody.find_all('tr')
#Here, we're creating a variavle called rows and searching through our new variable tbody to find all strings tagged with 'tr'. 

for row in rows:
#This instructs the program to iterate over rows. It loops through each row of data.

    cells = row.find_all('td')
 	#Find all of the rows that are tagged with 'td', and save them in a variable called cells.

    data = []
    #This is an assignment that means the variable data is refering to an empty list.

    for cell in cells:
 	#This instructs the program to iterate over cells. It will loop through each individual cell. 

        data.append(cell.text)
        #Here, we're telling the program that we will be appending the variable data by adding an object to the list (cell.text). 

    writer.writerow(data)
    #This writes all of our data that we've imported into the list called data that we've created.