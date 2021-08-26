from directMap import DMcache
from fourwaySet import setCache
files = ["gcc.trace","gzip.trace","mcf.trace","swim.trace","twolf.trace"]

for x in files:
   print(str(files.index(x)+1) +"."+ x)
   cache = []
   DMcache(x,cache)
   print()
   cache = []
   setCache(x,cache)
   print()
