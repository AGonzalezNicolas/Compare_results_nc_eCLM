#!/bin/bash
# Author Ana Gonzalez-Nicolas based on Daniel Caviedes-Voullieme's script

# Uses NCO
ml Stages/2024  GCC/12.3.0  OpenMPI/4.1.5
module load NCO/5.1.8

# NAMES OF nc FILES TO COMPARE:
# Name_TEST=$1
# Name_REF=$2
# ncdiff $Name_TEST $Name_REF -O diff.nc
Name_TEST=/p/project1/cslts/gonzalez5/CLM5/eCLM_Paul/eCLM_last_PSmpi_release/eCLM/Tests/CaseDocs_1x1_wuestebach_2009_forcings_DP_1_PSmpi_release/1x1_wuestebach_2009_forcings_DP_1.clm2.h0.2009-01-01-00000.nc
Name_REF=/p/scratch/cslts/gonzalez5/CLM5_DATA/Archive/lnd/hist/1x1_wuestebach_2009_forcings_DP_1.clm2.h0.2009-01-01-00000.nc

ncdiff $Name_TEST $Name_REF diff.nc

####
# zero=0.000001      # threshold = 10E-6 ( 6 variables error > threshold for year 2009)
# zero=0.0000001     # threshold = 10E-7 ( 7 variables error > threshold for year 2009)
zero=0.00000001  # threshold = 10E-8 (16 variables error > threshold for year 2009)
fac=86400.0      # factor from seconds to days

# GPP  Gross primary production (gC/m^2/s)
# NEE  Net ecosystem exchange of carbon, includes fire and hrv_xsmrpool (gC/m^2/s)
# ER   Total ecosystem respiration (autotrophic + heterotrophic) (gC/m^2/s)
# AR   Autotrophic respiration (MR + GR)(gC/m^2/s)
# HR   Total heterotrophic respiration (gC/m^2/s)

# QSOIL  Ground evaporation (soil/snow evaporation + soil/snow sublimation - dew) (mm/s)
# QVEGE  Canopy evaporation (mm/s)
# QVEGT  Tanopy transpiration (mm/s)
# QOVER  Total surface runoff (includes QH2OSFC) (mm/s)

# EFLX_LH_TOT     Total latent heat flux [+ to atm] (W/m^2)
# FSH             Sensible heat not including correction for land use change and rain/snow conversion (W/m^2)
# Rnet            Net radiation (W/m^2)
# QFLX_EVAP_TOT   qflx_evap_soi + qflx_evap_can + qflx_tran_veg (kg/m^2/s)

# GRAINC          Grain C (does not equal yield) (gC/m^2)
# LEAFC           Leaf C (gC/m^2)
# DEADSTEMC       Dead steam C (gC/m^2)
# FROOTC          Fine root C (gC/m^2)
# GRAINC_TO_FOOD  Grain C to food (gC/m^2/s)

####

echo "Variables being checked for MAXIMUM ABSOLUTE ERROR:"
echo "C_fluxes variables: GPP, NEE, ER, AR , HR"
echo "H2O_fluxes variables: QSOIL, QVEGE, QVEGT, QOVER"
echo "Energy_fluxes variables: EFLX_LH_TOT, FSH, Rnet, QFLX_EVAP_TOT"
echo "Biomass variables: GRAINC, LEAFC, DEADSTEMC, FROOTC, GRAINC_TO_FOOD"
echo " "

####

ncap2 -O -s 'max_GPP=abs(max(GPP))' diff.nc max.nc
ncap2 -A -s 'max_NEE=abs(max(NEE))' diff.nc max.nc
ncap2 -A -s 'max_ER=abs(max(ER))' diff.nc max.nc
ncap2 -A -s 'max_AR=abs(max(AR))' diff.nc max.nc
ncap2 -A -s 'max_HR=abs(max(HR))' diff.nc max.nc

