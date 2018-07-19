#!/bin/bash
## =====================================================================
# For getting the environment to filter lists
#
## =====================================================================

wd=${HOME}/.local/src
ad=${HOME}/.local/opt/anaconda
al='https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh'
ai='conda_install.bash'

BASH_RC="$HOME/.bash_profile"

for d in "$wd" "$ad"; do 
  mkdir -p $d; 
done

cd $wd

# Get miniconda installation script
curl "$al" > "$ai"
# Batch run miniconda installer with custom path
bash "$ai" -b -p "$ad" 
# Update environment path for future
echo export PATH="$ad":"\$PATH" >> $BASH_RC
# Update environment for script
export PATH="$ad":"$PATH"
conda update conda 
# Install necessary packages
conda install numpy scipy pandas matplotlib ipython jupyter natsort

printf "\n"
for k in $(seq 0 5); do
  for j in $(seq 0 $k); do
    esc_str='\e[1;'$((30+j))'m%s\e[m'
    printf "$esc_str" "<3"
  done
  printf "\n"
done

for k in $(seq 0 4); do
  for j in $(seq 0 $((4-k))); do
    esc_str='\e[1;'$((30+j))'m%s\e[m'
    printf "$esc_str" "<3"
  done
  printf "\n"
done
printf "\n\nAll Done <3 <3 <3\n\n"

