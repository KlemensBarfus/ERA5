# splits ERA5 model level files with multiple hourly time steps in individual files with one timestep
# original filename: ERA5_ml_[var]_[date]_[annotation, e.g Berlin, not completely numeric, without "_"].grb (annotation can be skipped) 
# output filename: ERA5_ml_[var]_[date]_[hour]_[annotation, e.g Berlin, but without "_"].grb 

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
  if(len(all_files) > 0): # relevant files exist
    # test which file is relevant (not already an output file)
    for i_files in range(0, len(all_files)):
      test_string = all_files[i_files]
      test_string2 = test_string.split("/")
      filename_with_ending = test_string2[len(test_string2)-1]
      filename = filename_with_ending.split(".")[0]
      filename_parts = filename.split("_")
      valid = False
      n_filename_parts = len(filename_parts)
      if(n_filename_parts) == 3):
        valid = True
      else:
        if(filename_parts.isnumeric() == False):
          valid = True
      if(valid == True):
        # test if results already exist
        test_files = glob.glob(path+"_".join(filename_parts[0:3])+"_*_"+filename_parts[len(filename_parts)-1]+".grb")
        if(len(test_files) == 0):
          sys_cmd = "cdo splithour "+all_files[i_files]+" "+path+"_".join(filename_parts[0:3])   
          print(sys_cmd)
          # os.system(sys_cmd)
          if(n_filename_parts > 3):
            new_files = glob.glob(path+"_".join(filename_parts[0:3])+"*"+".grb")
            for new_file in new_files:
              filename_new_parts
          sys_cmd = "mv "+test_string+" "+path+"original_files"
          os.system(sys_cmd) 