ncap2 -A -s 'max_QSOIL=abs(max(QSOIL))' diff.nc max.nc
ncap2 -A -s 'max_QVEGE=abs(max(QVEGE))' diff.nc max.nc
ncap2 -A -s 'max_QVEGT=abs(max(QVEGT))' diff.nc max.nc
ncap2 -A -s 'max_QOVER=abs(max(QOVER))' diff.nc max.nc
#ncap2 -A -s 'max_QIRRIG==abs(max(QIRRIG))' diff.nc max.nc

ncap2 -A -s 'max_EFLX_LH_TOT=abs(max(EFLX_LH_TOT))' diff.nc max.nc
ncap2 -A -s 'max_FSH=abs(max(FSH))' diff.nc max.nc
ncap2 -A -s 'max_Rnet=abs(max(Rnet))' diff.nc max.nc
ncap2 -A -s 'max_QFLX_EVAP_TOT=abs(max(QFLX_EVAP_TOT))' diff.nc max.nc

ncap2 -A -s 'max_GRAINC=abs(max(GRAINC))' diff.nc max.nc
ncap2 -A -s 'max_LEAFC=abs(max(LEAFC))' diff.nc max.nc
ncap2 -A -s 'max_DEADSTEMC=abs(max(DEADSTEMC))' diff.nc max.nc
ncap2 -A -s 'max_FROOTC=abs(max(FROOTC))' diff.nc max.nc
ncap2 -A -s 'max_GRAINC_TO_FOOD=abs(max(GRAINC_TO_FOOD))' diff.nc max.nc

####

GPP=$(ncks -C -H -v max_GPP -s "%.10f" max.nc)
NEE=$(ncks -C -H -v max_NEE -s "%.10f" max.nc)
ER=$(ncks -C -H -v max_ER -s "%.10f" max.nc)
AR=$(ncks -C -H -v max_AR -s "%.10f" max.nc)
HR=$(ncks -C -H -v max_HR -s "%.10f" max.nc)

QSOIL=$(ncks -C -H -v max_QSOIL -s "%.10f" max.nc)
QVEGE=$(ncks -C -H -v max_QVEGE -s "%.10f" max.nc)
QVEGT=$(ncks -C -H -v max_QVEGT -s "%.10f" max.nc)
QOVER=$(ncks -C -H -v max_QOVER -s "%.10f" max.nc)
#QIRRIG=$(ncks -C -H -v max_QIRRIG -s "%.10f" max.nc)

EFLX_LH_TOT=$(ncks -C -H -v max_EFLX_LH_TOT -s "%.10f" max.nc)
FSH=$(ncks -C -H -v max_FSH -s "%.10f" max.nc)
Rnet=$(ncks -C -H -v max_Rnet -s "%.10f" max.nc)
QFLX_EVAP_TOT=$(ncks -C -H -v max_QFLX_EVAP_TOT -s "%.10f" max.nc)

GRAINC=$(ncks -C -H -v max_GRAINC -s "%.10f" max.nc)
LEAFC=$(ncks -C -H -v max_LEAFC -s "%.10f" max.nc)
DEADSTEMC=$(ncks -C -H -v max_DEADSTEMC -s "%.10f" max.nc)
FROOTC=$(ncks -C -H -v max_FROOTC -s "%.10f" max.nc)
GRAINC_TO_FOOD=$(ncks -C -H -v max_GRAINC_TO_FOOD -s "%.10f" max.nc)

####


sumVar=0

