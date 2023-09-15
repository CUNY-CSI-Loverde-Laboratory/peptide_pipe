#!/bin/sh 

package require Tk 
package require solvate
package require autoionize
package require psfgen

# Process argv. $1=file_name; $2=path_name
set i 0; foreach n $argv {set [incr i] $n}
set suffix "_wb"
set suffix2 "_ionized"

# Read topology files
resetpsf
topology toppar/toppar_all36_prot_c36m_d_aminoacids.str
#topology toppar/par_all36m_prot.prm
topology toppar/top_all36_prot.rtf
#topology toppar/toppar_all36_prot_c36m_d_aminoacids.str
#topology toppar/toppar_water_ions.str				#
#topology toppar/toppar_all36_moreions.str			#
#topology toppar/toppar_ions_won.str				#

# Build protein segment
segment U {pdb $1.pdb}

# Read protein coordinates from PDB file
pdbalias residue LYS DLYS
coordpdb $1.pdb U

# Guess missing coordinates 
guesscoord

# Write structure and coorsinate files
writepdb $1.pdb
writepsf $1.psf

# End of psfgen commands
# ENDMOL

# Solvate protein
solvate $1.psf $1.pdb -t 10 -o $1${suffix}

# Add neutralizing ions
autoionize -psf $1${suffix}.psf -pdb $1${suffix}.pdb -neutralize -o $1${suffix}${suffix2}

quit
