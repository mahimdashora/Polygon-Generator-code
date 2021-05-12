import geopandas
import numpy as np
nybb_path = geopandas.datasets.get_path('nybb')
boros = geopandas.read_file(nybb_path)
boros.set_index('BoroCode', inplace=True)
boros.sort_index(inplace=True)
g = [i for i in boros.geometry]
ext=[]
c=0
for i in range(len(g)):
  all_coords = []
  for b in g[i].boundary: # for first feature/row
    coords = np.dstack(b.coords.xy).tolist()
    #print(coords)
    all_coords.append(coords)   #can't use starred expression here              
    c+=1
   #all_coords has 33 subarrays
  a=np.true_divide(all_coords[0],1000)
  ext.append(a.astype(int))
print(len(ext)) 