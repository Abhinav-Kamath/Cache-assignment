def DMcache(file,cache):
   cache = ["0" * 15] * 65536 #cache memory
   f = open(file, "r")
   miss = 0 #number of misses
   hit = 0  #number of hits
   count = 0
   for x in f:
      strn = ""
      strn = x[4:len(x)-3]
      res = "{0:032b}".format(int(strn,16), '032b') #address from hex to binary
      count +=1
      byteoffset = res[30:] #2 bits used for byteoffset
      tag = res[:14] #14 bits used for tag
      index_bin = res[14:30] #16 bits used for index

      index = int(index_bin,2) #index from binary to decimal

      if(cache[index][0] == '0'): #if valid bit is zero at given index
         miss+=1
         cache[index] = "1" + tag 

      elif(cache[index][0] == '1' ): #if valid bit is 1 at given index
         if(cache[index][1:] == tag):  #if tag match is successful
            hit+=1
         else:             #if tag match is unsuccessful then evict and overwrite
            miss+=1
            cache[index] = "1" + tag

   print("Total accesses:" + str(count))       
   print()  
   print("Direct Mapped")
   print("hits " +str(hit))
   print("Misses :" +str(miss))
   print("hit rate " + str(hit/count))
   print("miss rate " + str(miss/count))