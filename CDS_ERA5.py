#!/usr/bin/env python
import cdsapi
import sys
import datetime
from datestring_to_datetime import datestring_to_datetime


def CDS_download_single_levels(res):
  c = cdsapi.Client()
  c.retrieve(
    res['ERA5_dataset'],
  {
    'product_type': res['product_type'],
    'variable': res['variable'],
    'year': res['year'],
    'month': res['month'],
    'day': res['day'],
    'time': res['time'],
    'format': 'grib',
   },
   res['output_filename'])

def CDS_download_pressure_levels(res):
  c = cdsapi.Client()
  c.retrieve(
    res['ERA5_dataset'],
  {
    'product_type': res['product_type'],
    'variable': res['variable'],
    'pressure_level': res['pressure_level'], 
    'year': res['year'],
    'month': res['month'],
    'day': res['day'],
    'time': res['time'],
    'format': 'grib',
   },
   res['output_filename'])
  

def MARS_download_model_levels(res):
  c = cdsapi.Client()
  c.retrieve(
    res['ERA5_dataset'], {
    "class": res['class'],
    "dataset": "era5",
    "date": res['date'],
    "expver": "1",
    "levelist": res['levellist'],
    "levtype": res['levtype'],
    "param": res['param'],
    "stream": res['stream'],
    "time": res["time"],
    "type": res['type'],
    }, res['output_filename'])



def MARS_download_surface_level(res):
  c = cdsapi.Client()
  c.retrieve(
    res['ERA5_dataset'], {
    "class": res['class'],
    "dataset": "era5",
    "date": res['date'],
    "expver": "1",
    "levtype": res['levtype'],
    "param": res['param'],
    "stream": res['stream'],
    "time": res['time'],
      "type": res['type'],
    },
    res['output_filename'])

  
