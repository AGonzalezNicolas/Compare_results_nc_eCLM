# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:16:08 2024

@author: Ana
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.gridspec as gridspec
import seaborn as sns
sns.set_theme()

# SIM1 Series 1 = TEST series to check --> wtb_1x1_eclm_forcings
label_1 = 'eCLM_c984ada_PSmpi_release'
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')
sim1_full = pd.read_excel('eCLM_c984ada_PSmpi_release_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm.xlsx', index_col=0, header = [0])


# SIM2 Series 2 REFERENCE CASE wtb_1x1 clm5_old_commit  name=1x1_wuestebach_2009_forcings
label_2 = 'CLM5_commit_eclm'
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')
sim2_full = pd.read_excel('CLM5_1x1_wuestebach_2009_forcings_DP_1_soilLay=2_5cm.xlsx', index_col=0, header = [0])

#Path to save plots
os.chdir(r'/p/project1/cslts/gonzalez5/CLM5/0_Check_results/16_CLM5_commit_eCLM_vs_eCLM_commit_c984ada_PSmpi_release')


### Data to plot
sim1 = sim1_full.loc['2009':'2021']          # test in seconds
sim2 = sim2_full.loc['2009':'2021']          # reference in seconds

error = sim2-sim1                            # error in seconds
RE = (abs((sim1 - sim2)/sim2))*100           # relative error


#######################################################################################################################

#%% FUNCTION to PLOT MULTIPLOTS 5-VARIABLES
# soil Layer =2 
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
v1_out =  ['RAIN','SNOW','TBOT','THBOT','THBOT']
v2_out =  ['WIND','QBOT','ZBOT','FLDS','FSDS']

## units for output variables
v1_out_u = ['mm s-1','mm s-1','K','K','K'] 
v2_out_u = ['m s-1','kg kg-1','m','W m-2','W m-2'] 

## labels for plots
labels1= ['RAIN','SNOW','TBOT','THBOT','THBOT'] 
labels2= ['WIND','QBOT','ZBOT','FLDS','FSDS'] 

MultiPlot3PFTs(v1_out,v1_out_u,labels1,'Forcings', sim1, sim2)
MultiPlot3PFTs(v2_out,v2_out_u,labels2,'Forcings2', sim1, sim2)



#%% FUNCTION TO PLOT MULTIPLOTS DELTA-ERRORS 5-VARIABLES plots
# Soil Layer d=2
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

# Plot Errors
label_delta = 'Error = eCLM - clm5'    
MultiPlot3PFTs_delta(v1_out,v1_out_u,labels1,'Delta_Forcings',label_delta,error)
MultiPlot3PFTs_delta(v2_out,v2_out_u,labels2,'Delta_Forcings2',label_delta,error)



