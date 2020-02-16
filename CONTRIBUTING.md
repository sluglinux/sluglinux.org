Clone the repo and enter directory
  * $ git clone https://github.com/sluglinux/sluglinux.org.git
  * $ cd sluglinux.org
  
Create your virtual environment
  * $ virtualenv env
  * $ source env/bin/activate
  * $ pip install pelican
  * $ pip install Markdown
  * $ pip install Fabric

Make your changes
  * cp content/minutes/2017-07-19.md content/minutes/2017-09-20.md
  * nano content/minutes/2017-09-20.md

Test changes by generating the static site and serving it locally
  * $ make html
  * $ make serve
  * visit localhost:8000

Generate production html and save changes in git
  * $ make publish
  * $ git status # view files that have been changed
  * $ git add \<file that you changed or added\>
  * $ git commit -m "added the minutes for the 2017-09-20 meeting."
  * $ git push

Get the changes into the sluglinux.github.io repo
  * $ cd ../
  * $ git clone https://github.com/sluglinux/sluglinux.github.io.git
  * $ cp -r ./sluglinux.org/output/* ./sluglinux.github.io/
  * $ cd sluglinux.github.io
  * $ git status # view files that have been changed
  * $ git add .
  * $ git commit -m "Deploy site from the Pelican repository"
  * $ git push
