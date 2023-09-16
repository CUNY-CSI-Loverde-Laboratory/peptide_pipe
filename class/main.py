#!/opt/miniconda3/bin/python3

import os
from peptide import Peptide

def pep_pattern():
    
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

def main():
            
    filename, sequence, count = pep_pattern()
    
    for i in range( 3 ):
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

