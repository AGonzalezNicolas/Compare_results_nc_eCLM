# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:16:08 2024

@author: Ana Gonzalez-Nicolas based on Olga's script
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.gridspec as gridspec
import seaborn as sns
sns.set_theme()

# SIM1 Series 1 = TEST series to check --> eCLM
label_1 = 'eCLM_c984ada_PSmpi_release'
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')
#files = [filename for filename in os.listdir('.')]
#files =sorted(files)
#print(files,'\n')
sim1_full = pd.read_excel('eCLM_c984ada_PSmpi_release_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm.xlsx', index_col=0, header = [0])
sim1_full_sLay9 = pd.read_excel('eCLM_c984ada_PSmpi_release_1x1_wuestebach_2009_forcings_DP_1_soilLay=9_100cm.xlsx', index_col=0, header = [0])


# SIM2 Series 2 REFERENCE CASE wtb_1x1 clm5_old_commit  name=1x1_wuestebach_2009_forcings_DP_1
label_2 = 'CLM5_commit_eclm'
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')
sim2_full = pd.read_excel('CLM5_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm.xlsx', index_col=0, header = [0])
sim2_full_sLay9 = pd.read_excel('CLM5_1x1_wuestebach_2009_forcings_DP_1_soilLay=9_100cm.xlsx', index_col=0, header = [0])

#PATH TO SAVE PLOTS
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')

#### unit conversions
# sec to day
f_h=60*60*24

### data
sim1 = sim1_full.loc['2009':'2021']              # test in seconds
sim1_day = sim1_full.loc['2009':'2021']*f_h      # test in days

sim2 = sim2_full.loc['2009':'2021']              # reference in seconds
sim2_day = sim2_full.loc['2009':'2021']*f_h      # reference in days

error = sim2-sim1                                # error in seconds
error_day = sim2_day - sim1_day                  # error in days

RE = (abs((sim1 - sim2)/sim2))*100               # relative error

#######################################################################################################################

##%% FUNCTION to PLOT MULTIPLOTS 5-VARIABLES
# 
def MultiPlot3PFTs(vars_out,vars_out_u,lbl,plotname,test,ref):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=5, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    ax3 = fig.add_subplot(spec[:, 2])
    ax4 = fig.add_subplot(spec[:, 3])
    ax5 = fig.add_subplot(spec[:, 4])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[0],label=label_1,ax=ax1,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[0],label=label_2,ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[1],ax=ax2,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[2],ax=ax3,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[2],ax=ax3,alpha=.7)
    ax3.set_ylabel(lbl[2]+'   '+'['+vars_out_u[2]+']')
    ax3.set_xticklabels(label_ax,rotation=90, ha='right')      
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[3],ax=ax4,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[3],ax=ax4,alpha=.7)
    ax4.set_ylabel(lbl[3]+'   '+'['+vars_out_u[3]+']')
    ax4.set_xticklabels(label_ax,rotation=90, ha='right')      
    # 
    sns.lineplot(data=test, x=test.index, y=vars_out[4],ax=ax5,alpha=.7)
    sns.lineplot(data=ref, x=test.index, y=vars_out[4],ax=ax5,alpha=.7)
    ax5.set_ylabel(lbl[4]+'   '+'['+vars_out_u[4]+']')
    ax5.set_xticklabels(label_ax,rotation=90, ha='right')      
    #
    fig.suptitle(plotname)
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()


#%% PLOT MULTIPLOTS: 5-VARIABLES plots
# For this case soil layer d=2 
## output variables
v1_out = ['GPP','NEE','ER','AR','HR']               
v2_out = ['QSOIL','QVEGE','QVEGT','QOVER','QIRRIG']
v3_out = ['EFLX_LH_TOT','FSH','Rnet','Rnet','QFLX_EVAP_TOT']
v4_out = ['GRAINC','LEAFC','DEADSTEMC','FROOTC','GRAINC_TO_FOOD']

