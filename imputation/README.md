# this folder for
 - creating a new reference dataset from 1000G data, with a particular population removed
 - generating a test dataset, given
   - plink dataset
   - set of markers (the virtual "chip")
   - set of individuals
 - running IMPUTE2, given
  - input dataset
  - custom reference location


# prerequisites
 - PLINK1.9
 - IMPUTE2
 - IMPUTE2 reference data
   - unzip 1000GP_Phase3.tgz into "input"
   - 1000GP_Phase3.tgz here https://mathgen.stats.ox.ac.uk/impute/1000GP_Phase3.html
