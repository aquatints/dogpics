sudo mkdir /dogpics/
sudo mkdir /dogpics/web/
sudo mkdir /dogpics/backend/

pip3 install flask
pip3 install pyimgur
pip3 install watson-developer-cloud

cd /dogpics/web/
sudo git clone https://github.com/aquatints/dogpics
cd dogpics
sudo git checkout dogpics-web

cd /dogpics/backend
sudo mkdir dogs
sudo mkdir notdogs
sudo mkdir discard
sudo mkdir limbo
sudo git clone https://github.com/aquatints/dogpics
cd dogpics
sudo git checkout backend

cd /dogpics/

sudo wget https://raw.githubusercontent.com/aquatints/dogpics/notes/bootscript.sh
sudo chmod +x bootscript.sh
sudo ./bootscript.sh
