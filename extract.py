import os
import shutil

for root, dirs, files in os.walk('lfw/'):  
   for file in files:
      path_file = os.path.join(root,file)
      shutil.copy2(path_file,'img/') 