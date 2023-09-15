#!/opt/miniconda3/bin/python3

import os
from peptide import Peptide

def pep_pattern(chunk,chunk_len,repeat_len):
    peptide=""
    for i in range(0,repeat_len):
        peptide = peptide+chunk

    return (peptide) # return a string

def main():
    pos_res=["ARG","LYS"]
    aro_res=["TYR","PHE"]
    neu_res=["ALA","GLY","LEU"]
    

    # SET #6: Alternating ++AAHHHH:
    for repeat in range(2,5):
        for i in [0,1]:
            for j in [0,1]:
                for k in [0,1,2]:
                    print(repeat,i,j,k)
                    p=pep_pattern(pos_res[i]+" "+aro_res[j]+" "+(neu_res[k]+" ")*6,8,repeat)
                    print(p)

    """
    # SET #5: Alternating +AHHHHHH:
    for repeat in range(2,5):
        for i in [0,1]:
            for j in [0,1]:
                for k in [0,1,2]:
                    print(repeat,i,j,k)
                    p=pep_pattern(pos_res[i]+" "+aro_res[j]+" "+(neu_res[k]+" ")*6,8,repeat)
                    print(p)
    
    
    # SET #1: Alternating +/A
    for repeat in range(8,17):
        for i in [0,1]:
            for j in [0,1]:
                print(repeat,i,j)
                p=pep_pattern(pos_res[i]+" "+aro_res[j]+" ",2,repeat)
                print(p)
    
    print("set#2:")
    #SET #2: Alternating ++/AA:
    for repeat in range(4,9):
        for i in [0,1]:
            for j in [0,1]:
                print(repeat,i,j)
                p=pep_pattern((pos_res[i]+" ")*2+(aro_res[j]+" ")*2,4,repeat)
                print(p)
    
    print("set#3:") 
    #SET #3: Alternating ++++/AAAA:
    for repeat in range(2,5):
        for i in [0,1]:
            for j in [0,1]:
                print(repeat,i,j)
                p=pep_pattern((pos_res[i]+" ")*4+(aro_res[j]+" ")*4,8,repeat)
                print(p)
    
    print("set#4:")    
    #SET #4: Alternating ++++++++/AAAAAAAA:
    for repeat in range(1,3):
        for i in [0,1]:
            for j in [0,1]:
                print(repeat,i,j)
                p=pep_pattern((pos_res[i]+" ")*8+(aro_res[j]+" ")*8,16,repeat)
                print(p)
    """

"""
            sys_nm=str(repeat)+str(aa)
            ch,ch_len=pep_pattern(aa)
            #print(ch,ch_len)
            
            print("creating system... "+sys_nm)
            peptide_obj=Peptide(sys_nm,ch,ch_len,repeat)
            peptide_obj.make_pdb()
            
            print("solvating system... "+sys_nm)
            peptide_obj.solvate_pdb()
            
            print("getting box dim for system: "+sys_nm)
            peptide_obj.box_size()
        
            print("Cleaning up files for "+sys_nm)
            os.system("mkdir -p "+sys_nm)
            os.system("mv "+sys_nm+"* "+sys_nm)
            os.system("mv *.inp "+sys_nm) #mv equil.inp and prod.inp
            os.system("cp scripts/submit.sh "+sys_nm)
"""
if __name__ == "__main__":
    main()

#TESTING
#p1=Peptide("6ALA","LYS LYS ALA ",3,2)
#p1.make_pdb()
#p1.solvate_pdb()
#p1.box_size()
