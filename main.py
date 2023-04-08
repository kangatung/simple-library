def main_functions():
	print("Perpustakaan\nv1.0\n\n")
	print("[1].Data List Buku")
	print("[2].Tambah List Buku Baru")
	print("[3].Delete Data List Buku")
	print("[4].Reset Data")
	print("[5].Exit\n")
	
	input_main = int(input(">>> "))
	
	if input_main == 1:
		data_list()
	elif input_main == 2:
		tambah_list()
	elif input_main == 3:
		delete_data()
	elif input_main == 4:
		reset_data()
	elif input_main == 5:
		exit()
	else:
		main_functions()
	
	
def data_list():
	print("\n")
	open_file = open("dataperpus.txt","r")
	print(open_file.read())
	open_file.close()
	
	
def tambah_list():
	tambah_file = open("dataperpus.txt","a")
	input_tambah = input("Silahkan masukkan judul buku yang baru: ")
	tambah_file.write(input_tambah)
	tambah_file.write("\n")
	tambah_file.close()
	print("Buku dengan judul %s berhasil ditambahkan\n" %(input_tambah))
	
	
def delete_data():
	delete_file = open("dataperpus.txt","r+")
	list_number = int(input("Silahkan masukkan data yang ingin di hapus: "))
	list_name = delete_file.readlines()
	del list_name[list_number - 1]
	print("data berhasil diperbarui!!!\n\n")
	list_name2 = "".join(list_name)
	print(list_name2)
	delete_file.close()
	
	delete_file = open("dataperpus.txt","w")
	delete_file.write(list_name2)
	delete_file.close()
	
	
def reset_data():
	reset_file = open("dataperpus.txt","w")
	reset_file.write("")
	reset_file.close()
	
while True:	
	main_functions()


























