#process argv. $1=file_name="${peptide_name}_wb_ionized"; $2=path_name
set i 0; foreach n $argv {set [incr i] $n}
set suffix "_dim"
set outFile_name $1${suffix}
set outFile [open $outFile_name.out w]

#Get waterbox dimensions:
set all [atomselect top "all"]
set bounds [measure minmax $all]
set box [vecsub [lindex $bounds 1] [lindex $bounds 0]]
set center [measure center $all]


puts $outFile "set boxtype  rect"
puts $outFile "set xtltype  cubic"
puts $outFile "set a [lindex $box 0]"
puts $outFile "set b [lindex $box 1]"
puts $outFile "set c [lindex $box 2]"
puts $outFile "set alpha 90.0"
puts $outFile "set beta  90.0"
puts $outFile "set gamma 90.0"
puts $outFile "set fftx  72"
puts $outFile "set ffty  72"
puts $outFile "set fftz  72"
puts $outFile "set xcen [lindex $center 0]"
puts $outFile "set ycen [lindex $center 1]"
puts $outFile "set zcen [lindex $center 2]"
puts $outFile "set system_name ${1}_wb_ionized"

#$all delete
quit
