Finds and clones github all repos matching string

Requires pygithub

To Use:
1.  Create a Personal access token in your account on GitHub.  https://github.com/settings/tokens  You should only need "repo" and "public repo" scopes.

2. Set the GITHUB_TOKEN environment variable to the github token

3. Set the GITHUB_USER environment variable to the github user or org that you want to search.

4. Within your roles directory, run get_repos.py <string_to_search>.  It will clone any roles that are absent as long as they match <string_to_search>*.
