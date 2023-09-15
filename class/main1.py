#!/opt/miniconda3/bin/python3

import os
from peptide import Peptide

def pep_pattern(aa):
    chunk_len=3
    chunk=aa+" LYS LYS " # Make sure to leave a space at the end!
    return (chunk,chunk_len) # return a tuple

def main():
    for repeat in range(4,10):
        for aa in ['ALA','GLY','LEU','TYR']:
            
            sys_nm=str(repeat)+str(aa)
            ch,ch_len=pep_pattern(aa)
            print(ch,ch_len)
            
            #print("creating system... "+sys_nm)
            #peptide_obj=Peptide(sys_nm,ch,ch_len,repeat)
            #peptide_obj.make_pdb()
            
            #print("solvating system... "+sys_nm)
            #peptide_obj.solvate_pdb()
            
            #print("getting box dim for system: "+sys_nm)
            #peptide_obj.box_size()
        
            #print("Cleaning up files for "+sys_nm)
            #os.system("mkdir -p "+sys_nm)
            #os.system("mv "+sys_nm+"* "+sys_nm)
            #os.system("mv *.inp "+sys_nm) #mv equil.inp and prod.inp
            #os.system("cp scripts/submit.sh "+sys_nm)

if __name__ == "__main__":
    main()

#TESTING
#p1=Peptide("6ALA","LYS LYS ALA ",3,2)
#p1.make_pdb()
#p1.solvate_pdb()
#p1.box_size()
