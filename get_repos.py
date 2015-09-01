#!/usr/bin/python
# Requires pygithub

from github import Github
import os

token = os.environ['GITHUB_TOKEN']
github_user = os.environ['GITHUB_USER']

g = Github(login_or_token=token)

repolist = g.search_repositories("ansible-role- user:%s in:name" % (github_user))

for repo in repolist:
  if os.path.exists(repo.name):
    print "%s exists, skipping" % repo.name
  else:
    print "Cloning %s" % repo.name
    os.system("git clone git@github.com:%s/%s.git" % (github_user, repo.name))

