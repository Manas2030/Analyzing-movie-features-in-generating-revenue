import os
os.system("pip install gdown")
currdir = os.getcwd() 
newdir = currdir + "/data"
os.chdir(newdir) 
os.system("gdown https://drive.google.com/uc?id=1E3cZYOdVT3-FQuaZqrjStkLM5wv4MgOc")
os.chdir(currdir) 

