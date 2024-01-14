import mysql.connector
from tabulate import tabulate
class Furniture:
    def __init__(self) -> None:
        self.konfigurasi = {
            'host': "localhost",
            'user': "root",
            'password': "",
            'database': "5220411274"
        }
        self.connection = None
        self.cursor = None
    
    def connect(self):
        self.connection = mysql.connector.connect(**self.konfigurasi)
        self.cursor = self.connection.cursor()
    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self,data):
        kolom = ', '.join(data.keys())
        list_isi = []
        for i in data.values():
            list_isi.append("%s")
        isi = ', '.join(list_isi)
        insert_query = f"INSERT INTO tb_barang ({kolom}) VALUES({isi})"
        self.cursor.execute(insert_query,tuple(data.values()))
        self.connection.commit()
        return self.cursor.lastrowid
    
    def update(self,id, data):
        set_inputan = []

        for key in data.keys():
            set_inputan.append(f"{key} = %s")
        set_clause = ', '.join(set_inputan)
        update_value = list(data.values())
        update_value.append(id)
        update_query = f"UPDATE tb_barang SET {set_clause} WHERE id = %s"
        self.cursor.execute(update_query,tuple(update_value))
        self.connection.commit()
        return self.cursor.rowcount
    
    def delete(self,id):
        delete_query = f"DELETE FROM tb_barang WHERE id = %s"
        self.cursor.execute(delete_query,(id,))
        self.connection.commit()
    
    def lihat(self):
        lihat_data = f"SELECT * FROM tb_barang"
        self.cursor.execute(lihat_data)
        hasil =  self.cursor.fetchall()
        columns = [desc[0] for desc in self.cursor.description]
        table = tabulate(hasil, headers=columns, tablefmt="pretty")
        print(table)
    


furniture = Furniture()
furniture.connect()

def main():
    while True:
        print("========================")
        print("=====CRUD FURNITURE=====")
        print("========================\n")
        print("Menu")
        print('1. Tambah Barang')
        print('2. Edit Barang')
        print('3. Hapus Barang')
        print('4. Lihat Seluruh Barang')
        masuk = input("Masukan Pilihan : ")
        if masuk == '1':
            tambah_barang()
        elif masuk == '2':
            edit()
        elif masuk == '3':
            hapus_barang()
        elif masuk =='4':
            furniture.lihat()
            main()
        else:
            pass

def tambah_barang():
    nama_barang = input("Nama Barang : ")
    harga = int(input("Harga Barang : "))
    jumlah_stok = int(input("Jumlah Stok : "))
    data = {
        'nama_barang' : nama_barang,
        'harga' : harga,
        'jumlah_stok' : jumlah_stok
    }
    furniture.insert(data)
    while True:
        pilih = input("input barang lagi? (y/n) : ")
        if pilih == 'y':
            tambah_barang()
        elif pilih == 'n':
            main()
        else:
            continue
def edit():
    id = int(input("masukan id barang : "))
    print('Pilih Menut Edit')
    print("1. Edit Nama Barang")
    print("2. Edit Harga Barang")
    print("3. Edit Jumlah stok")
    print("4. Edit Seluruh Informasi Barang")
    pilih = input("masukan pilihan : ")
    if pilih == '1':
        edit_nama(id)
    elif pilih == '2':
        edit_harga(id)
    elif pilih == '3':
        edit_jumstok(id)
    elif pilih == '4':
        edit_seluruh(id)
    else:
        print('inputan tidak valid silahkan menginput sesuai dengan nomer yang tertera.')
        edit()
    while True:
        pilih = input("edit barang lagi? (y/n) : ")
        if pilih == 'y':
            edit()
        elif pilih == 'n':
            main()
        else:
            continue


def edit_nama(id):
    nama = input('Masukan Nama Barang Terbaru : ')
    data = {
        'nama_barang' : nama
    }
    furniture.update(id,data)

def edit_harga(id):
    harga = input('Masukan Harga Barang Terbaru : ')
    data = {
        'harga' : harga
    }
    furniture.update(id,data)

def edit_jumstok(id):
    jumstok = input('Masukan Jumlah Stok Terbaru : ')
    data = {
        'jumlah_stok' : jumstok
    }
    furniture.update(id,data)

def edit_seluruh(id):
    nama = input('Masukan Nama Barang Terbaru : ')
    harga = input('Masukan Harga Barang Terbaru : ')
    jumstok = input('Masukan Jumlah Stok Terbaru : ')
    data = {
        'nama_barang' : nama,
        'harga' : harga,
        'jumlah_stok' : jumstok
    }
    furniture.update(id,data)

def hapus_barang():
    id = int(input("masukan id barang : "))
    furniture.delete(id)
    while True:
        pilih = input("hapus barang lagi? (y/n) : ")
        if pilih == 'y':
            hapus_barang()
        elif pilih == 'n':
            main()
        else:
            continue

main()