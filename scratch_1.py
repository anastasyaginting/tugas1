gaji = int(input("Masukkan gaji"))
berkeluarga = (False, True)[input("Sudah berkeluarga? (Y/T)") == "Y"]
punya_rumah = (False, True)[input("Punya rumah? (Y/T)") =="Y"]

if gaji > 3000000:
    print ("Gaji sudah diatas UMR")
    if berkeluarga:
        print ("Wajip ikutan asuransidan menabung untuk pensiun")
    else:
        print ("Tidak perlu ikutan asuransi")

    if punya_rumah:
        print ("Wajip bayar pajak rumah")
    else:
        print ("Tidak wajip bayar pajak rumah")
else:
    print ("Gaji belom UMR" )
