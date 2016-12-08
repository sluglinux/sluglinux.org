Clone the repo. Enter directory.
  * $ git clone git@gitlab.mooncitylabs.org:slug/sluglinux.org.git
  * $ cd sluglinux.org
  
Create your virtual environment
  * $ virtualenv env
  * $ source env/bin/activate
  * $ pip install pelican
  * $ pip install Markdown
  * $ pip install Fabric
  
Generate static page and serve locally
  * $ make html
  * $ make serve
  * visit localhost:8000

Generate production html and save changes in git
  * $ make publish
  * $ git status # view files that have been changed
  * $ git add <file that you changed or added>
  * $ git commit -m "commit message"
  * $ git push"
  * $ upload output to sluglinux.github.io repo somehow (to be updated)
  

