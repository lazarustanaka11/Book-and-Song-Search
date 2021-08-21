# install app and dependencies
install:
	pip install --upgrade pip
	pip install -e .
	python -m venv venv
	source ./venv/bin/activate


commit:
	black ./src/
	git add -u
	git commit -m "update"
	git push

ammend_commit:
	black ./src/
	git add -u
	git commit --amend --no-edit
	git push -f

run:
	python src/interface.py
