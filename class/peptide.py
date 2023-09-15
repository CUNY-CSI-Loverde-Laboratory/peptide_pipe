import os

class Peptide:
    def __init__(self,name,chunk,chunk_len,repeat):
        self.name=str(name)
        self.chunk=str(chunk)
        self.repeat=int(repeat)
        self.chunk_len=int(chunk_len)
        self.peptide_len=int(chunk_len*repeat)

        print(self.name,self.chunk,self.repeat)
    
    def make_pdb(self,alt_chirality=False):
        chunk=self.chunk
        sys_nm=self.name
        re=self.repeat
        ch_len=self.chunk_len
        p_len=self.peptide_len
        D_pos=[]
        
        f=open(sys_nm+".txt", "w")
        f.write("source leaprc.protein.ff14SB \n")
        seq=chunk*re
        f.write("foo = sequence { " + seq + "}")
        p_len=re*ch_len
        
        if(alt_chirality==True):
            for j in range(p_len):
                if(j%2==1):
                    f.write("\nselect foo."+str(j)+".CA")
                    D_pos.append(j)
        
            f.write("\nflip foo")
            
        f.write("\nsavepdb foo "+sys_nm+".pdb\nquit")
        f.close()
        os.system("./scripts/tleap.sh "+sys_nm+".txt")
        
        if(alt_chirality==True):
            #Change from L label to D Label:
            f2=open(sys_nm+".pdb", "r")
            f3=open(sys_nm+"D.pdb","w")
        
            for line in f2:
                try:
                    if int(line.split()[4]) in D_pos:
                        aa='D'+line.split()[3]
                        #aa=aa[:-1]
                        new_line=line.replace(line.split()[3]+" ",aa)
                        f3.write(new_line)
                    else:
                        f3.write(line)
                except:
                    print("End of pdb file")
                    f3.write("TER\nEND")
                    f2.close()
                    f3.close()
                    break

            #os.system("rm leap.log")
            os.system("rm "+sys_nm+".pdb")
            os.system("mv "+sys_nm+"D.pdb "+sys_nm+".pdb")
            ## END if alt_chirality == True

    #END def make_pdb

    def solvate_pdb(self):
        sys_nm=self.name
        
        os.system("vmd -dispdev text -e scripts/solvate.tcl -args "+sys_nm+" | tee "+sys_nm+"_solvate.log")
        #os.system("rm protein_solvate.log")

    def box_size(self):
        sys_nm=self.name
    
        os.system("vmd -dispdev text -pdb "+sys_nm+"_wb_ionized.pdb -e scripts/box_size.tcl -args "+sys_nm+" > "+sys_nm+"wb_ionized_dim.log")
        os.system("sed \"s/system_wb_ionized_dim.out/"+sys_nm+"_dim.out/\" scripts/01_equil_ex.inp > 01_equil.inp")
        os.system("sed \"s/system_wb_ionized_dim.out/"+sys_nm+"_dim.out/\" scripts/02_prod_ex.inp > 02_prod.inp")

#TESTING
#p1=Peptide("6ALA","LYS LYS ALA ",3,2)
#p1.make_pdb()
#p1.solvate_pdb()
#p1.box_size()

