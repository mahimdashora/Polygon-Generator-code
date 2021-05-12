import random
import os
import numpy as np
import cv2 as cv2
import time

import matplotlib.pyplot as plt 


list_of_cord=[]
list_temp=[]

for i in range(10,501):
    for j in range(0,i):
        list_temp.append([random.randint(750,1250),random.randint(750,1250)])
    list_of_cord.append(list_temp.copy())
    list_temp.clear()

#for i in range(0,len(list_of_cord)):
 #   print(list_of_cord[i])
arr3=[]
img=np.zeros((2000, 2000, 3), dtype = "uint8")
timer=[]
file_size_list=[]
for i in range(0,len(list_of_cord)):
    list_of_cord[i].append(list_of_cord[i][0])
    arr2=np.asarray(list_of_cord[i],dtype=np.int32)
    img=np.zeros((2000, 2000, 3), dtype = "uint8")
    print(arr2)
    #arr3.append(arr2)
    start=time.time()
    cv2.polylines(img,[arr2],True,(255,0,0),2)
    end=time.time()
    #cv2.imshow("image",img)
    image="image_"+str(i)+".jpg"
    
    timer.append((end-start)*1000)
    
    with open('listfile.txt', 'a+') as filehandle:#writing co-ordinates to file
     c=0
     filehandle.write(' %d %d '%(i+1,len(arr2)-1))
     for listitem in arr2:
         if c==len(arr2)-1:
           filehandle.write('%s ' % listitem)
         else:
          filehandle.write('%s ,' % listitem)
         c+=1
     filehandle.write("\n")
     

    cv2.imwrite(image,img)
    file_size = os.stat(image)
    #print("Size of file :", (file_size.st_size)/1024,"Kb")
    file_size_list.append((file_size.st_size)/1024)

#for i in range(0,len(timer)):
    #print(timer[i])

cv2.waitKey(0)
cv2.destroyAllWindows()



#x_axis=[i for i in range(10,501)]

#y_axis=file_size_list 

#plt.plot(x_axis,y_axis) 
#plt.show()