#case 1

#input
bagian= "case 1"
kipas_angin = 25000
sepeda= 6000
helm_rossi= 8000
diskon1= 10/100
diskon2= 55/100
diskon3= 77/100
jumlah1= 5
jumlah2= 2
jumlah3= 10

#output
print (bagian)
print ("====GEBYAR DISKON====")
print ("====MASUKKAN JUMLAH BARANG YANG DIPESAN====")
print ("KIPAS ANGIN DISKON 10% Rp. 25000,00 : 5")
print ("SEPEDA DISKON 55%      Rp. 6000,00  : 2")
print ("HELM ROSSI DISKON 77%  Rp. 8000,00  : 10")
print ("====TOTAL====")
print ("TOTAL KIPAS ANGIN :Rp.", kipas_angin * jumlah1 * diskon1)
print ("TOTAL SEPEDA SUPER :Rp.", sepeda * 2 * 55/100)
print ("TOTAL HELM ROSSI :Rp.", helm_rossi * 10 * diskon3)
print ("JUMLAH TOTAL DISKON YANG DIDAPAT ADALAH :Rp.", 12500 + 6600 + 61600)


#case 2

#input
bagian= "case 2"
kipas_angin = 25000
sepeda= 6000
helm_rossi= 8000
diskon1= 10/100
diskon2= 55/100
diskon3= 77/100
jumlah1= 10
jumlah2= 10
jumlah3= 10

#output
print (bagian)
print ("====GEBYAR DISKON====")
print ("====MASUKKAN JUMLAH BARANG YANG DIPESAN====")
print ("KIPAS ANGIN DISKON 10% Rp. 25000,00 : 10")
print ("SEPEDA DISKON 55%      Rp. 6000,00  : 10")
print ("HELM ROSSI DISKON 77%  Rp. 8000,00  : 10")
print ("====TOTAL====")
print ("TOTAL KIPAS ANGIN :Rp.", kipas_angin * jumlah1 * diskon1)
print ("TOTAL SEPEDA SUPER :Rp.", sepeda * 10 * 55/100)
print ("TOTAL HELM ROSSI :Rp.", helm_rossi * 10 * diskon3)
print ("JUMLAH TOTAL DISKON YANG DIDAPAT ADALAH :Rp.", 25000 + 33000 + 61600)
