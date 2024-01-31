import os 

path = os.getcwd() +'\chrome_driver\chromedriver.exe'

env = { "driver" : f"{path}" }

print(path)