## units for output variables
v1_out_u = ['gC m-2 d-1','gC m-2 d-1','gC m-2 d-1','gC m-2 d-1','gC m-2 d-1'] # *f_h in days
v2_out_u = ['mm d-1','mm d-1','mm d-1','mm d-1','mm d-1']                     # *f_h in days
v3_out_u = ['W m-2','W m-2','W m-2','W m-2','kg m-2 s-1']
v4_out_u = ['gC m-2','gC m-2','gC m-2','gC m-2','gC m-2 s-1']
v1_out_u_sec = ['gC m-2 s-1','gC m-2 s-1','gC m-2 s-1','gC m-2 s-1','gC m-2 s-1'] # in seconds
v2_out_u_sec = ['mm s-1','mm s-1','mm s-1','mm s-1','mm s-1']                     # in seconds

## labels for plots
labels1=['GPP','NEE','ER','AR','HR']
labels2=['QSOIL','QVEGE','QVEGT','QOVER','QIRRIG']
labels3=['LH','FSH','Rnet','Rnet','ET']
labels4=['GRAINC','LEAFC','DEADSTEMC','FROOTC','Harvest']

MultiPlot3PFTs(v1_out,v1_out_u,labels1,'C_fluxes', sim1_day, sim2_day)   # *f_h in days
MultiPlot3PFTs(v2_out,v2_out_u,labels2,'H2O_fluxes', sim1_day, sim2_day) # *f_h in days
MultiPlot3PFTs(v1_out,v1_out_u_sec,labels1,'C_fluxes_s', sim1, sim2)     # in seconds
MultiPlot3PFTs(v2_out,v2_out_u_sec,labels2,'H2O_fluxes_s', sim1, sim2)   # in seconds
MultiPlot3PFTs(v3_out,v3_out_u,labels3,'Energy_fluxes', sim1, sim2)
MultiPlot3PFTs(v4_out,v4_out_u,labels4,'Biomass', sim1, sim2)


###%% FUNCTION TO PLOT MULTIPLOTS DELTA-ERRORS 5-VARIABLES plots
#
def MultiPlot3PFTs_delta(vars_out,vars_out_u,lbl,plotname,labels_plot,delta):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=5, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    ax3 = fig.add_subplot(spec[:, 2])
    ax4 = fig.add_subplot(spec[:, 3])
    ax5 = fig.add_subplot(spec[:, 4])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[0],label=labels_plot,ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[2],ax=ax3,alpha=.7)
    ax3.set_ylabel(lbl[2]+'   '+'['+vars_out_u[2]+']')
    ax3.set_xticklabels(label_ax,rotation=90, ha='right')      
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[3],ax=ax4,alpha=.7)
    ax4.set_ylabel(lbl[3]+'   '+'['+vars_out_u[3]+']')
    ax4.set_xticklabels(label_ax,rotation=90, ha='right')      
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[4],ax=ax5,alpha=.7)
    ax5.set_ylabel(lbl[4]+'   '+'['+vars_out_u[4]+']')
    ax5.set_xticklabels(label_ax,rotation=90, ha='right')      
    #
    fig.suptitle(plotname)
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()

# Error
label_delta = 'Error = eCLM - clm5'    
MultiPlot3PFTs_delta(v1_out,v1_out_u,labels1,'Delta_C_fluxes',label_delta,error_day)   # *f_h in days
MultiPlot3PFTs_delta(v2_out,v2_out_u,labels2,'Delta_H2O_fluxes',label_delta,error_day) # *f_h in days
MultiPlot3PFTs_delta(v3_out,v3_out_u,labels3,'Delta_Energy_fluxes',label_delta,error)
MultiPlot3PFTs_delta(v4_out,v4_out_u,labels4,'Delta_Biomass',label_delta,error)
MultiPlot3PFTs_delta(v1_out,v1_out_u_sec,labels1,'Delta_C_fluxes_sec',label_delta,error)
MultiPlot3PFTs_delta(v2_out,v2_out_u_sec,labels2,'Delta_H2O_fluxes_sec',label_delta,error)

# Relative error
## units for output variables
v1_out_u_percent = ['%','%','%','%','%'] 
#v2_out_u_percent = ['%','%','%','%']      #-> many values are =0
v3_out_u_percent = ['%','%','%','%','%']
#v4_out_u_percent = ['%','%','%']          #-> many values are =0

label_RE = 'Relative Error'    
MultiPlot3PFTs_delta(v1_out,v1_out_u_percent,labels1,'Rel_Error_C_fluxes',label_RE,RE)
#MultiPlot3PFTs_delta(v2_out,v2_out_u_percent,labels2,'Rel_Error_H2O_fluxes',label_RE,RE)    #-> many values are =0
MultiPlot3PFTs_delta(v3_out,v3_out_u_percent,labels3,'Rel_Error_Energy_fluxes',label_RE,RE)
#MultiPlot3PFTs_delta(v4_out,v4_out_u_percent,labels4,'Rel_Error_Biomass',label_RE,RE)       #-> many values are =0
 


