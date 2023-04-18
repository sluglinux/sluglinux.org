#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

docker run \
    --rm \
    --interactive \
    --tty \
    --volume $PWD:/site \
    --workdir /site \
    --publish 4000:4000/tcp \
    --publish 35729:35729/tcp \
    --name sluglinux-build \
    sluglinux-build:latest \
    bundle exec jekyll serve --destination /tmp/site --watch --host 0.0.0.0 --livereload --incremental
