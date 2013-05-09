# -*- mode: python -*-

path = 'z:\\projects\\Client\\'

a = Analysis([path + 'main.py'],
			# pathex=[path + 'pyinstaller'],
			hiddenimports=[],
			hookspath=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
	a.scripts,
	a.binaries + 
		[('icudt.dll', path + 'icudt.dll', 'BINARY')] +
		[('locales\\en-US.pak', path + 'locales\\en-US.pak', 'DATA')] + 
		[('icon.ico', path + 'icon.ico',  'BINARY')],
	a.zipfiles,
	a.datas,
	name=os.path.join('dist', 'd3up.exe'),
	debug=False,
	strip=None,
	console=False, 
	icon=path + 'icon.ico' 
)
app = BUNDLE(exe,
	name=os.path.join('dist', 'd3up.exe.app'))