sudo mkdir /dogpics/
sudo mkdir /dogpics/web/
sudo mkdir /dogpics/backend/

cd /dogpics/web/
sudo git clone https://github.com/aquatints/dogpics
cd dogpics
sudo git checkout dogpics-web

cd /dogpics/backend
sudo mkdir dogs
sudo mkdir notdogs
sudo mkdir discard
sudo git clone https://github.com/aquatints/dogpics
cd dogpics
sudo git checkout backend

cd /dogpics/

sudo wget https://raw.githubusercontent.com/aquatints/dogpics/notes/bootscript.sh
sudo chmod +x bootscript.sh
sudo ./bootscript.sh