def setCache(s,cache):
   LRU = [] #corresponding list used for LRU implementation

   '''(256*1024)/(4*4) = 16384 number of mem lines'''


   strp = "00000000000000000" #17 bits for each mem line where FIRST bit is for Valid bit check

   for m in range(16384): #initializing the two lists
      cache.append([strp] * 4) 
      LRU.append([0,0,0,0])

   f = open(s, "r")
   miss = 0 #number of misses
   hit = 0  #number of hits
   count = 0


   for x in f:
      strn = ""
      strn = x[4:len(x)-3]
      res = "{0:032b}".format(int(strn,16), '032b')
      count += 1
      byteoffset = res[30:]   #2 bits used for byteoffset
      tag = res[:16] #16 bits used for tag
      index_bin = res[16:30] #14 bits used for index
      index = int(index_bin,2) #index from binary to decimal
      replaceFlag = False #flag i any eviction and replacement takes place

      
      for j in range(4):  #check for tag match
         if(cache[index][j] == '1' + tag):
            hit+=1
            replaceFlag = True     #if match found then its a hit
            LRU[index][j] = count  #update the index of LRU to latest count 
            #count is the sequential input line
            break


      if(not(replaceFlag)):   #else its a miss
         miss+=1
         for k in range(4):      #look for empty ways if any and update
            if(cache[index][k][0] == '0'):
               replaceFlag = True
               cache[index][k] = "1"+tag
               LRU[index][k] = count
               break

         if(not(replaceFlag)):         #if all ways in the line hold data
            last_used = LRU[index].index(min(LRU[index])) #access the last recently used way
            cache[index][last_used] = "1"+tag #evict and update
            LRU[index][last_used] = count #update LRU

   print("Four way set")
   print("hits " +str(hit))
   print("Misses :" +str(miss))
   print("hit rate " + str(hit/count))
   print("miss rate " + str(miss/count))