#!/opt/miniconda3/bin/python3

import os
from peptide import Peptide

def pep_pattern1(): # gen1
    
    C = [ "GLU", "ASP", "ARG", "LYS" ]; # Charged
    A = [ "TYR", "PHE" ]; # Aromatic
    H = [ "GLY", "ALA", "LEU" ]; # Hydrophobic
    sequences = []
    filenames = [] 
    counter = 0

    # First Generation:
    for i in range(4): # Charged
        for j in range(2): # Aromatic
            for r in [ 1, 2, 4, 8 ]: # residue repeat in chunk
                pattern = ( C[i] + ' ' ) * r + ( A[j] + ' ' ) * r # 1 chunk
                min_len = ( 64 // len( pattern ) ) # min length = 16 res
                max_len = min_len * 2 # max length = 32 res
			    #print(min_len,max_len)
                
                for k in range( min_len, max_len + 1 ): # variation in length
                    filenames.append( C[i] + str(r) + A[j] + str(r) + '_' + str(k) )
                    sequences.append( pattern * k )
                    counter += 1

    #print(counter)
    return( filenames, sequences, counter )

def pep_pattern(): #gen2

    C = [ "GLU", "ASP", "ARG", "LYS"]; # Charged
    A = ["TYR", "PHE"]; # Aromatic
    H = ["GLY", "ALA", "LEU"]; # Hydrophobic
    counter=0
    sequences = []
    filenames = []

    for i in range(2,5): # repeat num
        for j in range(4): # Charged residues
            for k in range(0,2): # Aromatic residues
                for l in range(0,3): # Hydrophobic residues   
                    filenames.append( C[j] + str(1) + A[k] + str(1) + H[l] + str(6) + '_' + str(i) )
                    sequences.append( ((C[j] + ' ' + A[k] + ' ' + (H[l] + ' ') * 6) * i ) )

                    filenames.append( C[j] + str(2) + A[k] + str(2) + H[l] + str(4) + '_' +str(i) )
                    sequences.append( ((C[j] + ' ') * 2 + (A[k] + ' ') * 2 + (H[l] + ' ') * 4) * i )
				    
                    filenames.append( C[j] + str(3) + A[k] + str(3) + H[l] + str(2) + '_' + str(i) )
                    sequences.append( ((C[j] + ' ') * 3 + (A[k] + ' ') * 3 + (H[l] + ' ') * 2) * i )
                    
                    counter += 3
    #print(counter)
    return(filenames, sequences, counter)

def main():
            
    filename, sequence, count = pep_pattern()
    
    for i in range( count ):
        print( "creating system... " + filename[i] )
        peptide_obj = Peptide( filename[i], sequence[i] )
        peptide_obj.make_pdb()
            
        print( "solvating system... " + filename[i] )
        peptide_obj.solvate_pdb()
            
        print( "getting box dim for system: " + filename[i] )
        peptide_obj.box_size()
        
        print( "Cleaning up files for " + filename[i] )
        os.system( "mkdir -p " + filename[i] )
        os.system( "mv " + filename[i] + "* " + filename[i] )
        os.system( "mv *.inp " + filename[i] ) #mv equil.inp and prod.inp
        os.system( "cp scripts/submit.sh " + filename[i] )

if __name__ == "__main__":
    main()

