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
