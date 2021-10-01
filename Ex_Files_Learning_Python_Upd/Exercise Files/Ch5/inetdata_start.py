# 
# Example file for retrieving data from the internet
#
import urllib.request # needed to make http requests

def main():
  webUrl = urllib.request.urlopen("https://www.google.com")
  print("result code: " + str(webUrl.getcode())) #see if you can connect with website without errors
  data = webUrl.read()
  print(data)

  
if __name__ == "__main__":
  main()
