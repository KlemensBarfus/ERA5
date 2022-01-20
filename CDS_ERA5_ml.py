#!/usr/bin/env python
import cdsapi
import sys
import datetime
c = cdsapi.Client()

output_path = "/scratch/ws/0/barfus-DCUA/ERA5/"
add_on = "_Berlin"
area_str = '60/-10/40/30' # N/W/S/E 

def split_timestring(temp_string):
  rec_year = int(temp_string[0:4])
  rec_month = int(temp_string[4:6])
  rec_day = int(temp_string[6:8])
  if(len(temp_string) > 8):
    rec_hour = int(rec_date_str[8:10])
  else:
    rec_hour = None
  return rec_year, rec_month, rec_day, rec_hour

def start_call_mars(param_str, date_str, time_str, area_str, output_name, pprint=False):
  if(pprint == True):
    print('c.retrieve("reanalysis-era5-complete",')
    print('{')
    print('"class": "ea",')
    print('"expver": "1",')
    print('"stream": "oper",')
    print('"type": "an",')
    print('"param"   :', param_str, ',')
    print('"levtype": "ml",')
    print('"levelist": "1/to/137",')
    print('"date": ', date_str,',')
    print('"time": ',time_str,',')
    print('"grid": "0.25/0.25",')
    print('"area": ',area_str,',')
    print('"format": "grib"')
    print('},')
    print(output_name,')')
  c.retrieve("reanalysis-era5-complete",
  {
  "class": "ea",
  "expver": "1",
  "stream": "oper",
  "type": "an",
  "param"   : param_str,
  "levtype": "ml",
  "levelist": "1/to/137",
  "date": date_str,
  "time": time_str,
  "grid": "0.25/0.25",
  "area": area_str,
  "format": "grib"
   },
   output_name)



# sys.argv e.g.:
# 20010101 parameter [number or "sfc"]
# 2001010112 parameter [number or "sfc"] # with hour
# 2001010108 2001010112 parameter [number or "sfc"] # only some hours of the same day
# 20010101 20010108 parameter [number or "sfc"] # several complete days

if(len(sys.argv) == 3):
  parameter_str = sys.argv[2]
else:
  parameter_str = sys.argv[3]
if(parameter_str == "sfc"):
  param_str = "165.128/166.128/167.128/168.128/172.128/134.128/151.128/235.128/31.128/34.128/33.128/141.128/139.128/170.128/183.128/236.128/39.128/40.128/41.128/42.128"
  levtype_str = "sfc"
else:
  param_str = parameter_str+".128"
  levtype_str = "ml"

if(len(sys.argv) == 3):
  rec_date_str = sys.argv[1]
  rec_year, rec_month, rec_day, rec_hour = split_timestring(rec_date_str)
  year_str = str(rec_year)
  month_str = str(rec_month).zfill(2)
  day_str = str(rec_day).zfill(2)
  date_str = str(rec_year)+"-"+str(rec_month).zfill(2)+"-"+str(rec_day).zfill(2)
  if(rec_hour is None): # yyyymmdd
    time_str = "00/to/23/by/1"  # get all hours
    output_name = output_path+"ERA5_ml_"+parameter_str+"_"+str(rec_year)+str(rec_month).zfill(2)+str(rec_day).zfill(2)+add_on+".grb"   
  else: # get only one hour
    time_str = str(rec_hour).zfill(2)+"/to/"+str(rec_hour).zfill(2)+"/by/1"
    output_name = output_path+"ERA5_ml_"+parameter_str+"_"+str(rec_year)+str(rec_month).zfill(2)+str(rec_day).zfill(2)+str(rec_hour).zfill(2)+add_on+".grb"
  start_call_mars(param_str, date_str, time_str, area_str, output_name)
else: # len(sys.argv) == 4
  start_date_str = sys.argv[1] # either yyyymmdd or yyyymmddhhmm
  start_year, start_month, start_day, start_hour = split_timestring(start_date_str)
  stop_date_str = sys.argv[2]
  stop_year, stop_month, stop_day, stop_hour = split_timestring(stop_date_str)
  year_str = str(start_year)
  month_str = str(start_month).zfill(2)
  if(start_hour is None):
    start_date = datetime.datetime(start_year, start_month, start_day)
    stop_date = datetime.datetime(stop_year, stop_month, stop_day)
    n_days = (stop_date - start_date).days + 1
    time_str = "00/to/23/by/1"
    #-"2013-09-01/to/2013-09-30"
    day_str = "[" 
    for i_days in range(0, n_days):
      dd = datetime.timedelta(i_days)
      rec_date  = start_date + dd
      temp_str = "'"+str(rec_date.day).zfill(2)+"', "
      day_str = day_str + temp_str
    day_str = day_str+"]"
    output_name = output_path+"ERA5_ml_"+parameter_str+"_"+start_date_str+"_"+stop_date_str+add_on+".grb"
  else:
    time_str = str(start_hour).zfill(2)+"/to/"+str(stop_hour).zfill(2)+"/by/1"
    day_str = str(start_day).zfill(2)    
    date_str = str(start_year)+"-"+str(start_month).zfill(2)+"-"+str(start_day).zfill(2) 
    output_name = output_path+"ERA5_ml_"+parameter_str+"_"+str(rec_year)+str(rec_month).zfill(2)+str(rec_day).zfill(2)+"_"+str(start_hour).zfill(2)+"-"+str(stop_hour).zfill(2)+add_on+".grb"
  pprint = False
  start_call_mars(param_str, year_str, month_str, day_str, time_str, area_str, output_name, pprint)


#  c.retrieve("reanalysis-era5-complete",
#  {
#  "class": "ea",
#  "expver": "1",
#  "stream": "oper",
#  "type": "an", 
#  "param"   : parameter_str+".128",
#  "levtype": "ml",
#  "levelist": "1/to/137",
#  "date": date_str,
#  "time": "00/to/23/by/1",
#  "grid": "0.25/0.25",
#  "area": '54/9/50/18', 
#  "format": "grib"
#   },
#   output_name)


