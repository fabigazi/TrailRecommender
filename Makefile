# make commands for Mac OS
trails:
	Python3 trail_recommend.py	

venv:
	#cd setup
	mkdir -p .gitignore	
	python3 -m venv venv
	mv venv .gitignore

requirements:
	pip3 install --upgrade pip
	pip3 install -r setup/requirements.txt
	
teardown:
	rm -r .gitignore/venv