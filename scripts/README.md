# Scripts

This directory is meant to hold helpful scripts for developers.  They are meant
to be run from the repository root.

## docker-build.sh

Build a Docker image containing the tools needed to generate the site locally.

## docker-run.sh

Run Jekyll in a container using the image built by `docker-build.sh` with ports
passed through to access the `jekyll serve` hosted output.

### Ports

Passes 4000 and 35729 through from the host to the container.
