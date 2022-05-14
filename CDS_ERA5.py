#!/usr/bin/env python
import cdsapi
import sys
import datetime
c = cdsapi.Client()


start_date_str = sys.argv[1]
stop_date_str = sys.argv[2]

output_path = "/scratch/ws/barfus-BerlinStorms/BerlinStorms/ERA5/"

start_year_str = start_date_str[0:4]
start_month_str = start_date_str[4:6]
start_day_str = start_date_str[6:8]
stop_year_str = stop_date_str[0:4]
stop_month_str = stop_date_str[4:6]
stop_day_str = stop_date_str[6:8]

parameter_str = sys.argv[3]

start_year = int(start_year_str)
start_month = int(start_month_str)
start_day = int(start_day_str)
stop_year = int(stop_year_str)
stop_month = int(stop_month_str)
stop_day = int(stop_day_str)
start_date = datetime.datetime(start_year, start_month, start_day)
stop_date = datetime.datetime(stop_year, stop_month, stop_day)
 
n_days = (stop_date - start_date).days + 1


for i_days in range(0, n_days):
  dd = datetime.timedelta(i_days)
  rec_date  = start_date + dd
  date = str(rec_date.year)+"-"+str(rec_date.month).zfill(2)+"-"+str(rec_date.day).zfill(2)
  output_name = output_path+"ERA5_ml_"+parameter_str+"_"+str(rec_date.year)+str(rec_date.month).zfill(2)+str(rec_date.day).zfill(2)+".grb"
  print(output_name)
  c.retrieve("reanalysis-era5-complete",
  {
  "class": "ea",
  "expver": "1",
  "stream": "oper",
  "type": "an", 
  "param"   : parameter_str+".128",
  "levtype": "ml",
  "levelist": "1/to/137",
  "date": date,
  "time": "00/to/23/by/1",
  "grid": "0.25/0.25", 
  "format": "grib"
   },
   output_name)


