#!/usr/bin/python
# Requires pygithub

from github import Github
import os
import sys

token = os.environ['GITHUB_TOKEN']
github_user = os.environ['GITHUB_USER']
search_pattern = os.environ.get('GITHUB_REPO_PATTERN', sys.argv[1])

g = Github(token)

repolist = g.search_repositories("%s user:%s in:name" %
                            (search_pattern, github_user))

for repo in repolist:
  if os.path.exists(repo.name):
    print "%s exists, skipping" % repo.name
  else:
    print "Cloning %s" % repo.name
    os.system("git clone git@github.com:%s/%s.git" % (github_user, repo.name))
