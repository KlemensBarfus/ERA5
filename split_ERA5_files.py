# splits ERA5 model level or surface data files with multiple hourly time steps in individual files with one timestep
# original filename: ERA5_ml_[var]_[date]_[annotation, e.g Berlin, not completely numeric, without "_"].grb (annotation can be skipped) or
# ERA5_sfc_[date]_[annotation, e.g Berlin, not completely numeric, without "_"].grb 
# output filename: ERA5_ml_[var]_[date]_[hour]_[annotation, e.g Berlin, but without "_"].grb or 
# ERA5_sfc_[date]_[hour]_[annotation, e.g Berlin, but without "_"].grb
# input parameters are:
# path to data, optional: varnumber(s) or 'sfc', if multiple separated by commas (without spaces)


# written by K.: Barfus 9/2019
import os
import glob
import sys

def get_parts_of_filename(string):
  t = string.split("/")
  t2 = t[len(t)-1]
  t3 = t2.split(".")
  t4 = t3[0]
  t5 = t4.split("_")
  return(t5)


path = sys.argv[1]
if(path[len(path)-1] != "/"):
  path = path + "/"
if(len(sys.argv) == 3):
  var_temp = sys.argv[2]
  vars = var_temp.split(",")
else:
  vars = None
  
# find relevant files:
files_orig = []
if(vars is None):
  search_string = path+"ERA5_ml_*_*.grb"
  temp_str = glob.glob(search_string)
  # filter files
  for t in temp_str:
    parts = get_parts_of_filename(t)
    if(len(parts) == 4):
      files_orig.append(t)
    else:
      if(parts[4].isnumeric() == False):
        files_orig.append(t)
  search_string = path+"ERA5_sfc_*.grb"
  temp_str = glob.glob(search_string)
  # filter files
  for t in temp_str:
    parts = get_parts_of_filename(t)
    if(len(parts) == 3):
      files_orig.append(t)
    else:
      if(parts[3].isnumeric() == False):
        files_orig.append(t)
else:
  for var in vars:
    if(var.isnumeric()):
      search_string = path+"ERA5_ml_"+var+"_*.grb" 
      temp_str = glob.glob(search_string)
      # filter files
      for t in temp_str:
        parts = get_parts_of_filename(t)
        if(len(parts) == 4):
          files_orig.append(t)
        else:
          if(parts[4].isnumeric() == False):
            files_orig.append(t)
    else:
      search_string = path+"ERA5_sfc_*.grb"
      temp_str = glob.glob(search_string)
      for t in temp_str:
        parts = get_parts_of_filename(t)
        if(len(parts) == 3):
          files_orig.append(t)
        else:
          if(parts[3].isnumeric() == False):
            files_orig.append(t)


for ffile in files_orig:
  #print(ffile)
  filename_parts = get_parts_of_filename(ffile)
  # test if results already exist
  if(len(filename_parts) == 3): # ERA5_sfc_yyyymmdd...
    search_string = path+"_".join(filename_parts[0:3])+"_*.grb"
    temp_str = path+"_".join(filename_parts[0:3])+"_"
    add_on = ""
    search_str2 = path+"_".join(filename_parts[0:3])+"_*.grb"
  else:
    if(len(filename_parts) == 4): # ERA5_ml_
      search_string = path+"_".join(filename_parts[0:3])+"_*_"+filename_parts[3]+".grb"
      temp_str = path+"_".join(filename_parts[0:3])+"_"
      add_on = "_"+filename_parts[3]
      search_str2 = path+"_".join(filename_parts[0:3])+"_*.grb" 
    else:
      search_string = path+"_".join(filename_parts[0:4])+"_*_"+filename_parts[4]+".grb"
      temp_str = path+"_".join(filename_parts[0:4])+"_"
      add_on = "_"+filename_parts[4]
      search_str2 = path+"_".join(filename_parts[0:4])+"_*.grb"
  test_files = glob.glob(search_string)
  if(len(test_files) == 0):
    sys_cmd = "cdo splithour "+ffile+" "+temp_str
    os.system(sys_cmd)
    new_files = glob.glob(search_str2)
    for new_file in new_files:
      temp_str = get_parts_of_filename(new_file)
      if(temp_str[len(temp_str)-1].isnumeric()):
        if(len(filename_parts) >= 4):
          new_file2 = new_file.replace(".grb",add_on+".grb")
          sys_cmd = "mv "+new_file+" "+new_file2
          os.system(sys_cmd)

          #sys_cmd = "mv "+test_string+" "+path+"original_files"
          #os.system(sys_cmd) 
