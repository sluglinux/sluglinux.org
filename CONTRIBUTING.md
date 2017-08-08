Clone the repo. Enter directory.
  * $ git clone https://github.com/sluglinux/sluglinux.org.git
  * $ cd sluglinux.org
  
Create your virtual environment
  * $ virtualenv env
  * $ source env/bin/activate
  * $ pip install pelican
  * $ pip install Markdown
  * $ pip install Fabric

Make your changes
  * cp 2017-01-18.md 2017-03-15.md
  * nano 2017-03-15.md
  
Test changes by generating the static site and serving it locally
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
