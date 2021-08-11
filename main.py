print("loading...")
import requests
import random
wanna = "yes"
while "y" in wanna:
  PROJECT_ID = str(random.randint(1, 559645340))
  url = 'https://projects.scratch.mit.edu/' + PROJECT_ID
  print("chosen project \"" + url + "\"")
  rup = requests.get(url, allow_redirects=True)
  inpat = input("yo! wanna download this random project? ")
  if "y" in inpat:
    if "[40" in rup: 
      print("failure to download")
    else:
      open('RandomProject' + PROJECT_ID + '.json', 'wb').write(rup.content)
  wanna = input("wanna download another? ")
