from os import name
from typing import Any
import wx
from wx.core import Frame, NullGraphicsMatrix
import project
import sqlite3
import time

class DialogDaftar(project.daftarDialog):
    def __init__(self, parent):
        project.daftarDialog.__init__(self, parent)

    def btnSimpanOnButtonClick( self, event ):
        # get value variabel
        username = self.textDaftarName.GetValue()
        password = self.textDaftarPass.GetValue()
        konfrmPass = self.textDaftarKonfirm.GetValue()
        nama = self.textDaftarNama.GetValue()
        alamat = self.textDaftarAlamat.GetValue()
        nomerHP = self.textDaftarNomer.GetValue()
        tahun = self.textDaftarTahun.GetValue()

        # verifikasi data pengguna
        if username == "" or password == "" or konfrmPass == "" or nama == "" or alamat == "" or nomerHP == "" or tahun == "":
            wx.MessageBox('Maaf!! Data Tidak Boleh Kosong', 'Informasi', wx.OK | wx.ICON_EXCLAMATION)
        elif not nomerHP.isdecimal():
            wx.MessageBox('Maaf!! data nomer HP harus berupa angka')
        elif not tahun.isdecimal():
            wx.MessageBox('Maaf!! data tahun lahir harus berupa angka')
        else:
            box = wx.MessageDialog(None, 'Apakah data Anda sudah benar?', 'Informasi', wx.YES_NO | wx.ICON_QUESTION)
            kode = box.ShowModal()
            if kode != 5104:
                wx.MessageBox('Berhasil Disimpan', 'Informasi', wx.OK | wx.ICON_INFORMATION)
        
        

    def daftarDialogOnClose( self, event ):
    	self.Destroy()

class MainHome(project.MenuUtama):
    def __init__(self, parent):
        project.homeFrame.__init__(self, parent)

    def btnDaftarOnButtonClick( self, event ):
        dialog = DialogDaftar(parent=None)
        dialog.ShowModal()

    def homeFrameOnClose( self, event ):
    	self.Destroy()

class formProfilPelanggan (project.ProfilPelanggan):
    def __init__(self, parent, username):
        super().__init__(parent)
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data = cursor.execute("select * from Pelanggan where Username=?", (username,)).fetchone()
        saldo = cursor.execute("select * from SaldoPelanggan where Username=?", (username,)).fetchone()
        conn.close()
        self.nama.SetLabel(f"Nama : {data[0]}")
        self.username.SetLabel(f"Username : {data[1]}")
        self.alamat.SetLabel(f"Alamat : {data[2]}")
        self.nomorHp.SetLabel(f"Nomor Hp : {data[3]}")
        self.tahunLahir.SetLabel(f"Tahun Lahir : {data[4]}")
        self.JumlahUang.SetLabel(f"Jumlah Uang : {saldo[1]}")
        self.JumlahHutang.SetLabel(f"Jumlah Hutang : {saldo[2]}")

class formTabelPelanggan(project.LihatPelanggan):
    def __init__(self, parent):
        super().__init__(parent)
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data = cursor.execute("select Nama, Pelanggan.Username, alamat, NomorHp, tahunLahir, JumlahUang, JumlahHutang from Pelanggan join SaldoPelanggan where Pelanggan.username = SaldoPelanggan.username").fetchall()
        conn.close()
        namaKolom = ('Nama', 'Username', 'Alamat', 'Nomor Hp', 'Tahun Lahir', 'Jumlah Uang', 'Jumlah Hutang')
        for baris in range(len(data)):
            self.Tabel.AppendRows()
            for kolom in range(len(data[baris])):
                self.Tabel.SetColLabelValue(kolom, namaKolom[kolom])
<<<<<<< HEAD
                self.Tabel.SetCellValue(baris, kolom, str(data[baris][kolom]))        
=======
                self.Tabel.SetCellValue(baris, kolom, str(data[baris][kolom]))    
<<<<<<< Updated upstream
>>>>>>> parent of 71647af (update)
        
# class lihatSaldo (project.LihatSaldo):
#     def __init__(self, parent):
#         super().__init__(parent)
#         conn = sqlite3.connect('project.sqlite')
#         cursor = conn.cursor()
#         hasil = cursor.execute("select jumlahUang from SaldoPelanggan where noID = ?", (str(self.__nomorid),)).fetchone()[0]
#         conn.close()
#         self.m_staticText42.SetValue(str(hasil))

