# make commands for Mac OS
trails:
	source setup/.gitignore/venv/bin/activate
	Python3 trail_recommend.py	
	deactivate

requirements:
	cd setup
	mkdir .gitignore
	cd .gitignore
	python3 -m venv venv
	venv/bin/activate
	pip3 install --upgrade pip
	pip3 install -r ../requirements.txt
	deactivate

teardown:
	rm -r setup/.gitignore/venv