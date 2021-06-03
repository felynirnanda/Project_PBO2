import wx
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
                self.Tabel.SetCellValue(baris, kolom, str(data[baris][kolom]))

            
        
class lihatSaldo (project.LihatSaldo):
    def __init__(self, parent):
        super().__init__(parent)
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        hasil = cursor.execute("select jumlahUang from SaldoPelanggan where noID = ?", (str(self.__nomorid),)).fetchone()[0]
        conn.close()
        self.m_staticText42.SetValue(str(hasil))
        
    
class TambahNabung (project.TambahTabungan):
    def __init__(self, parent):
        project.TambahTabungan.__init__(self, parent)

    def btn_OK_tambahTabungan( self, event ):
        jumlah = self.inputTabungan.GetValue()
        event.Skip()
        if jumlah.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_INFORMATION)
            
        else:
            box = wx.MessageDialog(None, 'Apakah data sudah benar', 'Informasi', wx.YES_NO | wx.ICON_QUESTION)
            kodedlg = box.ShowModal()
            print(kodedlg)
            if kodedlg != 5104:
                username = self.inputUsername.GetValue()
                waktu = time.ctime()
                conn = sqlite3.connect('project.sqlite')
                cursor = conn.cursor()
                query = "INSERT INTO Transaksi(username,jumlah,waktu) VALUES (?,?,?)"
                cursor.execute(query, (username, jumlah, waktu))
                conn.commit()
                conn.close()
                self.Destroy()


app = wx.App()
# frame = MainHome(parent=None)
# frame = formProfilPelanggan(None, "felynir")
frame = TambahNabung(parent=None)
frame.Show()
app.MainLoop()