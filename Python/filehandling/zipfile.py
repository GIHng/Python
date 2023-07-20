import tarfile

import zipfile

filelist = ["./data.dat", "./test.bin"]
tarfile.TarFile


with tarfile.TarFile('./test.tar', 'w') as myzip:
    for temp in filelist:
        myzip.write(temp)