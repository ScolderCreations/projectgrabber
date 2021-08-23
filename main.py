print("loading...")
import requests
import random
wanna = "yes"
pre = input("press enter ")
while "y" in wanna:
  if len(str(pre)) > 1:
    PROJECT_ID = str(pre)
  else:
    PROJECT_ID = str(random.randint(1, 559647000))
  url = 'https://projects.scratch.mit.edu/' + PROJECT_ID
  print("chosen project \"" + url + "\"")
  rup = requests.get(url, allow_redirects=True)
  inpat = input("yo! wanna download this random project? ")
  if "y" in inpat:
    if "[40" in rup: 
      print("failure to download")
    else:
      open(PROJECT_ID, 'wb').write(rup.content)
  wanna = input("wanna download another? ")
  print("done!")
