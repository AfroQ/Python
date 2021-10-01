# 
# Example file for parsing and processing HTML
#
import os
from html.parser import HTMLParser

metacount = 0;

class MyHTMLParser(HTMLParser):
  def handle_comment(self, data):
    print("Encountered comments: ", data)
    pos = self.getpos()
    print("\tAt line", pos[0], " position", pos[1])
  
  def handle_starttag(self, tag, attrs):
    if tag == 'meta':
      global metacount
      metacount +=1
    print("Encountered comments: ", tag)
    pos = self.getpos()
    print("\tAt line", pos[0], " position", pos[1])

    if len(attrs) > 0:
      print("\tAttributes:")
      for a in attrs:
        print("", a[0], " = ", a[1])

  def handle_endtag(self, tag):
    print("Encountered tag: ", tag)
    pos = self.getpos()
    print("\tAt line", pos[0], " position", pos[1])
  
  def handle_data(self, data):
    if data.isspace():
      return
    print("Encountered data: ", data)
    pos = self.getpos()
    print("\tAt line", pos[0], " position", pos[1])
    
    print("Meta tags found: " + str(metacount))

def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  #filename = "samplehtml.html"
  f = open(os.path.join("C:/Users/nyaku/OneDrive/Desktop/Programming/Python/Ex_Files_Learning_Python_Upd/Exercise Files/Ch5/samplehtml.html"))
  if f.mode == 'r':
    contents = f.read()
    parser.feed(contents)
    

if __name__ == "__main__":
  main();
  