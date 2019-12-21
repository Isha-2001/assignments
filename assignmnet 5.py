
from __future__ import with_statement
import contextlib
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import sys
import os
import csv
def make_tiny(url):
  request_url = ('http://tinyurl.com/api-create.php?' +
  urlencode({'url':url}))
  with contextlib.closing(urlopen(request_url)) as response:
      return response.read().decode('utf-8')

def main():
    Url=input("enter list of urls ")
    urls=Url.split()
    tinyurl=[]
    for url in urls :
        tinyurl = make_tiny(url)
        print(tinyurl)
    tl = tinyurl.split()
    currentdir=os.path.dirname(__file__)
    filename=os.path.join(currentdir,"url.txt")
    with open(filename,'w') as file:

          fieldnames=['url','surl']
          writer=csv.writer(file)
          writer.writerow(fieldnames)
          row=0
          while row!=len(urls):
            Row=[urls[row],tl[row]]
            writer.writerow(Row)
            row+=1

    short=input("enter the short url to be searched : ")
    with open(filename,'r') as file:
    #row=file.readline()

        reader=csv.reader(file)
        line=0
        for row in reader:
            if line!=0:
                if (line%2)==0:
                    st=row[1]
                    if st==short:
                        print({row[0]})
            line+=1

main()
#def make_tiny(url):
#	request_url = ('http://tinyurl.com/api-create.php?' +
#	urlencode({'url':url}))
#	with contextlib.closing(urlopen(request_url)) as response:
#		return response.read().decode('utf-8')