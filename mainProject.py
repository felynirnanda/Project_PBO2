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

class MenuKaryawan(project.MenuKaryawan):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username

    def klikLihatPelanggan(self, event):
        lhtPelanggan = formTabelPelanggan(self)
        lhtPelanggan.Show()
        
    def klikLihatProfilKaryawan(self, event):
        lhtProfilKaryawan = formProfilKaryawan(self, self.username)
        lhtProfilKaryawan.Show()

class MenuPelanggan(project.MenuPelanggan):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username

    def btnLihatProfilPelanggan(self, event):
        lhtProfilPelanggan = formProfilPelanggan()
        lhtProfilPelanggan.Show()

    def btnBayarHutang(self, event):
        bayarHutang = BayarUtang(self, self.username)
        bayarHutang.Show()

    def btnTambah(self, event):
        tambahTabungan = TambahNabung()
        tambahTabungan.Show()

    def btnPinjam(self, event):
        pinjam = PinjamTabungan()
        pinjam.Show()

    def btnTarik(self, event):
        tarikUang = tarik()
        tarikUang.Show()

    def btnLihatSaldo(self, event):
        lhtSaldo = LihatSaldo()
        lhtSaldo.Show()

    # def btnKeluar(self, event):
    #     menuUtama = 

class formProfilKaryawan (project.ProfilKaryawan):
    def __init__(self, parent, username):
        super().__init__(parent)
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        kry = cursor.execute("select * from Karyawan where Username=?", (username,)).fetchone()
        conn.close()
        self.username.SetLabel(f"Username : {kry[0]}")
        self.nama.SetLabel(f"Nama : {kry[3]}")
        self.alamat.SetLabel(f"Alamat : {kry[4]}")
        self.nomorHp.SetLabel(f"Nomor Hp : {kry[5]}")
        self.tahunLahir.SetLabel(f"Tahun Lahir : {kry[6]}")

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
        data = cursor.execute("select Nama, Pelanggan.Username, alamat, NomorHp, tahunLahir, Saldo, Hutang from Pelanggan join SaldoPelanggan where Pelanggan.username = SaldoPelanggan.username").fetchall()
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
    
    def saldoTarik(self, event):
        uangTarik = self.m_textCtrl21.GetValue()
        if self.__jumlahSaldo < uangTarik:
            wx.MessageBox('Maaf saldo tidak mencukupi', wx.OK | wx.ICON_ERROR)
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
                query = cursor.execute("INSERT INTO Transaksi(username,tambahUang,waktu) VALUES (?,?,?)", (username, jumlah, waktu,))
                cursor.execute(query)
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

    def btn_OK_pinjamTabungan( self, event ):
        uangPinjam = self.m_textCtrl21.GetValue()
        hari = float(self.m_textCtrl23.GetValue())
        bulan = hari / 30
        bungaPinjam = bulan / 12 * 5 / 100 * uangPinjam
        piutang = uangPinjam + bungaPinjam
        self.__jumlahHutang += piutang
        jumlahSaldo = self.__jumlahSaldo + uangPinjam 
        self.__jumlahSaldo = jumlahSaldo
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        cursor.execute("update SaldoPelanggan set jumlahHutang = ? ,jumlahUang = ? where noID = ? ", (self.__jumlahHutang, self.__jumlahSaldo, self.__nomorid,))
        conn.commit()
        conn.close()
        self.m_textCtrl22.SetValue(str(piutang))

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

     def bayar(self, event) :
        if self.__jumlahSaldo < self.__jumlahHutang:
            self.keterangan.SetLabel("maaf saldo Anda kurang untuk membayar utang")
        else:
            Saldo = self.__jumlahSaldo - piutang 
            self.__jumlahSaldo = jumlahSaldo
            conn = sqlite3.connect('project.sqlite')
            cursor = conn.cursor()
            cursor.execute("update SaldoPelanggan set Hutang = 0 ,Uang = ? where username = ? ", (self.__jumlahSaldo, self.__username,))
            conn.commit()
            conn.close()
            self.keterangan.SetLabel("Sudah Terbayar")



app = wx.App()
# frame = BayarUtang(None, "felynir")
# frame = MenuKaryawan(None, "justin")
# frame = TambahNabung(parent=None)
# frame = formProfilPelanggan(None, "felynir")
# frame = LihatSaldo(parent=None)
# frame = PinjamTabungan (parent=None)
frame = MenuPelanggan(None, "felynir")
frame.Show()
app.MainLoop()