# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:05:03 2024

@author: Ana Gonzalez-Nicolas based on Olga's script
"""

import os
import netCDF4 as nc
import numpy as np
import pandas as pd
from datetime import timedelta


def netCDFtoArray(ncfile, var):
    ncdf = nc.Dataset(ncfile)
    # for output timesteps in days:
    tsteps = np.ma.getdata(ncdf.variables['time'][:,])+1
    data = np.zeros((len(ncdf.variables['time']),len(var)))
    all_units= []
    for v in range(len(var)):
        ## for 2D variables
        if ncdf.variables[var[v]].shape[1] == 1:
            data[:,v] = np.ma.getdata(ncdf.variables[var[v]][:,0]) 
        ## for 3D variables
        else:       
            data[:,v] = np.ma.getdata(ncdf.variables[var[v]][:,d,0])
        all_units.append(ncdf.variables[var[v]].units)
    return(data,tsteps,all_units)



def Out_to_Excel(case_dir, case_name, params, start_date, path_save, excel_name): 
    print("Soil layer= ", d)
    print("Path files= ", case_dir)
    
    ## case directory
    os.chdir(case_dir)
    
    ##listing all files in the directory
    files = [filename for filename in os.listdir('.') if filename.startswith(case_name)]
    files =sorted(files)
    print(case_name,'\n',files,'\n')
    
    # writing data to array
    full_array = np.zeros((0,len(params)))
    full_days = np.zeros((0,))
    for f in files:
        array,days,full_units = netCDFtoArray(f, params)
        full_array = np.concatenate([full_array,array])
        full_days = np.concatenate([full_days,days])
    
    ## path to save the excel file
    os.chdir(path_save)

    ## creating correct date range
    frequency='D'
    timestamps = pd.date_range(start_date,periods=full_array.shape[0], freq=frequency)
    ## this timedelta is needed because CLM calculates daily means at the end of the day and writes them to the next day only!
    if frequency == 'D':
        timestamps_d = timestamps-timedelta(days=1)

    ## writing parameters to excel file
    df_excel = pd.DataFrame(full_array[:,:], timestamps_d,params)
    path = os.getcwd()
    #excel_name = path.split('\\')[-1]      
    with pd.ExcelWriter(excel_name+'.xlsx') as writer:
        df_excel.to_excel(writer)


#%%     
# Write all outputs in one array --> These will be ploted with the second script
# List here output/parameters of interest:
param_list = ['GPP','NEE','ER', 'QFLX_EVAP_VEG', 'QFLX_EVAP_TOT', 'Qh', 'Qle', 'EFLX_LH_TOT', 'FSH', 'Rnet', 'NPP','HR', 'AR',
         'TLAI', 'LEAFC', 'GRAINC', 'FROOTC', 'LIVESTEMC', 'GRAINC_TO_FOOD', 'GDDPLANT', 'TSA', 'QIRRIG', 'QIRRIG_DEMAND',
         'QINTR', 'QDRIP', 'QSOIL', 'QVEGE', 'QVEGT','QINFL','QOVER','TG','H2OSOI','SMP', 'TV', 'GDDPLANT', 'DEADSTEMC', 'TSOI',
         'RAIN','SNOW','TBOT','THBOT','WIND','QBOT','ZBOT','FLDS','FSDS']

### Soil layers discretization:
### https://escomp.github.io/ctsm-docs/versions/release-clm5.0/html/tech_note/Ecosystem/CLM50_Tech_Note_Ecosystem.html 

### SOIL LAYER d=2,  5 cm         
d=2 # soil layer

# PATH TO SAVE EXCEL FILES
path_excel = r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release'

# SIM 1 to compare (eCLM commit c984ada_PSmpi_release) 
path1 = r'/p/project1/cslts/gonzalez5/CLM5/eCLM_Paul/eCLM_last_PSmpi_release/eCLM/Tests/CaseDocs_1x1_wuestebach_2009_forcings_DP_1_PSmpi_release'
casename1= '1x1_wuestebach_2009_forcings_DP_1.clm2.h0'
excelname1= 'eCLM_c984ada_PSmpi_release_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm'
print('SIM1 eCLM d=2')
Out_to_Excel(path1,casename1,param_list,'2009-01-01',path_excel,excelname1)

# SIM 2 is Reference (case CLM5_DP1  name=1x1_wuestebach)
path2 = r'/p/scratch/cslts/gonzalez5/CLM5_DATA/Archive/lnd/hist'
casename2= '1x1_wuestebach_2009_forcings_DP_1.clm2.h0'
excelname2= 'CLM5_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm'
print('SIM2 CLM5 d=2')
Out_to_Excel(path2,casename2,param_list,'2009-01-01',path_excel,excelname2)


### SOIL LAYER d=3, 100 cm
d=9 # soil layer

# SIM 1 to compare (eCLM commit c984ada_PSmpi_release) 
excelname_d9_1= 'eCLM_c984ada_PSmpi_release_1x1_wuestebach_2009_forcings_DP_1_soilLay=9_100cm'
print('SIM1 eCLM d=9')
Out_to_Excel(path1,casename1,param_list,'2009-01-01',path_excel,excelname_d9_1)

# SIM 2 is Reference (case CLM5_DP1  name=1x1_wuestebach)
excelname_d9_2= 'CLM5_1x1_wuestebach_2009_forcings_DP_1_soilLay=9_100cm'
print('SIM2 clm5 d=9')
Out_to_Excel(path2,casename2,param_list,'2009-01-01',path_excel,excelname_d9_2)
