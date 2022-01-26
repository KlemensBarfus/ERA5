# splits ERA5 model level files with multiple hourly time steps in individual files with one timestep
# original filename: ERA5_ml_[var]_[date].grb
# written by K.: Barfus 9/2019
import os
import glob
import sys

path = sys.argv[1]
#path = "/scratch/ws/0/barfus-BerlinStorms2/BerlinStorms/ERA5/"

vars = ['129','130','131','132','133']
n_vars = len(vars)

for i_vars in range(0, n_vars):
  # get list of files
  test_str = "ERA5_ml_"+vars[i_vars]+"_*.grb"
  all_files = glob.glob(path+test_str)
  # test which file is relevant (not already an output file)
  for i_files in range(0, len(all_files)):
    test_string = all_files[i_files]
    test_string2 = test_string.split("/")
    test_string3 = test_string2[len(test_string2)-1]
    if(len(test_string3) == 24): # file is relevant
      print(test_string3)
      # test if already results exist
      #tt = path+test_string3[0:20]+"*.grb"
      #print(tt)
      test_files = glob.glob(path+test_string3[0:20]+"_*.grb")
      if(len(test_files) == 0):
        sys_cmd = "cdo splithour "+test_string+" "+path+test_string3[0:20]+"_"    
        print(sys_cmd)
        os.system(sys_cmd)
      sys_cmd = "mv "+test_string+" "+path+"original_files"
      os.system(sys_cmd) 