# class tambahTabungan(project.TambahTabungan):
#     def __init__(self, parent):
#         super().__init__(parent)
#         uangMasuk = self.m_textCtrl21.GetValue()
#         jumlahSaldoTabungan = self.__jumlahSaldo + uangMasuk
#         self.__jumlahSaldo = jumlahSaldoTabungan
#         conn = sqlite3.connect('project.sqlite')
#         cursor = conn.cursor()
#         cursor.execute("update SaldoPelanggan set jumlahUang = ? where noID = ? ", (jumlahSaldoTabungan, self.__nomorid,))
#         conn.commit()
#         conn.close() 

class tarik(project.Tarik):
    def __init__(self, parent):
        super().__init__(parent)
    
<<<<<<< HEAD
    def saldoTarik(self, event):
        uangTarik = self.m_textCtrl21.GetValue()
        if self.__jumlahSaldo < uangTarik:
            wx.MessageBox('Maaf saldo tidak mencukupi', wx.OK | wx.ICON_ERROR)
=======
    def btnTarikOnButtonClick( self, event ):
        uangTarik = self.textJumlahTarik.GetValue()
        username = self.textUsernameTarik.GetValue()
        nilai = " "

        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        current = cursor.execute("select saldo from SaldoPelanggan where Username = ?", (username,)).fetchone()[0]
        conn.close()

        if uangTarik.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_ERROR)

>>>>>>> parent of 71647af (update)
        else:
            jumlahSaldoTarik = self.__jumlahSaldo - uangTarik
            self.__jumlahSaldo = jumlahSaldoTarik
            conn = sqlite3.connect('project.sqlite')
            cursor = conn.cursor()
            cursor.execute("update SaldoPelanggan set jumlahUang = ? where noID = ? ", (self.__jumlahSaldo, self.__nomorid,))
            conn.commit()
            conn.close()
            wx.MessageBox('Sisa saldo anda',self.__jumlahSaldo, wx.OK | wx.ICON_ERROR)


class TambahNabung (project.TambahTabungan):
    def __init__(self, parent):
        project.TambahTabungan.__init__(self, parent)

    def btn_OK_tambahTabungan( self, event ):
        jumlah = self.inputTabungan.GetValue()
        username = self.inputUsername.GetValue()
        event.Skip()
        if jumlah.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_ERROR)
            
        else:
            box = wx.MessageDialog(None, 'Apakah data sudah benar', 'Informasi', wx.YES_NO | wx.ICON_QUESTION)
            kodedlg = box.ShowModal()
            print(kodedlg)
            if kodedlg != 5104:
                waktu = time.ctime()
                current = str(LihatSaldo(parent=None).btn_LihatSaldo(event=None))
                jumlah_Saldo = int(current) + int(jumlah)
                conn = sqlite3.connect('project.sqlite')
                cursor = conn.cursor()
                query = "INSERT INTO Transaksi(username,tambahUang,waktu) VALUES (?,?,?)"
                cursor.execute(query, (username, jumlah, waktu))
                query = cursor.execute("update SaldoPelanggan set saldo = ? where Username = ? ", (jumlah_Saldo, username,))
                cursor.execute(query)
                conn.commit()
                conn.close()
                self.Destroy()
        
class LihatSaldo(project.LihatSaldo):
    def __init__(self, parent):
        project.LihatSaldo.__init__(self, parent)
        # self.saldoSekarang = self.btn_LihatSaldo(event=None)
    
    def btn_LihatSaldo( self, event ):
        nama = self.inputNama.GetValue()
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        hasil = cursor.execute("select saldo from SaldoPelanggan where Username = ?", (nama,)).fetchone()[0]
        conn.close()
        self.saldo.SetValue(str(hasil))
        return hasil

class PinjamTabungan(project.Pinjam):
    def __init__(self, parent):
        super().__init__(parent)

<<<<<<< HEAD
=======
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    def m_button18OnButtonClick( self, event ):
        uangPinjam = int(self.m_textCtrl21.GetValue())
        hari = int(self.m_textCtrl19.GetValue())
        bulan = hari / 30
        bungaPinjam = bulan / 12 * 5 / 100 * uangPinjam
        piutang = uangPinjam + bungaPinjam
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        self.__jumlahHutang = cursor.execute("Select Hutang from SaldoPelanggan where username=?",(self.username,)).fetchone()[0]
        self.__jumlahHutang += piutang
        cursor.execute("update SaldoPelanggan set Hutang = ? where username = ? ", (self.__jumlahHutang, self.username,))
