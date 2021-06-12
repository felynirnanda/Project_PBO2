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
        lhtProfilPelanggan = formProfilPelanggan(self, self.username)
        lhtProfilPelanggan.Show()

    def btnBayarHutang(self, event):
        bayarHutang = BayarUtang(self, self.username)
        bayarHutang.Show()

    def btnTambah(self, event):
        tambahTabungan = TambahNabung(self, self.username)
        tambahTabungan.Show()

    def btnPinjam(self, event):
        pinjam = PinjamTabungan(self, self.username)
        pinjam.Show()

    def btnTarik(self, event):
        tarikUang = Tarik(self, self.username)
        tarikUang.Show()

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
        self.nama.SetLabel(f"Nama : {data[3]}")
        self.username.SetLabel(f"Username : {data[0]}")
        self.alamat.SetLabel(f"Alamat : {data[4]}")
        self.nomorHp.SetLabel(f"Nomor Hp : {data[5]}")
        self.tahunLahir.SetLabel(f"Tahun Lahir : {data[6]}")
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

class tarik(project.Tarik):
    def __init__(self, parent):
        super().__init__(parent)
    
    def btnTarikOnButtonClick( self, event ):
        uangTarik = self.textJumlahTarik.GetValue()
        username = self.textUsernameTarik.GetValue()
        nilai = " "

        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        current = cursor.execute("select saldo from SaldoPelanggan where Username = ?", (username,)).fetchone()[0]
        conn.close()
        self.m_staticText42.SetValue(str(hasil))


class Tarik(project.Tarik):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username

    def m_button18OnButtonClick(self, event):
        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data2 = cursor.execute("select Saldo from SaldoPelanggan where username = ? ", (self.username,)).fetchone()
        self.__jumlahSaldo = data2[0]
        tambahan = self.menarik.GetValue()
        self.__jumlahSaldo -= int(float(tambahan))
        cursor.execute("update SaldoPelanggan set Saldo=? where username = ?", (self.__jumlahSaldo, self.username,))
        conn.commit()
        conn.close()
        wx.MessageBox('Berhasil Bos', 'Informasi', wx.OK | wx.ICON_INFORMATION)
        self.Close()    


        if uangTarik.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_ERROR)

        else:
            if int(current) < int(uangTarik):
                wx.MessageBox('Maaf saldo tidak mencukupi','Informasi', wx.OK | wx.ICON_ERROR)
            else:
                jumlahSaldoTarik = int(current) - int(uangTarik)
                waktu = time.ctime()

                conn = sqlite3.connect('project.sqlite')
                cursor = conn.cursor()
                query = "INSERT INTO Transaksi(username,tambahUang,tarikUang,utang,waktu) VALUES (?,?,?,?,?)"
                cursor.execute(query, (username, nilai, uangTarik, nilai, waktu))

                cursor.execute("update SaldoPelanggan set Saldo = ? where Username = ? ", (jumlahSaldoTarik, username,))
                conn.commit()
                conn.close()
                wx.MessageBox('Sisa saldo anda {}'.format(str(jumlahSaldoTarik)),'Informasi Saldo', wx.OK | wx.ICON_INFORMATION)



class TambahNabung (project.TambahTabungan):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username

    def btn_OK_tambahTabungan( self, event ):
        jumlah = self.inputTabungan.GetValue()
        username = self.inputUsername.GetValue()
        nilai = " "
        event.Skip()

        if jumlah.isdecimal() == False:
            wx.MessageBox('Maaf harus berupa angka saja', 'Informasi', wx.OK | wx.ICON_ERROR)
            
        else:
            box = wx.MessageDialog(None, 'Apakah data sudah benar', 'Informasi', wx.YES_NO | wx.ICON_QUESTION)
            kodedlg = box.ShowModal()
            print(kodedlg)
            if kodedlg != 5104:
                conn = sqlite3.connect('project.sqlite')
                cursor = conn.cursor()
                current = cursor.execute("select saldo from SaldoPelanggan where Username = ?", (username,)).fetchone()[0]
                conn.close()

                waktu = time.ctime()
                jumlah_Saldo = int(current) + int(jumlah)

                conn = sqlite3.connect('project.sqlite')
                cursor = conn.cursor()
                query = "INSERT INTO Transaksi(username,tambahUang,tarikUang,utang,waktu) VALUES (?,?,?,?,?);"
                cursor.execute(query, (username, jumlah, nilai, nilai, waktu))
                query = cursor.execute("update SaldoPelanggan set saldo = ? where Username = ? ", (jumlah_Saldo, username,))
                conn.commit()
                conn.close()
                wx.MessageBox('Saldo anda saat ini {}'.format(str(jumlah_Saldo)),'Informasi Saldo', wx.OK | wx.ICON_INFORMATION)
        
class LihatSaldo(project.LihatSaldo):
    def __init__(self, parent):
        project.LihatSaldo.__init__(self, parent)
    
    def btn_LihatSaldo( self, event ):
        nama = self.inputNama.GetValue()

        conn = sqlite3.connect('project.sqlite')
        cursor = conn.cursor()
        data2 = cursor.execute("select Saldo from SaldoPelanggan where username = ? ", (self.username,)).fetchone()
        self.__jumlahSaldo = data2[0]
        tambahan = self.inputTabungan.GetValue()
        self.__jumlahSaldo += int(float(tambahan))
        cursor.execute("update SaldoPelanggan set Saldo=? where username = ?", (self.__jumlahSaldo, self.username,))
        conn.commit()
        conn.close()
        wx.MessageBox('Berhasil Bos', 'Informasi', wx.OK | wx.ICON_INFORMATION)
        self.Close()    

class PinjamTabungan(project.Pinjam):
    def __init__(self, parent, username):
        super().__init__(parent)
        self.username = username


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
        conn.commit()
        conn.close()
        wx.MessageBox('Berhasil Bos', 'Informasi', wx.OK | wx.ICON_INFORMATION)
        self.Close()  

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
# frame = MenuKaryawan(None, "justin")
# frame = MenuPelanggan(None, "felynir")
# frame = TambahNabung(None,"felynir")
# frame = PinjamTabungan(None, "felynir")
# frame = Tarik(None,"felynir")
# frame = TambahNabung(parent=None)
# frame = formProfilPelanggan(None, "felynir")
# frame = MenuPelanggan(None, "felynir")
# frame = LihatSaldo(parent=None)
frame = TambahNabung(parent=None)
# frame = tarik(parent=None)
# frame = PinjamTabungan(parent=None)
frame.Show()
app.MainLoop()