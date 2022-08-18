print("""
Opsi:
## bidang 2D
	# rumus keliling
		1. Keliling Segitiga
		2. Keliling Persegi
		3. Keliling Persegi Panjang
		4. Keliling Jajar Genjang
		5. Keliling Trapesium
		6. Keliling Lingkaran
	# rumus luas
		7. Luas Segitiga
		8. Luas Persegi
		9. Luas Persegi Panjang
		10. Luas Jajar Genjang
		11. Luas Trapesium
		12. Luas Lingkaran
	""")

opsi = int(input("Masukkan Opsi: "))

match opsi:
	case 1:
		print("\n#########-Hitung Keliling Segitiga-##########")
		sisi_a = float(input("masukkan sisi a: "))
		sisi_b = float(input("masukkan sisi b: "))
		sisi_c = float(input("masukkan sisi c: "))
		def func_kelilingSegitiga(sisi_a, sisi_b, sisi_c):
			keliling = sisi_a + sisi_b + sisi_c
			print("rumus: a+b+c")
			print("keliling segitiga adalah: "+str(keliling)+"cm")
		func_kelilingSegitiga(sisi_a, sisi_b, sisi_c)
	case 2:
		print("\n#########-Hitung Keliling Persegi-##########")
		sisi = float(input("masukkan sisi: "))
		def func_kelilingPersegi(sisi):
			keliling = 4 * sisi
			print("rumus: 4*sisi")
			print("keliling persegi adalah: "+str(keliling)+"cm")
		func_kelilingPersegi(sisi)
	case 3:
		print("\n#########-Hitung Keliling Persegi Panjang-##########")
		sisi_a = float(input("masukkan sisi a: "))
		sisi_b = float(input("masukkan sisi b: "))
		def func_kelilingPersegipanjang(sisi_a, sisi_b):
			keliling = (2 * sisi_a) + (2 * sisi_b)
			print("rumus: 2*(a+b)")
			print("keliling persegi panjang adalah: "+str(keliling)+"cm")
		func_kelilingPersegipanjang(sisi)
	case 4:
		print("\n#########-Hitung Keliling Jajar Genjang-##########")
		sisi_a = float(input("masukkan sisi a: "))
		sisi_b = float(input("masukkan sisi b: "))
		def func_kelilingJajargenjang(sisi_a, sisi_b):
			keliling = (2 * sisi_a) + (2 * sisi_b)
			print("rumus: 2*(a+b)")
			print("keliling jajar genjang adalah: "+str(keliling)+"cm")
		func_kelilingJajargenjang(sisi)
	case 5:
		print("\n#########-Hitung Keliling Trapesium-##########")
		sisi_a = float(input("masukkan sisi a: "))
		sisi_b = float(input("masukkan sisi b: "))
		sisi_c = float(input("masukkan sisi c: "))
		sisi_d = float(input("masukkan sisi d: "))
		def func_kelilingTrapesium(sisi_a, sisi_b, sisi_c, sisi_d):
			keliling = sisi_a + sisi_b + sisi_c + sisi_d
			print("rumus: a+b+c+d")
			print("keliling trapesium adalah: "+str(keliling)+"cm")
		func_kelilingTrapesium(sisi_a, sisi_b, sisi_c, sisi_d)
	case 6:
		print("\n#########-Hitung Keliling Lingkaran-##########")
		print("opsi: (d)iameter, ja(r)i-jari")
		opsi = str(input("masukkan r/d: "))
		if (opsi == "r"):
			jari_jari = float(input("masukkan jari-jari: "))
			def func_kelilingLingkaran(r):
				keliling = 2 * 3.14 * r
				print("rumus: 2*π*r")
				print("keliling lingkaran adalah: "+str(keliling)+"cm")
			func_kelilingLingkaran(jari_jari)
		elif (opsi == "d"):
			diameter = float(input("masukkan diameter: "))
			def func_kelilingLingkaran(d):
				keliling = 3.14 * d
				print("rumus: π*d")
				print("keliling lingkaran adalah: "+str(keliling)+"cm")
			func_kelilingLingkaran(diameter)
		else :
			print("\nmaaf masukkan anda salah")
	case 7:
		print("\n#########-Hitung Luas Segitiga-##########")
		alas = float(input("masukkan alas: "))
		tinggi = float(input("masukkan tinggi: "))
		def func_luasSegitiga(alas, tinggi):
			luas = 0.5 * alas * tinggi
			print("rumus: 1/2*a*t")
			print("luas segitiga adalah: "+str(luas)+"cm^2")
		func_luasSegitiga(alas, tinggi)
	case 8:
		print("\n#########-Hitung Luas Persegi-##########")
		sisi = float(input("masukkan sisi: "))
		def func_luasPersegi(sisi):
			luas = sisi**2
			print("rumus: s^2")
			print("luas persegi adalah: "+str(luas)+"cm^2")
		func_luasPersegi(sisi)
	case 9:
		print("\n#########-Hitung Luas Persegi Panjang-##########")
		panjang = float(input("masukkan alas: "))
		lebar = float(input("masukkan tinggi: "))
		def func_luasPersegipanjang(panjang, lebar):
			luas = panjang * lebar
			print("rumus: p*l")
			print("luas persegi panjang adalah: "+str(luas)+"cm^2")
		func_luasPersegipanjang(panjang, lebar)
	case 10:
		print("\n#########-Hitung Luas Jajar Genjang-##########")
		alas = float(input("masukkan alas: "))
		tinggi = float(input("masukkan tinggi: "))
		def func_luasJajargenjang(alas, tinggi):
			luas = alas * tinggi
			print("rumus: a*t")
			print("luas jajar genjang adalah: "+str(luas)+"cm^2")
		func_luasJajargenjang(alas, tinggi)
	case 11:
		print("\n#########-Hitung Luas Trapesium-##########")
		sisi_atas = float(input("masukkan sisi atas: "))
		sisi_bawah = float(input("masukkan sisi bawah: "))
		tinggi = float(input("masukkan tinggi: "))
		def func_luasTrapesium(sisi_atas, sisi_bawah, tinggi):
			luas = 0.5*tinggi*(sisi_atas+sisi_bawah)
			print("rumus: 1/2*t*(a+b)")
			print("luas trapesium adalah: "+str(luas)+"cm^2")
		func_luasTrapesium(sisi_atas, sisi_bawah, tinggi)
	case 12:
		print("\n#########-Hitung Luas Lingkaran-##########")
		print("opsi: (d)iameter, ja(r)i-jari")
		opsi = str(input("masukkan r/d: "))
		if (opsi == "r"):
			jari_jari = float(input("masukkan jari-jari: "))
			def func_luasLingkaran(r):
				luas = 3.14 * (r**2)
				print("rumus: π*(r^2)")
				print("luas lingkaran adalah: "+str(luas)+"cm^2")
			func_luasLingkaran(jari_jari)
		elif (opsi == "d"):
			diameter = float(input("masukkan diameter: "))
			def func_luasLingkaran(d):
				luas = 3.14 * ((d/2)**2)
				print("luas lingkaran adalah: "+str(luas)+"cm^2")
				print("rumus: π*((d/2)^2)")
			func_luasLingkaran(diameter)
		else :
			print("\nmaaf masukkan anda salah")
	case _:
		print("\nmaaf opsi nomor "+str(opsi)+" tidak tersedia")