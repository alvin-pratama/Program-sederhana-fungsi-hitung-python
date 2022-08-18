print("""
Opsi:
## bidang 3D
	# rumus volume
		1. Volume Kubus
		2. Volume Balok
		3. Volume Limas Segitiga
		4. Volume Limas Segiempat
		5. Volume Prisma Segitiga
		6. Volume Prisma Segiempat
		7. Volume Tabung
	""")

opsi = int(input("Masukkan Opsi: "))

match opsi:
	case 1:
		print("\n#########-Hitung Volume Kubus-##########")
		rusuk = float(input("masukkan rusuk: "))
		def func_volumeKubus(rusuk):
			volume = rusuk**3
			print("rumus: s^3")
			print("volume kubus adalah: "+str(volume)+"cm^3")
		func_volumeKubus(rusuk)
	case 2:
		print("\n#########-Hitung Volume Balok-##########")
		rusuk_p = float(input("masukkan panjang alas: "))
		rusuk_l = float(input("masukkan lebar alas: "))
		rusuk_t = float(input("masukkan tinggi balok: "))
		def func_volumeBalok(rusuk_p, rusuk_l, rusuk_t):
			volume = rusuk_p*rusuk_l*rusuk_t
			print("rumus: p*l*t -> Luas Alas Persegi*Tinggi")
			print("volume balok adalah: "+str(volume)+"cm^3")
		func_volumeBalok(rusuk_p, rusuk_l, rusuk_t)
	case 3:
		print("\n#########-Hitung Volume Limas Segitiga-##########")
		rusuk_alas_segitiga = float(input("masukkan alas segitiga: "))
		rusuk_tinggi_segitiga = float(input("masukkan tinggi segitiga: "))
		rusuk_tinggi_limas = float(input("masukkan tinggi limas: "))
		def func_volumeLimassegitiga(rusuk_alas_segitiga, rusuk_tinggi_segitiga, rusuk_tinggi_limas):
			volume = 1/3*(1/2*(rusuk_alas_segitiga*rusuk_tinggi_segitiga))*rusuk_tinggi_limas
			print("rumus: 1/3*(1/2*a*t)*t -> 1/3*Luas Alas Segitiga*Tinggi Limas")
			print("volume limas segitiga adalah: "+str(volume)+"cm^3")
		func_volumeLimassegitiga(rusuk_alas_segitiga, rusuk_tinggi_segitiga, rusuk_tinggi_limas)
	case 4:
		print("\n#########-Hitung Volume Limas Segiempat-##########")
		rusuk_panjang_persegi = float(input("masukkan alas persegi: "))
		rusuk_lebar_persegi = float(input("masukkan tinggi persegi: "))
		rusuk_tinggi_limas = float(input("masukkan tinggi limas: "))
		def func_volumeLimassegiempat(rusuk_panjang_persegi, rusuk_lebar_persegi, rusuk_tinggi_limas):
			volume = 1/3*(rusuk_panjang_persegi*rusuk_lebar_persegi)*rusuk_tinggi_limas
			print("rumus: 1/3*(p*l)*t -> 1/3*Luas Alas Segiempat*Tinggi Limas")
			print("volume limas segiempat adalah: "+str(volume)+"cm^3")
		func_volumeLimassegiempat(rusuk_panjang_persegi, rusuk_lebar_persegi, rusuk_tinggi_limas)
	case 5:
		print("\n#########-Hitung Volume Prisma Segitiga-##########")
		rusuk_alas_segitiga = float(input("masukkan alas segitiga: "))
		rusuk_tinggi_segitiga = float(input("masukkan tinggi segitiga: "))
		rusuk_tinggi_prisma = float(input("masukkan tinggi prisma: "))
		def func_volumePrismasegitiga(rusuk_alas_segitiga, rusuk_tinggi_segitiga, rusuk_tinggi_prisma):
			volume = 1/2*(rusuk_alas_segitiga*rusuk_tinggi_segitiga)*rusuk_tinggi_prisma
			print("rumus: (1/2*a*t)*t -> Luas Alas Segitiga*Tinggi Prisma")
			print("volume prisma segitiga adalah: "+str(volume)+"cm^3")
		func_volumePrismasegitiga(rusuk_alas_segitiga, rusuk_tinggi_segitiga, rusuk_tinggi_prisma)
	case 6:
		print("\n#########-Hitung Volume Prisma Segiempat-##########")
		rusuk_panjang_persegi = float(input("masukkan alas persegi: "))
		rusuk_lebar_persegi = float(input("masukkan tinggi persegi: "))
		rusuk_tinggi_prisma = float(input("masukkan tinggi prisma: "))
		def func_volumePrismasegiempat(rusuk_panjang_persegi, rusuk_lebar_persegi, rusuk_tinggi_prisma):
			volume = (rusuk_panjang_persegi*rusuk_lebar_persegi)*rusuk_tinggi_prisma
			print("rumus: (p*l)*t -> Luas Alas Segiempat*Tinggi Prisma")
			print("volume prisma segiempat adalah: "+str(volume)+"cm^3")
		func_volumePrismasegiempat(rusuk_panjang_persegi, rusuk_lebar_persegi, rusuk_tinggi_prisma)
	case 7:
		print("\n#########-Hitung Volume Tabung-##########")
		print("opsi: (d)iameter, ja(r)i-jari")
		opsi = str(input("masukkan r/d: "))
		if (opsi == "r"):
			jari_jari = float(input("masukkan jari-jari: "))
			tinggi_tabung = float(input("masukkan tinggi tabung: "))
			def func_volumeTabung(r, t):
				volume = 3.14*(r**2)*t
				print("rumus: π*r²*t")
				print("volume tabung adalah: "+str(volume)+"cm^3")
			func_volumeTabung(jari_jari, tinggi_tabung)
		elif (opsi == "d"):
			diameter = float(input("masukkan diameter: "))
			tinggi_tabung = float(input("masukkan tinggi tabung: "))
			def func_volumeTabung(d, t):
				volume = 3.14*((d/2)**2)*t
				print("rumus: π*(d/2)²*t")
				print("volume tabung adalah: "+str(volume)+"cm^3")
			func_volumeTabung(diameter, tinggi_tabung)
		else :
			print("\nmaaf masukkan anda salah")
	case _:
		print("\nmaaf opsi nomor "+str(opsi)+" tidak tersedia")