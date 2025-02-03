## Script_NCO
Compares two "nc"-files with NCO and computes the maximum absolute error for the specified outputs.
The maximum absolute error should be less than a threshold, which can be specified in the script.

How to use:
- Change paths and file names
- Specify threshold
- To submit the script, it must be executable:
  ```
  chmod +x CompareSolution.sh
  ./CompareSolution.sh
  ```

## Scripts_python_plots
Compares several "nc"-files with Python of two different simulations (SIM1 and SIM2) and plots different results over time (14 years).

How to use:
1) Source modules in `run_python.in`:
   ```
   source run_python.in
   ```
2) Change paths and file names in `netCDFtoExcel.py` and run Python:
   ```
   python netCDFtoExcel.py
   ```
3) Change paths and file names in `Plots_pull_request_2series.py` and run Python:
   ```
   python Plots_pull_request_2series.py
   ```


## CaseDocs_WTB
Files of the Wuestebach case:
https://icg4geo.icg.kfa-juelich.de/ModelSystems/clm/CLM5.0_on_JSC_Machines/-/tree/master/SampleCases/JSC/1x1_wuestebach_east?ref_type=heads

Follow instructions there but modify the following before submitting:

1) Simulation lenght:
  ```
  ./xmlchange STOP_OPTION=nyears,RUN_STARTDATE=2009-01-01,STOP_DATE=-999,STOP_N=14
  ```

2) Add to print outputs and forcings in `lnd_in`:
  ```
  hist_fincl1 = 'GPP', 'NEE', 'ER', 'QFLX_EVAP_VEG', 'QFLX_EVAP_TOT', 'Qh', 'Qle', 'EFLX_LH_TOT', 'FSH', 'Rnet', 'NPP',
         'HR', 'AR', 'TLAI', 'LEAFC', 'GRAINC', 'FROOTC', 'LIVESTEMC', 'GRAINC_TO_FOOD', 'GDDPLANT', 'TSA', 'QIRRIG',
         'QIRRIG_DEMAND', 'QINTR', 'QDRIP', 'QSOIL', 'QVEGE', 'QVEGT', 'QINFL', 'QOVER', 'TG', 'H2OSOI', 'SMP',
         'TV', 'GDDPLANT', 'DEADSTEMC', 'TSOI', 'RAIN', 'SNOW', 'TBOT', 'THBOT', 'WIND', 'QBOT', 'ZBOT',
         'FLDS', 'FSDS'
  ```		 

3) Modify to double precision in `lnd_in`: 
  ```
  hist_ndens=1
  ```
  
