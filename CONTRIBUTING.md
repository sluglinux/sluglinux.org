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

Generate production html and upload
  * $ make publish
  * $ make rsync_upload