from os import listdir
from os.path import isfile, join
import re

path = "./lab1/lab1"

files = [f for f in listdir(path) if isfile(join(path, f))]

pattern = re.compile("(.*.h|.*.cpp)$")  
code_files = filter(lambda x : bool(pattern.match(x)), files)

outstring = ""
for filename in code_files:
    file = open(path + "/" + filename, "r")
    outstring += filename + "\n```c++\n" + file.read() + "\n```\n"

outfile = open("report.md", "w")
outfile.write(outstring)