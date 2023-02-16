# The github-pages Gem requires Ruby 2.
#   https://rubygems.org/gems/github-pages
FROM library/ruby:2-alpine

# The github-pages Gem's dependencies need build tools.
RUN apk add --update build-base
RUN gem install github-pages