=======
>>>>>>> parent of 71647af (update)
    def btn_OK_pinjamTabungan( self, event):
        nama = self.inputNama.GetValue()
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        jumlahUang = cursor.execute("select jumlahUang from SaldoPelanggan where Username = ?", (nama,)).fetchone()[0]
        conn.close()
        uangPinjam = int(self.m_textCtrl21.GetValue())
        hari = int(self.m_textCtrl23.GetValue())
        bulan = hari / 30
        bungaPinjam = bulan / 12 * 5 / 100 * uangPinjam
        piutang = uangPinjam + bungaPinjam
        jumlahSaldo = jumlahUang + uangPinjam 
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        cursor.execute("update SaldoPelanggan set jumlahHutang = ? ,jumlahUang = ? where Username = ? ", (piutang, jumlahSaldo, nama))
        conn.commit()
        conn.close()
<<<<<<< HEAD
        self.m_textCtrl22.SetValue(str(piutang))

app = wx.App()
# frame = TambahNabung(parent=None)
=======
        wx.MessageBox('Berhasil Bos', 'Informasi', wx.OK | wx.ICON_INFORMATION)
        self.Close()  

class BayarUtang(project.BayarHutang):
     def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data1 = cursor.execute("select Saldo, Hutang from SaldoPelanggan where username = ? ", (self.username,)).fetchone()
        conn.close()
        self.__jumlahSaldo = data1[0]
        self.__jumlahHutang = data1[1]
        if self.__jumlahSaldo < self.__jumlahHutang:
            self.keterangan.SetLabel("maaf saldo Anda kurang untuk membayar utang")
        else:
            self.__jumlahSaldo -= self.__jumlahHutang
            conn = sqlite3.connect('project.sqlite')
            cursor = conn.cursor()
            cursor.execute("update SaldoPelanggan set Hutang = 0 , Saldo = ? where username = ? ", (self.__jumlahSaldo, self.username,))
            conn.commit()
            conn.close()
            self.keterangan.SetLabel("Sudah Terbayar")


=======
    def btnPinjamOnButtonClick( self, event ):
        uangPinjam = self.jumlahPinjam.GetValue()
        username = self.usernamePinjam.GetValue()
        nilai = " "

        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        current = cursor.execute("select Hutang from SaldoPelanggan where Username = ?", (username,)).fetchone()[0]
        conn.close()

        if uangPinjam.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_ERROR)

        else:
            jumlahPinjam = int(current) + int(uangPinjam)
            waktu = time.ctime()

            conn = sqlite3.connect('project.sqlite')
            cursor = conn.cursor()
            query = "INSERT INTO Transaksi(username,tambahUang,tarikUang,utang,waktu) VALUES (?,?,?,?,?)"
            cursor.execute(query, (username, nilai, nilai, uangPinjam, waktu))

            cursor.execute("update SaldoPelanggan set Hutang = ? where Username = ? ", (jumlahPinjam, username,))
            conn.commit()
            conn.close()
            wx.MessageBox('Hutang anda saat ini {}'.format(str(jumlahPinjam)),'Informasi Saldo', wx.OK | wx.ICON_INFORMATION)
>>>>>>> Stashed changes

class BayarUtang(project.BayarHutang):
     def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data1 = cursor.execute("select Saldo, Hutang from SaldoPelanggan where username = ? ", (self.username,)).fetchone()
        conn.close()
        self.__jumlahSaldo = data1[0]
        self.__jumlahHutang = data1[1]
        if self.__jumlahSaldo < self.__jumlahHutang:
            self.keterangan.SetLabel("maaf saldo Anda kurang untuk membayar utang")
        else:
            self.__jumlahSaldo -= self.__jumlahHutang
            conn = sqlite3.connect('project.sqlite')
            cursor = conn.cursor()
            cursor.execute("update SaldoPelanggan set Hutang = 0 , Saldo = ? where username = ? ", (self.__jumlahSaldo, self.username,))
            conn.commit()
            conn.close()
            self.keterangan.SetLabel("Sudah Terbayar")



app = wx.App()
# frame = BayarUtang(None, "felynir")
<<<<<<< Updated upstream
<<<<<<< HEAD
# frame = MenuKaryawan(None, "justin")
# frame = TambahNabung(None,"felynir")
# frame = PinjamTabungan(None, "felynir")
frame = Tarik(None,"felynir")
=======
frame = MenuKaryawan(None, "justin")
>>>>>>> e79e41b0029b3e77f7f78a2d676a1dac1a62d695
# frame = TambahNabung(parent=None)
=======
# frame = MenuKaryawan(None, "justin")
>>>>>>> Stashed changes
>>>>>>> parent of 71647af (update)
# frame = formProfilPelanggan(None, "felynir")
# frame = LihatSaldo(parent=None)
frame = PinjamTabungan (parent=None)
frame.Show()
app.MainLoop()