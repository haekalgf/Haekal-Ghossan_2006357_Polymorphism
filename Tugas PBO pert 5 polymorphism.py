class mollusca:
    def intro(self):
        print("mollusca adalah hewan tripoblastik selomata yang bertubuh lunak")

    def deskripsi(self):
        print("termasuk semua hewan lunak dengan maupun tanpa cangkang, seperti berbagai jenis siput, kiton, kerang-kerangan, serta cumi")

class gastropoda(mollusca):
    def deskripsi(self):
        print("kelas ini meliputi segala jenis siput dan siput telanjang berbagai ukuran, dari ukuran miskrokopis hingga ukuran besar")

class cephalopoda(mollusca):
    def deskripsi(self):
        print("di dalamnya mencakup semua gurita, cumi-cumi, dan sotong")

obj_mollusca= mollusca()
obj_gastropoda = gastropoda()
obj_cephalopoda = cephalopoda()

obj_mollusca.intro()
obj_mollusca.deskripsi()

obj_gastropoda.intro()
obj_gastropoda.deskripsi()

obj_cephalopoda.intro()
obj_cephalopoda.deskripsi()