USERNAME=""

/home/$USERNAME/NAMD_2.14_Linux-x86_64-multicore-CUDA/charmrun +p 4  /home/$USERNAME/NAMD_2.14_Linux-x86_64-multicore-CUDA/namd2 01_equil.inp +devices 0,1 > 01_equil.log &&
/home/$USERNAME/NAMD_2.14_Linux-x86_64-multicore-CUDA/charmrun +p 4  /home/$USERNAME/NAMD_2.14_Linux-x86_64-multicore-CUDA/namd2 02_prod.inp +devices 0,1 > 02_prod.log &
