- Ubuntu 16.04.4 LTS
- Python 3
	- `pip3 install watson-cloud-developer`
	- `pip3 install pyimgur`
	- `pip3 install Flask`

```bash
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

```
