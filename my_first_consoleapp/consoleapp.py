import requests
import sys
import json
def main():
  # res = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
  # print(res.text)
  if len(sys.argv) < 2:
    print("Usage: This Program uses at least one parameter, to return the responseText of a http-get on the url, specified as the first parameter. Please try again...")
    exit()
  elif len(sys.argv) == 2:
    url_to_open = sys.argv[1]
    res = requests.get(url_to_open)
    print(json.dumps(res.json(), indent=2))
    
  

  print(sys.argv)
  


  

if __name__ == '__main__':
  main()