# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['FrameScan-GUI.py'],
             pathex=['D:\\code\\Python37\\obj\\FrameScan-GUI','D:\\code\\Python37\\obj\\FrameScan-GUI\\Modules'],
             binaries=[],
             datas=[],
             hiddenimports=['bs4','uuid','Crypto.Cipher.AES','xml.etree','xml.etree.ElementTree','eventlet.hubs.epolls', 'eventlet.hubs.kqueue','eventlet.hubs.selects', 'dns','dns.asyncresolver','dns.versioned', 'dns.dnssec', 'dns.asyncquery','dns.asyncbackend','dns.e164', 'dns.hash', 'dns.namedict', 'dns.tsigkeyring', 'dns.update', 'dns.version', 'dns.zone'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='FrameScan-GUI',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,icon='Conf/main.ico')