def CDO_get_leveltype(res, var, pressure_level=[]):
  # model levels
  if(var in ['26','27','28','29','30','43','74','129','160','161','162','163','172','228007']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "sfc"
    res['type'] = 'an'
    res['class'] = 'ea'
  if(var in ['15','16','17','18','31','32','33','34','35','36','37','38','39','40','41','42','59',
             '66','67','134','139','141','148','151','159','164','165','166','167','168','170',
             '183','186','187','188','198','229','230','231','232','235','236','238','243','244',
             '245','228001','228003','228008','228009','228010','228011','228012','228013','228014',
             '228015','228016','228017','228018','228019','228023','228024','228029','228131',
             '228132','228217','228218','228219','228220','228221','228246','228247','260015','260121','260123']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "sfc"
    res['type'] = 'an'
    res['class'] = 'ea'
  if(var in ['8','9','44','45','50','57','142','143','144','145','146','147','169','175','176','177','178','179',
             '180','181','182','195','196','197','205','208','209','210','211','212','213','228','239','240',
             '228021','228022','228129','228130','228251']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "sfc"
    res['type'] = 'an' 
    res['class'] = 'ea'
  if(var in ['235020','235021','235023','235024','235026','235027','235029','235030','235031','235032','235033',
             '235034','235035','235036','235037','235038','235039','235040','235041','235042','235043','235045',
             '235046','235047','235048','235049','235050','235051','235052','235053','235054','235055','235056',
             '235057','235058','235059','235068','235069','235070']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "sfc"
    res['type'] = 'an'
    res['class'] = 'ea'
  if(var in ['78','79','136','137','206','162053','162054','162059','162060','162061','162062','162063','162064',
             '162065','162066','162067','162068','162069','162070','162071','162072','162073','162074','162075',
             '162076','162077','162078','162079','162080','162081','162082','162083','162084','162085','162086',
             '162087','162088','162089','162090','162091','162092','228088','228089','228090']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "sfc"
    res['type'] = 'an'
    res['class'] = 'ea'
  if(var in ['60','75','76','129','130','131','132','133','135','138','155','157','203','246','247','248']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "pl"
    res['type'] = 'an'
    res['class'] = 'ea'
  if(var in ['75','76','77','129','130','131','132','133','135','138','152','155','203','246','247','248']):
    res['ERA5_dataset'] = "reanalysis-era5-complete"
    res['stream'] = "oper"
    res['levtype'] = "ml"
    res['type'] = 'an'
    res['class'] = 'ea'
  # CDS variables
  # single levels
  if(var in ['100m_u_component_of_wind', '100m_v_component_of_wind', '10m_u_component_of_neutral_wind', '10m_u_component_of_wind', 
             '10m_v_component_of_neutral_wind', '10m_v_component_of_wind','10m_wind_gust_since_previous_post_processing', '2m_dewpoint_temperature', 
             '2m_temperature','air_density_over_the_oceans', 'angle_of_sub_gridscale_orography', 'anisotropy_of_sub_gridscale_orography',
             'benjamin_feir_index', 'boundary_layer_dissipation', 'boundary_layer_height','charnock', 'clear_sky_direct_solar_radiation_at_surface', 'cloud_base_height',
             'coefficient_of_drag_with_waves', 'convective_available_potential_energy', 'convective_inhibition', 'convective_precipitation', 'convective_rain_rate', 
             'convective_snowfall', 'convective_snowfall_rate_water_equivalent', 'downward_uv_radiation_at_the_surface', 'duct_base_height', 'eastward_gravity_wave_surface_stress', 
             'eastward_turbulent_surface_stress', 'evaporation', 'forecast_albedo', 'forecast_logarithm_of_surface_roughness_for_heat', 'forecast_surface_roughness',
             'free_convective_velocity_over_the_oceans', 'friction_velocity', 'gravity_wave_dissipation', 'high_cloud_cover', 'high_vegetation_cover',
             'ice_temperature_layer_1', 'ice_temperature_layer_2', 'ice_temperature_layer_3', 'ice_temperature_layer_4', 'instantaneous_10m_wind_gust', 
             'instantaneous_eastward_turbulent_surface_stress', 'instantaneous_large_scale_surface_precipitation_fraction', 'instantaneous_moisture_flux', 
             'instantaneous_northward_turbulent_surface_stress', 'instantaneous_surface_sensible_heat_flux', 'k_index', 'lake_bottom_temperature',
             'lake_cover', 'lake_depth', 'lake_ice_depth', 'lake_ice_temperature', 'lake_mix_layer_depth', 'lake_mix_layer_temperature', 'lake_shape_factor', 
             'lake_total_layer_temperature', 'land_sea_mask', 'large_scale_precipitation', 'large_scale_precipitation_fraction', 'large_scale_rain_rate',
             'large_scale_snowfall', 'large_scale_snowfall_rate_water_equivalent', 'leaf_area_index_high_vegetation', 'leaf_area_index_low_vegetation', 
             'low_cloud_cover', 'low_vegetation_cover', 'maximum_2m_temperature_since_previous_post_processing', 'maximum_individual_wave_height', 
             'maximum_total_precipitation_rate_since_previous_post_processing', 'mean_boundary_layer_dissipation', 'mean_convective_precipitation_rate', 'mean_convective_snowfall_rate',
             'mean_direction_of_total_swell', 'mean_direction_of_wind_waves', 'mean_eastward_gravity_wave_surface_stress', 'mean_eastward_turbulent_surface_stress', 'mean_evaporation_rate', 
             'mean_gravity_wave_dissipation', 'mean_large_scale_precipitation_fraction', 'mean_large_scale_precipitation_rate', 'mean_large_scale_snowfall_rate',
             'mean_northward_gravity_wave_surface_stress', 'mean_northward_turbulent_surface_stress', 'mean_period_of_total_swell', 'mean_period_of_wind_waves', 
             'mean_potential_evaporation_rate', 'mean_runoff_rate', 'mean_sea_level_pressure', 'mean_snow_evaporation_rate', 'mean_snowfall_rate',
             'mean_snowmelt_rate', 'mean_square_slope_of_waves', 'mean_sub_surface_runoff_rate', 'mean_surface_direct_short_wave_radiation_flux', 
             'mean_surface_direct_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_long_wave_radiation_flux', 'mean_surface_downward_long_wave_radiation_flux_clear_sky', 
             'mean_surface_downward_short_wave_radiation_flux', 'mean_surface_downward_short_wave_radiation_flux_clear_sky', 'mean_surface_downward_uv_radiation_flux', 
             'mean_surface_latent_heat_flux', 'mean_surface_net_long_wave_radiation_flux', 'mean_surface_net_long_wave_radiation_flux_clear_sky', 
             'mean_surface_net_short_wave_radiation_flux', 'mean_surface_net_short_wave_radiation_flux_clear_sky', 'mean_surface_runoff_rate', 'mean_surface_sensible_heat_flux', 
             'mean_top_downward_short_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux', 'mean_top_net_long_wave_radiation_flux_clear_sky', 'mean_top_net_short_wave_radiation_flux',
             'mean_top_net_short_wave_radiation_flux_clear_sky', 'mean_total_precipitation_rate', 'mean_vertical_gradient_of_refractivity_inside_trapping_layer',
             'mean_vertically_integrated_moisture_divergence', 'mean_wave_direction', 'mean_wave_direction_of_first_swell_partition',
             'mean_wave_direction_of_second_swell_partition', 'mean_wave_direction_of_third_swell_partition', 'mean_wave_period',
             'mean_wave_period_based_on_first_moment', 'mean_wave_period_based_on_first_moment_for_swell', 'mean_wave_period_based_on_first_moment_for_wind_waves',
             'mean_wave_period_based_on_second_moment_for_swell', 'mean_wave_period_based_on_second_moment_for_wind_waves', 'mean_wave_period_of_first_swell_partition',
             'mean_wave_period_of_second_swell_partition', 'mean_wave_period_of_third_swell_partition', 'mean_zero_crossing_wave_period',
             'medium_cloud_cover', 'minimum_2m_temperature_since_previous_post_processing', 'minimum_total_precipitation_rate_since_previous_post_processing',
             'minimum_vertical_gradient_of_refractivity_inside_trapping_layer', 'model_bathymetry', 'near_ir_albedo_for_diffuse_radiation',
             'near_ir_albedo_for_direct_radiation', 'normalized_energy_flux_into_ocean', 'normalized_energy_flux_into_waves',
             'normalized_stress_into_ocean', 'northward_gravity_wave_surface_stress', 'northward_turbulent_surface_stress',
             'ocean_surface_stress_equivalent_10m_neutral_wind_direction', 'ocean_surface_stress_equivalent_10m_neutral_wind_speed', 'peak_wave_period',
             'period_corresponding_to_maximum_individual_wave_height', 'potential_evaporation', 'precipitation_type',
             'runoff', 'sea_ice_cover', 'sea_surface_temperature', 'significant_height_of_combined_wind_waves_and_swell', 'significant_height_of_total_swell', 
             'significant_height_of_wind_waves', 'significant_wave_height_of_first_swell_partition', 'significant_wave_height_of_second_swell_partition', 
             'significant_wave_height_of_third_swell_partition', 'skin_reservoir_content', 'skin_temperature', 'slope_of_sub_gridscale_orography',
             'snow_albedo', 'snow_density', 'snow_depth', 'snow_evaporation', 'snowfall', 'snowmelt', 'soil_temperature_level_1', 'soil_temperature_level_2', 
             'soil_temperature_level_3', 'soil_temperature_level_4', 'soil_type', 'standard_deviation_of_filtered_subgrid_orography',
             'standard_deviation_of_orography', 'sub_surface_runoff', 'surface_latent_heat_flux', 'surface_net_solar_radiation', 'surface_net_solar_radiation_clear_sky', 
             'surface_net_thermal_radiation', 'surface_net_thermal_radiation_clear_sky', 'surface_pressure', 'surface_runoff', 'surface_sensible_heat_flux', 
             'surface_solar_radiation_downward_clear_sky', 'surface_solar_radiation_downwards', 'surface_thermal_radiation_downward_clear_sky', 'surface_thermal_radiation_downwards', 
             'temperature_of_snow_layer', 'toa_incident_solar_radiation', 'top_net_solar_radiation', 'top_net_solar_radiation_clear_sky', 'top_net_thermal_radiation', 
             'top_net_thermal_radiation_clear_sky', 'total_cloud_cover', 'total_column_cloud_ice_water', 'total_column_cloud_liquid_water', 'total_column_ozone',
             'total_column_rain_water', 'total_column_snow_water', 'total_column_supercooled_liquid_water', 'total_column_water', 'total_column_water_vapour', 'total_precipitation',
             'total_sky_direct_solar_radiation_at_surface', 'total_totals_index', 'trapping_layer_base_height', 'trapping_layer_top_height', 'type_of_high_vegetation', 'type_of_low_vegetation',
             'u_component_stokes_drift', 'uv_visible_albedo_for_diffuse_radiation', 'uv_visible_albedo_for_direct_radiation', 'v_component_stokes_drift', 
             'vertical_integral_of_divergence_of_cloud_frozen_water_flux', 'vertical_integral_of_divergence_of_cloud_liquid_water_flux',
             'vertical_integral_of_divergence_of_geopotential_flux', 'vertical_integral_of_divergence_of_kinetic_energy_flux', 'vertical_integral_of_divergence_of_mass_flux',
             'vertical_integral_of_divergence_of_moisture_flux', 'vertical_integral_of_divergence_of_ozone_flux', 'vertical_integral_of_divergence_of_thermal_energy_flux',
             'vertical_integral_of_divergence_of_total_energy_flux', 'vertical_integral_of_eastward_cloud_frozen_water_flux', 'vertical_integral_of_eastward_cloud_liquid_water_flux',
             'vertical_integral_of_eastward_geopotential_flux', 'vertical_integral_of_eastward_heat_flux', 'vertical_integral_of_eastward_kinetic_energy_flux',
             'vertical_integral_of_eastward_mass_flux', 'vertical_integral_of_eastward_ozone_flux', 'vertical_integral_of_eastward_total_energy_flux',
             'vertical_integral_of_eastward_water_vapour_flux', 'vertical_integral_of_energy_conversion', 'vertical_integral_of_kinetic_energy',
             'vertical_integral_of_mass_of_atmosphere', 'vertical_integral_of_mass_tendency', 'vertical_integral_of_northward_cloud_frozen_water_flux',
             'vertical_integral_of_northward_cloud_liquid_water_flux', 'vertical_integral_of_northward_geopotential_flux', 'vertical_integral_of_northward_heat_flux',
             'vertical_integral_of_northward_kinetic_energy_flux', 'vertical_integral_of_northward_mass_flux', 'vertical_integral_of_northward_ozone_flux',
             'vertical_integral_of_northward_total_energy_flux', 'vertical_integral_of_northward_water_vapour_flux', 'vertical_integral_of_potential_and_internal_energy',
             'vertical_integral_of_potential_internal_and_latent_energy', 'vertical_integral_of_temperature', 'vertical_integral_of_thermal_energy',
             'vertical_integral_of_total_energy', 'vertically_integrated_moisture_divergence', 'volumetric_soil_water_layer_1',
             'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3', 'volumetric_soil_water_layer_4',
             'wave_spectral_directional_width', 'wave_spectral_directional_width_for_swell', 'wave_spectral_directional_width_for_wind_waves',
             'wave_spectral_kurtosis', 'wave_spectral_peakedness', 'wave_spectral_skewness',
             'zero_degree_level']):
    res['ERA5_dataset'] = 'reanalysis-era5-single-levels'
    res['product_type'] = 'reanalysis'
  if(var in ['divergence', 'fraction_of_cloud_cover', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content', 'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity',
                       'vorticity']):
    res['ERA5_dataset'] = 'reanalysis-era5-pressure-levels'
    res['product_type'] = 'reanalysis'
    # 'pressure_level'  
  if(var in ['geopotential']):
    if(len(pressure_level) == 0):
      res['ERA5_dataset'] = 'reanalysis-era5-single-levels'
      res['product_type'] = 'reanalysis' 
    else:
      res['ERA5_dataset'] = 'reanalysis-era5-pressure-levels'
      res['product_type'] = 'reanalysis'

  return res

def get_time(res, times_in): 
  # times_in can be:
  # "all" -> all hours
  # [h1, h2, h3, h4] -> list with desired hours as integers
 
  if(times_in == 'all'):    
    if(res['ERA5_dataset'] in ['reanalysis-era5-pressure-levels', 'reanalysis-era5-single-levels']):
      res['time'] = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
              '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
              '18:00', '19:00', '20:00', '21:00', '22:00', '23:00',]
    else:   
      res['time'] = '00/to/23/by/1'
  else:
    inn = times_in.split(",") 
    if(res['ERA5_dataset'] in ['reanalysis-era5-pressure-levels', 'reanalysis-era5-single-levels']):
      res_time = []
      for i in range(0, len(inn)):
        inn2 = int(inn[i])
        temp_str = str(inn[i]).zfill(2)+':00'
        res_time.append(temp_str)
    else:
      time = "'"    #'00/06/12/18'
      for i in range(0, len(inn)):
        temp_str = str(inn[i]).zfill(2)
        if(i < len(inn)-1):
          temp_str = temp_str+"/"
        else:
          temp_str = temp_str+"'"
        time = time + temp_str
    res['time'] = res_time  
  return res

def get_var_param(res, varname_in):
  if(varname_in == 'sfc'):  # shortcut for WRF surface variables from ml data
    res["param"] = "165.128/166.128/167.128/168.128/172.128/134.128/151.128/235.128/31.128/34.128/33.128/141.128/139.128/170.128/183.128/236.128/39.128/40.128/41.128/42.128"
  else:
    if(res['ERA5_dataset'] == "reanalysis-era5-complete"):
      if("," in varname_in): # multiple variables
        temp_str = varname_in.split(",")
        res["param"] = ""
        for i_param in range(0, len(temp_str)):
          if(i_param < len(temp_str)-1):
            res["param"] = res["param"]+temp_str+".128/"
          else:
            res["param"] = res["param"]+temp_str+".128"
      else:
        res["param"] = varname_in+".128"
    else: # CDS terminology
      res["variable"] = varname_in.split(",")
  return res    

def get_date(res, days_in):
  import datetime

  if("-" in days_in):
    temp_str = days_in.split("-")
    start_str = temp_str[0]
    stop_str = temp_str[1]
    if(len(start_str) == 4):
      start_day = datetime.datetime(int(start_str),1,1,0,0,0)
      stop_day = datetime.datetime(int(stop_str),12,31,23,59,59)
    else:  
      start_day = datestring_to_datetime(start_str)
      stop_day = datestring_to_datetime(stop_str)
    n_years = (stop_day.year - start_day.year) + 1
    # cds version - not necessarily mars version
    # year
    if(n_years == 1):
      res["year"] = str(start_day.year)
    else:
      res["year"] = []
      for i_years in range(0, n_years):
        rec_year_str = str(start_day.year + i_years)
        res["year"].append(rec_year_str)
    # month    
    if(n_years > 1):
      res = res_all_months(res)
    else:
      res = res_get_month(res, start_day.month, stop_day.month)
    # day
    if(n_years > 1):
      res = res_all_days(res)
    else:
      n_months = (stop_day.month - start_day.month) + 1 
      if(n_months > 1):
        res = res_all_days(res)
      else:
        res = res_get_days(res, start_day, stop_day)
    # MARS version
    start_date_str = str(start_day.year)+"-"+str(start_day.month).zfill(2)+"-"+str(start_day.day).zfill(2)
    stop_date_str = str(stop_day.year)+"-"+str(stop_day.month).zfill(2)+"-"+str(stop_day.day).zfill(2)
    res["date"] = start_date_str+"/to/"+stop_date_str #     "date": "1999-01-01/to/1999-01-31",
  else: # only one year or one day
    if(len(days_in) == 4): # yyyy
      res["year"] = days_in
      res = res_all_months(res)
      res = res_all_days(res)
    else:                # yyyymmdd  
      rec_day = datestring_to_datetime(days_in)
      res["year"] = str(rec_day.year)
      res["month"] = str(rec_day.month).zfill(2)
      res["day"] = str(rec_day.day).zfill(2)
      res["date"] = str(rec_day.year)+"-"+str(rec_day.month).zfill(2)+"-"+str(rec_day.day).zfill(2)
  return res 


def res_all_days(res):
  res["day"] = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
                '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                '25', '26', '27', '28', '29', '30', '31']
  return res

def res_all_months(res):
  res["month"] =  ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
  return res

def res_get_month(res, start_month, stop_month):
  n_months = (stop_month - start_month)+1
  res["month"] = []
  for i_month in range(0, n_months):
    rec_month_str = str(start_month + i_month).zfill(2)
    res["month"].append(rec_month_str)
  return res  

def res_get_days(res, start_day, stop_day):
  import datetime
  res["day"] = []
  rec_day = start_day
  while(rec_day <= stop_day):
    res["day"].append(str(rec_day.day).zfill(2))
    rec_day = rec_day + datetime.timedelta(days=1)
  return res
    
def get_area(res, area_in):
  if("," in area_in):
    temp_str = area_in.split(",")
    temp_str = [int(i) for i in temp_str]
    res["area"] = temp_str
  else:
    res["area"] = "all"
  return res

def get_levels(res, level_in):
  # get pressure/model levels
  # level_in can be:
  # "pl" -> all pressure levels from CDS
  # "ml" -> all model levels from MARS
  # "
  if(level_in == "pl"):
    res['pressure_level'] = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200',
                     '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750',
                     '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000',]
  else:
    if(level_in == 'ml'):
      res['pressure_level'] = []
      res['levellist'] = "1/to/137"
    else:
      if("," in level_in):  # multiple pressure levels from CDS  
        temp_str = level_in.split(',')
        res_temp = []
        for i in range(0, len(temp_str)):
          res_temp.append("'"+temp_str[i]+"',")
        res['pressure_level'] = res_temp
      else:
        if(level_in.isnumeric()): # one pressure level from CDS
          res['pressure_level'] = level_in
        else: # single level
          res['pressure_level'] = [] 
  return res


def get_output_filename(res, path_in, varname_in, days_in, time_in, level_in, area_in):
  output_filename = path_in + "ERA5_"
  temp_str = varname_in.replace(",", "-") 
  output_filename = output_filename + temp_str
  output_filename = output_filename +"_"+days_in
  #time_in = sys.argv[3]    # either all hours of the day, then 'all', or list of hours, then e.g. 0,6,12,18
  if("," in time_in):
    temp_str = time_in.split(",")
    temp_str2 = ""
    for i in range(0, len(temp_str)):
      temp_str2 = temp_str2 + str(int(temp_str[i])).zfill(2)
    output_filename = output_filename+"_"+temp_str2
  if("," in level_in):
    temp_str = level_in.split(",")
    temp_str2 =	""
    for	i in range(0, len(temp_str)):
      temp_str2 = temp_str2 + temp_str[i]
    output_filename = output_filename+"_"+temp_str2
  if(area_in != "all"):
    output_filename = output_filename+"_"+area_in
  output_filename = output_filename+".grib"  
  res['output_filename'] = output_filename
  return res

def geopotential_inside_variables(varname_in):
  if('geopotential' in varname_in):
    res = True
  else:
    res = False
  return res  


#def main():
import sys

# routine to download ERA5 data from CDS or MARS
# An important note: working with variable names is straightforward except for 'geopotential'
# as this appears as a single level as well as a pressure level variable in CDS
# this makes the whole thing a little bit ugly
  
varname_in = sys.argv[1] # "varnames separated by a comma
days_in = sys.argv[2]    # either one year as yyyy, two years as yyyy-yyyy,  one day as yyyymmdd or start and stop day as yyyymmdd-yyyymmdd
time_in = sys.argv[3]    # either all hours of the day, then 'all', or list of hours, then e.g. 0,6,12,18
level_in = sys.argv[4]   # either 'ml', then all model levels, 'pl', then all pressure levels, '850,700,500' as list of pressure levels '850' as a single pressure level or 
                           # any dummy (e.g. 'sl') if variables on single levels
area_in = sys.argv[5]    # either global data, then 'all' or a description of subarea [n, W, S, E]
path_in = sys.argv[6]    # path where to store the data

  
res = {}

       
# get vars
if(varname_in == 'sfc'):  # shortcut for WRF surface variables from ml data
  res["param"] = "165.128/166.128/167.128/168.128/172.128/134.128/151.128/235.128/31.128/34.128/33.128/141.128/139.128/170.128/183.128/236.128/39.128/40.128/41.128/42.128"
  res['pressure_level'] = []
  var_nr1 = "165"
  res = CDO_get_leveltype(res, var_nr1, pressure_level=res['pressure_level'])
else:
  res = get_levels(res, level_in)
  temp_str = varname_in.split(",")
  var_nr1 = temp_str[0]  # get the first variable to check the level
  res = CDO_get_leveltype(res, var_nr1, pressure_level=res['pressure_level'])

res = get_date(res, days_in)

res = get_time(res, time_in)

res = get_var_param(res, varname_in)

res = get_area(res, area_in)

res = get_output_filename(res, path_in, varname_in, days_in, time_in, level_in, area_in)

if(res['ERA5_dataset'] == 'reanalysis-era5-single-levels'):
  CDS_download_single_levels(res)
else:
  if(res['ERA5_dataset'] == 'reanalysis-era5-pressure-levels'):
    CDS_download_pressure_levels(res)
  else:
    if(res['ERA5_dataset'] == 'reanalysis-era5-complete'):
      if(res['levtype'] == 'sfc'):
        MARS_download_surface_level(res)
      else:
        MARS_download_model_levels(res)
      
#if __name__ == "__main__":
#    main()

