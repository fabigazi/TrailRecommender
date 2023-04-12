# make commands for Mac OS
trails:
	source setup/.gitignore/venv/bin/activate
	Python3 trail_recommend.py	
	deactivate

requirements:
	# go into setup directory and create git ignore folder
	cd setup
	mkdir -p .gitignore	
	cd .gitignore
	python3 -m venv venv
	. venv/bin/activate
	pip3 install --upgrade pip
	pip3 install -r setup/requirements.txt
	deactivate

teardown:
	rm -r setup/.gitignore/venv