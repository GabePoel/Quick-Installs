import shutil
import tarfile
import os
try:
    import wget
except:
    try:
        os.system('pip3 install wget')
        import wget
    except:
        try:
            os.system('sudo apt-get install python3-pip')
            os.system('pip3 install wget')
            import wget
        except:
            try:
                os.system('pacman -S python-pip')
                os.system('pip3 install wget')
                import wget
            except:
                print('Must have pip or the wget package installed.')
                quit()

print('Downloading VESTA')
here = os.getcwd()
download_url = 'https://jp-minerals.org/vesta/archives/3.5.2/VESTA-gtk3.tar.bz2'
home = os.path.expanduser('~')
install_location = os.path.join(home, '.local', 'share', 'VESTA')
if not os.path.exists(install_location):
    os.makedirs(install_location)
install_name = os.path.join(install_location, 'VESTA-gtk3.tar.bz2')
wget.download(download_url, install_name)
print('\nExtracting VESTA')
tar = tarfile.open(install_name, 'r:bz2')
tar.extractall(install_location)
tar.close()
extract_location = os.path.join(install_location, 'VESTA-gtk3')
files = os.listdir(extract_location)
print('Installing VESTA')
for f in files:
    src = os.path.join(extract_location, f)
    shutil.move(src, install_location)
os.remove(install_name)
os.rmdir(extract_location)
src_img_loc = os.path.join(here, 'img')
dst_img_loc = os.path.join(install_location, 'img')
images = os.listdir(src_img_loc)
for img in images:
    src = os.path.join(src_img_loc, img)
    shutil.copy(src, dst_img_loc)
launcher_path = os.path.join(home, '.local', 'share', 'applications', 'vesta.desktop')
launcher = open(launcher_path, 'w')
launcher.write(
    "[Desktop Entry]\n" +
    "Name=VESTA\n" + 
    "Exec=" + os.path.join(home, '.local', 'share', 'VESTA', 'VESTA') + "\n" + 
    "Comment=3D visualization program for structural models, volumetric data such as electron/nuclear densities, and crystal morphologies.\n" +
    "Terminal=false\n" + 
    "Icon=" + os.path.join(home, '.local', 'share', 'VESTA', 'img', 'vesta.svg') + "\n" +
    "Type=Application\n" +
    "Categories=Science; Education;"
)
launcher.close()
