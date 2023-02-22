# Overview

Please open a pull request or issue for any changes you think are appropriate.

# Workflow

Clone the repo and enter directory
* `$ git clone https://github.com/sluglinux/sluglinux.org.git`
* `$ cd sluglinux.org`

Build the Docker image
* `$ ./scripts/docker-build.sh`

Make your changes
* `$ cp _posts/minutes/2017-07-19-.md _posts/minutes/2017-09-20-.md`
* `$ nano _posts/minutes/2017-09-20-.md`

> **_NOTE:_**  There is an extra hyphen (`-`) before the file extension.  This
> is to work around the fact that Jekyll wants the post title in the filename.
> Custom collections did not nicely solve this issue, and a plugin to change the
> behavior is not supported by GitHub Pages.

Test changes by generating the static site and serving it locally
* `$ ./scripts/docker-run.sh`
* visit <http://localhost:4000/>

Commit your changes to a branch
* `$ git checkout -b <your branch name>`
* `$ git status # view files that have been changed`
* `$ git add <file that you changed or added>`
* `$ git commit -m "Add 2017-09-20 meeting minutes"`
* `$ git push`

> **_NOTE:_**  This may require forking the repository, adding your fork as
> another remote, and pushing to that remote.  Please feel free to ask for help!

Open a pull request to merge your branch, ideally with a rebase and fast-forward
with no merge commit.

The [Pro Git book](https://git-scm.com/book/) is an invaluable resource for
getting up to speed with Git!
