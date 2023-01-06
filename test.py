from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir("D:\LastVersionScrapper\BauAnalizer2\Analysis") if isfile(join("D:\LastVersionScrapper\BauAnalizer2\Analysis", f))]
print("The Files Found = " ,onlyfiles )