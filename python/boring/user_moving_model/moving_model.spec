# -*- mode: python -*-

block_cipher = None


a = Analysis(['moving_model.py'],
             pathex=['D:\\Project\\python\\boring\\user_moving_model'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='moving_model',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
