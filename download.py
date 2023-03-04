import glob
from utils import *
from scraper import *

in_file = glob.glob("*.html")
i = 0

for row in in_file:


    print(i,len(in_file))
    website = open(row, mode="r", encoding="utf-8").read()
    run(website)
    i+=1