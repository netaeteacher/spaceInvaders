import cx_Freeze

OPTIONS = {"build_exe": {"packages": ["pygame"],
                         "include_files": ["img", "sounds", "Bullet.py", "Explosion.py",
                                           "main.py", "Meteor.py", "Player.py", "ShieldBar.py",
                                           "spaceInvadersGUI.py", "TekkiePygameLib.py"]}}

EXECUTABLES = [cx_Freeze.Executable("main.py", icon="img/spaceShip3.ico", targetName="Space Invaders - Ido Pony",
                                    base="win32GUI")]

cx_Freeze.setup(
    options=OPTIONS,
    executables=EXECUTABLES
)