#### 
echo "C_fluxes variables with error greater than threshold $zero:"
if (( $(echo "$GPP > $zero" | bc -l) )); then
  temp=$(echo "$GPP * $fac" | bc -l)
  echo "GPP error = $GPP gC/m^2/s = $temp gC/m^2/d"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$NEE > $zero" | bc -l) )); then
  temp=$(echo "$NEE * $fac" | bc -l)
  echo "NEE error = $NEE gC/m^2/s = $temp gC/m^2/d"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$ER > $zero" | bc -l) )); then
  temp=$(echo "$ER * $fac" | bc -l)
  echo "ER error = $ER gC/m^2/s = $temp gC/m^2/d"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$AR > $zero" | bc -l) )); then
  temp=$(echo "$AR * $fac" | bc -l)
  echo "AR error = $AR gC/m^2/s = $temp gC/m^2/d"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$HR > $zero" | bc -l) )); then
  temp=$(echo "$HR * $fac" | bc -l)
  echo "HR error = $HR gC/m^2/s = $temp gC/m^2/d"
  sumVar=$((sumVar+1))
fi

#### 
echo " "
echo "H2O_fluxes variables with error greater than threshold $zero:"
if (( $(echo "$QSOIL > $zero" | bc -l) )); then
  temp=$(echo "$QSOIL * $fac" | bc -l)
  echo "QSOIL error = $QSOIL mm/s = $temp mm/d"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$QVEGE > $zero" | bc -l) )); then
  temp=$(echo "$QVEGE * $fac" | bc -l)
  echo "QVEGE error = $QVEGE mm/s = $temp mm/d"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$QVEGT > $zero" | bc -l) )); then
  temp=$(echo "$QVEGT * $fac" | bc -l)
  echo "QVEGT error = $QVEGT mm/s = $temp mm/d"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$QOVER > $zero" | bc -l) )); then
  temp=$(echo "$QOVER * $fac" | bc -l)
  echo "QOVER error = $QOVER mm/s = $temp mm/d"
  sumVar=$((sumVar+1))
fi
#if ((  $(echo "$QIRRIG > $zero" | bc -l) )); then
#  echo "QIRRIG error = $QIRRIG"
#  $sumVar = $sumVar + 1
#fi


###
echo " "
echo "Energy_fluxes variables with error greater than threshold $zero:"
if (( $(echo "$EFLX_LH_TOT > $zero" | bc -l) )); then
  echo "EFLX_LH_TOT error = $EFLX_LH_TOT W/m^2"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$FSH > $zero" | bc -l) )); then
  echo "FSH error = $FSH W/m^2"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$Rnet > $zero" | bc -l) )); then
  echo "Rnet error = $Rnet W/m^2"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$QFLX_EVAP_TOT > $zero" | bc -l) )); then
  temp=$(echo "$QFLX_EVAP_TOT * $fac" | bc -l)
  echo "QFLX_EVAP_TOT error = $QFLX_EVAP_TOT kg/m^2/s = $temp kg/m^2/d"
  sumVar=$((sumVar+1))
fi

###
echo " "
echo "Biomass variables with error greater than threshold $zero:"
if (( $(echo "$GRAINC > $zero" | bc -l) )); then
  echo "GRAINC error = $GRAINC gC/m^2"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$LEAFC > $zero" | bc -l) )); then
  echo "LEAFC error = $LEAFC gC/m^2"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$DEADSTEMC > $zero" | bc -l) )); then
  echo "DEADSTEMC error = $DEADSTEMC gC/m^2"
  sumVar=$((sumVar+1))
fi
if (( $(echo "$FROOTC > $zero" | bc -l) )); then
  echo "FROOTC error = $FROOTC gC/m^2"
  sumVar=$((sumVar+1))
fi
if ((  $(echo "$GRAINC_TO_FOOD > $zero" | bc -l) )); then
  echo "GRAINC_TO_FOOD error = $GRAINC_TO_FOOD gC/m^2"
  sumVar=$((sumVar+1))
fi


###
echo " "
if [ $sumVar -gt 0 ]; then
  echo "The eCLM comparison test failed for 1 year simulation."
  echo "$sumVar variables have an error greater than the threshold $zero."
  echo " "
  exit 1
else 
  echo "Maximum error is below the threshold $zero for one year."
  echo "Well done!"
  echo "Try with a different year now."
fi
echo " "