### PLOT LAYERS d=2 & d=9 for soil moisture, soil temperature

#%% PLOT MULTIPLOTS 2-VARIABLES plots
def MultiPlot3PFTs_2plots(vars_out,vars_out_u,lbl,plotname,title_layer):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=sim1, x=sim1.index, y=vars_out[0],label=label_1,ax=ax1,alpha=.7)
    sns.lineplot(data=sim2, x=sim1.index, y=vars_out[0],label=label_2,ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=sim1, x=sim1.index, y=vars_out[1],ax=ax2,alpha=.7)
    sns.lineplot(data=sim2, x=sim1.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    # 
    fig.suptitle(title_layer)
    #
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()
 

#%% PLOT MULTIPLOTS DELTA-ERRORS 2-VARIABLES plots
def MultiPlot3PFTs_delta_2plots(vars_out,vars_out_u,lbl,plotname,labels_plot,title_layer,delta):
    # plotting sensitive parameter against output variable
    fig = plt.figure(constrained_layout=True, figsize=(18, 3))
    # creating subplots and specifying their position
    spec = gridspec.GridSpec(ncols=2, nrows=1, figure=fig)
    ax1 = fig.add_subplot(spec[:, 0])
    ax2 = fig.add_subplot(spec[:, 1])
    
    label_ax =['2008','2010','2012','2014','2016','2018','2020','2022']      # 12 years plot: 2010-2021
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[0],label=labels_plot,ax=ax1,alpha=.7)
    ax1.set_ylabel(lbl[0]+'   '+'['+vars_out_u[0]+']')
    ax1.set_xticklabels(label_ax,rotation=90, ha='right')    
    # 
    sns.lineplot(data=delta, x=delta.index, y=vars_out[1],ax=ax2,alpha=.7)
    ax2.set_ylabel(lbl[1]+'   '+'['+vars_out_u[1]+']')
    ax2.set_xticklabels(label_ax,rotation=90, ha='right')   
    # 
    fig.suptitle(title_layer)
    #
    fig.tight_layout()
    plt.savefig(plotname,dpi=400)
    fig.show()

 
# SOIL LAYER d=2, @ 5 cm 
## output variables
v1_out = ['H2OSOI','TSOI']       
## units for output variables  # TSOI in K
v1_out_u = ['mm3/mm3','K']
v1_out_u_percent = ['%','%']
## labels for plots
labels1=['H2OSOI','TSOI']

MultiPlot3PFTs_2plots(v1_out,v1_out_u,labels1,'soiLay=5cm','SOIL LAYER at 5 cm (d=2)')
MultiPlot3PFTs_delta_2plots(v1_out,v1_out_u,labels1,'Delta_soiLay=5cm',label_delta,'SOIL LAYER at 5 cm (d=2)',error)
MultiPlot3PFTs_delta_2plots(v1_out,v1_out_u_percent,labels1,'Rel_Error_soiLay=5cm',label_RE,'SOIL LAYER at 5 cm (d=2)',RE)

# SOIL LAYER d=9, @ 100 cm 
sim1=sim1_full_sLay9.loc['2010':'2021']      # to test
sim2=sim2_full_sLay9.loc['2010':'2021']      # reference
## output variables
v1_out = ['H2OSOI','TSOI']
## units for output variables  # TSOI in K
v1_out_u = ['mm3/mm3','K']
## labels for plots
labels1=['H2OSOI','TSOI']

MultiPlot3PFTs_2plots(v1_out,v1_out_u,labels1,'soiLay=100cm','SOIL LAYER at 100 cm (d=9)')
MultiPlot3PFTs_delta_2plots(v1_out,v1_out_u,labels1,'Delta_soiLay=100cm',label_delta,'SOIL LAYER at 100 cm (d=9)',error)
MultiPlot3PFTs_delta_2plots(v1_out,v1_out_u_percent,labels1,'Rel_Error_soiLay=100cm',label_RE,'SOIL LAYER at 100 cm (d=9)',RE)
