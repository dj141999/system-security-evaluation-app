import csv
import os
import glob
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
from androguard.decompiler.decompiler import DecompilerDAD
from androguard.core.bytecodes.apk import APK
from androguard.core.analysis import analysis
from androguard.core.bytecodes import dvm

def extract_features(file_path):
    a = APK(file_path)
    # d = DalvikVMFormat(a.get_dex())
    # dx = Analysis(d)
    # vm = dvm.DalvikVMFormat(a.get_dex())
    # vmx = analysis.Analysis(vm)
    # d.set_vmanalysis(dx)
    # d.set_decompiler(DecompilerDAD(d, dx))
    return a.get_permissions()  

def mainn():
  text_file = open("data.txt", "r")   
  b_feature1 = text_file.readlines()
  text_file.close()

  feature_list=[]
  for perm in b_feature1:
     perm2=perm.split('\n')
     feature_list.append(perm2[0])

  feature=feature_list      
  feature_list=[]
  print(len(feature))

  with open("train_file2.csv", "w") as csvfile: 
    
    for feat in feature:
       feature_list.append(feat)
       csvfile.write(feat)
       csvfile.write(',')
    
    permission_list = []
    
    for file in glob.glob('downloaded.apk'):
      permissions = extract_features(file)
      if permissions is None:
          pass
      else:
          
          for permission in permissions:
              permission_list.append(permission)

      csvfile.write('\n')
      for feat in feature :
        j=0;
        for perm in permission_list:
           if(feat==perm):
               j=j+1
        if(j>0):
              csvfile.write('1')
              csvfile.write(',')
        else:
               csvfile.write('0')
               csvfile.write(',')