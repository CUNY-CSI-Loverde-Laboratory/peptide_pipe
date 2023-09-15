#!/opt/miniconda3/bin/python3

import os
from peptide import Peptide

def pep_pattern(chunk,chunk_len,repeat_len):
    #peptide=""
    #for i in range(0,repeat_len):
    #    peptide = peptide+chunk
    
    peptide=chunk*repeat_len

    return (peptide,chunk_len*repeat_len) # return a tuple

def main():
    pos_res=["ARG","LYS"]
    aro_res=["TYR","PHE"]
    neu_res=["ALA","GLY","LEU"]

    # SET #5: Alternating +AHHHH:
    for repeat in range(2,5): # 2 to 4+1
        for i in [0,1]:
            for j in [0,1]:
                for k in [0,1,2]:
                    print(repeat,i,j,k)
                    #pep,pep_len = pep_pattern(pos_res[i]+" "+aro_res[j]+" ",2,repeat)
                    
                    ch=(pos_res[i]+" ")*2+(aro_res[j]+" ")*2+(neu_res[k]+" ")*4
                
                    ch_len=8
                    aa=pos_res[i]+aro_res[j]+neu_res[k]

                    sys_nm=str(repeat)+str(aa)
                    print(ch,ch_len)
                
                    print("creating system... "+sys_nm)
                    peptide_obj=Peptide(sys_nm,ch,ch_len,repeat)
                    peptide_obj.make_pdb(alt_chirality=False)
            
                    print("solvating system... "+sys_nm)
                    peptide_obj.solvate_pdb()
            
                    print("getting box dim for system: "+sys_nm)
                    peptide_obj.box_size()
        
                    print("Cleaning up files for "+sys_nm)
                    os.system("mkdir -p "+sys_nm)
                    os.system("mv "+sys_nm+"* "+sys_nm)
                    os.system("mv *.inp "+sys_nm) #mv equil.inp and prod.inp
                    os.system("cp scripts/submit.sh "+sys_nm)

if __name__ == "__main__":
    main()

#TESTING
#p1=Peptide("6ALA","LYS LYS ALA ",3,2)
#p1.make_pdb()
#p1.solvate_pdb()
#p1.box_size()
