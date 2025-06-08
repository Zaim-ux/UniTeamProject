# UniTeamProject
A project I lead with a team of 8 other people. This project is a restaurant database management system that allows customers to order food from a digital menu, waiters to track orders and requests and kitchen staff to track what needs to be cooked.

# Setup virtual enviroments
	(so modules and dependencies are consistent, not used from your PC):
	Create directory "venvs"
	pip install virtualenv
	in your "venvs" directory run:
		  python3 -m venv <name>  /  where name could be something like "CS2810"
	when you want to activate the virtual enviroment (for running/testing the project):
		Windows:
			in the new directory run:
				Scripts\activate.bat
		Linux/MacOS:
			in the new directory run:
			source env/bin/activate 

# Django
	python -m pip install Django
	create a new project structure:
		django-admin startproject <projectName>  (start project, files ready)
	run once you are in project directory:
		python manage.py runserver
		I believe default local URL is "http://127.0.0.1:8000/" - check cmd for yours

# Git
	Create an access token in for your gitlab account:
		gitlab>profile icon>preferences>access tokens>add new token> select read_repository, write_repository>
		save the token locally.
	helpful to do this in the virtual enviroment:
	git clone https://gitlab.cim.rhul.ac.uk/TeamProject13/TeamProject13.git
	git config --global --add merge.ff false  (in venv)
	git authentication will take gitlab username and this token
	
	branch: git checkout <brancName> - for the feature you are working on
	git pull every so often, especially if it is at a time where others are likely to be working
	merges: fix manually, git merge --continue  /  This should not happen too often if task allocation is tidy.
	
	git add -A  /  add all your local files to the local working tree
	git commit -m "Message."
	git push

# Other
    If there are issues please communicate with the team, solutions / fixes will be listed here


# Team Project

This repository has been created to store your Team Project.

You may edit it as you like, but please do not remove the default topics or the project members list. These need to stay as currently defined in order for your lecturer to be able to find and mark your work.
