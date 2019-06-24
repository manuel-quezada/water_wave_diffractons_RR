# Installation of Proteus

## Download Proteus and checkout an specific commit
```
git clone https://github.com/erdc/proteus.git
cd proteus
git checkout da1e64e2399161d00560def8d2f80a12bb91cd99
```

## First compilation
This compilation will take care mainly of the dependencies. Inside the folder /proteus (created after cloning the repository) do:
```
make develop
```

## Checkout an specific stack
The following is needed to run the same code used in this work.
```
cd stack
git checkout f67c263af9261c1e0fc5473b38451998ac3e0797
cd ..
make distclean
```

## Change setup and final compilation
* Copy the file setup.py (provided here) into the folder /proteus.
* Run again:
```
make develop 
```

## Export the compiled objects
Finally, make the compiled objects visible for the system.
```
export PATH=/dir/where/proteus/was/cloned/proteus/linux2/bin:${PATH}
```

## Some tips for the installation of Proteus
* All the instructions here were tested using Ubuntu 16.04.
* Make sure you have fortran compilers before starting the installation. We use gfortran.
* If `make develop` fails, do it again since some missing files might need to be created the first time.
* The installation might fail to download some dependency. One can use a dedicated server to download the dependencies. To do that:
  * Inside the folder /proteus do
    ```
    ./hashdist/bin/hit remote add http://levant.hrwallingford.com/hashdist_src --objects="source"
    ```
  * Then run again:
    ```
    make develop
    ```
* For more information see https://github.com/erdc/proteus/wiki.
