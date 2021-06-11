# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class daftarDialog
###########################################################################

class daftarDialog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Daftar Pelanggan", pos = wx.DefaultPosition, size = wx.Size( 358,382 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		fgSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.textDaftarName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textDaftarName, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		fgSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.textDaftarPass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.textDaftarPass, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Konfirmasi Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		fgSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.textDaftarKonfirm = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer4.Add( self.textDaftarKonfirm, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Nama", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer4.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.textDaftarNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textDaftarNama, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Alamat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		fgSizer4.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.textDaftarAlamat = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textDaftarAlamat, 0, wx.ALL, 5 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Nomer HP", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		fgSizer4.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.textDaftarNomer = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textDaftarNomer, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Tahun Lahir", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		fgSizer4.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.textDaftarTahun = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.textDaftarTahun, 0, wx.ALL, 5 )

		self.btnSimpan = wx.Button( self, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSimpan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.btnSimpan.SetBackgroundColour( wx.Colour( 217, 203, 38 ) )

		fgSizer4.Add( self.btnSimpan, 0, 0, 5 )


		self.SetSizer( fgSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.daftarDialogOnClose )
		self.btnSimpan.Bind( wx.EVT_BUTTON, self.btnSimpanOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def daftarDialogOnClose( self, event ):
		event.Skip()

	def btnSimpanOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class LoginKaryawan
###########################################################################

class LoginKaryawan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Karyawan", pos = wx.DefaultPosition, size = wx.Size( 288,183 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.textMasukName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textMasukName, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.textMasukPass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textMasukPass, 0, wx.ALL, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetBackgroundColour( wx.Colour( 217, 203, 38 ) )

		fgSizer5.Add( self.btnLogin, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LoginPelanggan
###########################################################################

class LoginPelanggan ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Login Pelanggan", pos = wx.DefaultPosition, size = wx.Size( 288,183 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOBK ) )

		fgSizer5 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		fgSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.textMasukName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textMasukName, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		fgSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.textMasukPass = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer5.Add( self.textMasukPass, 0, wx.ALL, 5 )

		self.btnLogin = wx.Button( self, wx.ID_ANY, u"Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnLogin.SetBackgroundColour( wx.Colour( 217, 203, 38 ) )

		fgSizer5.Add( self.btnLogin, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MenuUtama
###########################################################################

class MenuUtama ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Utama", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText20 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang. Silahkan pilih :\n1. Daftar Pelanggan\n2. Login Pelanggan\n3. Login Karyawan\n4. Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer5.Add( self.m_staticText20, 0, wx.ALIGN_CENTER, 5 )

		self.m_textCtrl14 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_textCtrl14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button8 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.m_button8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MenuPelanggan
###########################################################################

class MenuPelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Pelanggan", pos = wx.DefaultPosition, size = wx.Size( 500,295 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang\nSilahkan pilih fitur :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer9.Add( self.m_staticText24, 0, wx.ALIGN_CENTER, 5 )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"Lihat Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self, wx.ID_ANY, u"Bayar Hutang", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"Tambah Tabungan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self, wx.ID_ANY, u"Pinjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button21, 0, wx.ALL, 5 )

		self.m_button22 = wx.Button( self, wx.ID_ANY, u"Tarik Uang", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button22, 0, wx.ALL, 5 )

		self.m_button23 = wx.Button( self, wx.ID_ANY, u"Lihat Saldo", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button23, 0, wx.ALL, 5 )

		self.m_button24 = wx.Button( self, wx.ID_ANY, u"Keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button24, 0, wx.ALL, 5 )


		bSizer9.Add( gSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.btnLihatProfilPelanggan )
		self.m_button19.Bind( wx.EVT_BUTTON, self.btnBayarHutang )
		self.m_button20.Bind( wx.EVT_BUTTON, self.btnTambah )
		self.m_button21.Bind( wx.EVT_BUTTON, self.btnPinjam )
		self.m_button22.Bind( wx.EVT_BUTTON, self.btnTarik )
		self.m_button23.Bind( wx.EVT_BUTTON, self.btnLihatSaldo )
		self.m_button24.Bind( wx.EVT_BUTTON, self.btnKeluar )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btnLihatProfilPelanggan( self, event ):
		event.Skip()

	def btnBayarHutang( self, event ):
		event.Skip()

	def btnTambah( self, event ):
		event.Skip()

	def btnPinjam( self, event ):
		event.Skip()

	def btnTarik( self, event ):
		event.Skip()

	def btnLihatSaldo( self, event ):
		event.Skip()

	def btnKeluar( self, event ):
		event.Skip()


###########################################################################
## Class BayarHutang
###########################################################################

class BayarHutang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Bayar Hutang", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_HIGHLIGHTTEXT ) )

		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.keterangan = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.keterangan.Wrap( -1 )

		bSizer11.Add( self.keterangan, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer11 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MenuKaryawan
###########################################################################

class MenuKaryawan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Menu Karyawan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Selamat Datang\nSilahkan pilih fitur :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		bSizer9.Add( self.m_staticText24, 0, wx.ALIGN_CENTER, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"Lihat Pelanggan", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button16, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_button17 = wx.Button( self, wx.ID_ANY, u"Lihat Profil", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button17, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer9.Add( gSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.klikLihatPelanggan )
		self.m_button17.Bind( wx.EVT_BUTTON, self.klikLihatProfilKaryawan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def klikLihatPelanggan( self, event ):
		event.Skip()

	def klikLihatProfilKaryawan( self, event ):
		event.Skip()


###########################################################################
## Class ProfilPelanggan
###########################################################################

class ProfilPelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Profil Pelanggan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.nama = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		bSizer12.Add( self.nama, 0, wx.ALL, 5 )

		self.alamat = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.Wrap( -1 )

		bSizer12.Add( self.alamat, 0, wx.ALL, 5 )

		self.nomorHp = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomorHp.Wrap( -1 )

		bSizer12.Add( self.nomorHp, 0, wx.ALL, 5 )

		self.username = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		bSizer12.Add( self.username, 0, wx.ALL, 5 )

		self.tahunLahir = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tahunLahir.Wrap( -1 )

		bSizer12.Add( self.tahunLahir, 0, wx.ALL, 5 )

		self.JumlahUang = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.JumlahUang.Wrap( -1 )

		bSizer12.Add( self.JumlahUang, 0, wx.ALL, 5 )

		self.JumlahHutang = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.JumlahHutang.Wrap( -1 )

		bSizer12.Add( self.JumlahHutang, 0, wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class ProfilKaryawan
###########################################################################

class ProfilKaryawan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Profil Karyawan", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.nama = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nama.Wrap( -1 )

		bSizer12.Add( self.nama, 0, wx.ALL, 5 )

		self.alamat = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.alamat.Wrap( -1 )

		bSizer12.Add( self.alamat, 0, wx.ALL, 5 )

		self.nomorHp = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.nomorHp.Wrap( -1 )

		bSizer12.Add( self.nomorHp, 0, wx.ALL, 5 )

		self.username = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.username.Wrap( -1 )

		bSizer12.Add( self.username, 0, wx.ALL, 5 )

		self.tahunLahir = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.tahunLahir.Wrap( -1 )

		bSizer12.Add( self.tahunLahir, 0, wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LihatPelanggan
###########################################################################

class LihatPelanggan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Pelanggan", pos = wx.DefaultPosition, size = wx.Size( 682,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.Tabel = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.Tabel.CreateGrid( 0, 7 )
		self.Tabel.EnableEditing( True )
		self.Tabel.EnableGridLines( True )
		self.Tabel.EnableDragGridSize( False )
		self.Tabel.SetMargins( 0, 0 )

		# Columns
		self.Tabel.EnableDragColMove( False )
		self.Tabel.EnableDragColSize( True )
		self.Tabel.SetColLabelSize( 30 )
		self.Tabel.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Tabel.EnableDragRowSize( True )
		self.Tabel.SetRowLabelSize( 80 )
		self.Tabel.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.Tabel.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer12.Add( self.Tabel, 0, wx.ALL, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LihatSaldo
###########################################################################

class LihatSaldo ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lihat Saldo", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 217, 220 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Lihat Saldo", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )

		self.m_staticText32.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial" ) )

		bSizer12.Add( self.m_staticText32, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer5.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.inputNama = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.inputNama, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Jumlah Saldo Anda Saat ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )

		gSizer5.Add( self.m_staticText35, 0, wx.ALL, 5 )

		self.saldo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.saldo, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_button15 = wx.Button( self, wx.ID_ANY, u"LIHAT", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button16, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )


		bSizer12.Add( gSizer5, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button15.Bind( wx.EVT_BUTTON, self.btn_LihatSaldo )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_LihatSaldo( self, event ):
		event.Skip()


###########################################################################
## Class TambahTabungan
###########################################################################

class TambahTabungan ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tambah Tabungan ", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 213, 220 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Tambah Tabungan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer13.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText301 = wx.StaticText( self, wx.ID_ANY, u"username ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText301.Wrap( -1 )

		gSizer3.Add( self.m_staticText301, 0, wx.ALL, 5 )

		self.inputUsername = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.inputUsername, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Masukan jumlah uang yang ingin Anda tabung : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.inputTabungan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.inputTabungan, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( gSizer3, 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button18.Bind( wx.EVT_BUTTON, self.btn_OK_tambahTabungan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def btn_OK_tambahTabungan( self, event ):
		event.Skip()


###########################################################################
## Class Pinjam
###########################################################################

class Pinjam ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pinjam", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 213, 220 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Pinjam", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer13.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Masukan jumlah uang yang ingin Anda pinjam :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( gSizer3, 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class Tarik
###########################################################################

class Tarik ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tarik ", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 190, 213, 220 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Tarik Uang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		self.m_staticText30.SetFont( wx.Font( 10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer13.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Masukan jumlah uang yang ingin Anda ambil :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )

		gSizer3.Add( self.m_staticText31, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_textCtrl21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer13.Add( gSizer3, 0, wx.EXPAND, 5 )

		self.m_button18 = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


