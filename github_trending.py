import requests
import json
from datetime import datetime, timedelta


def get_trending_repositories(top_size, count_of_days):
    days_ago = (datetime.today() -
                timedelta(count_of_days)).strftime('%Y-%m-%d')
    params = {'q': 'created>{}'.format(days_ago),
              'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories',
                            params=params).json()
    trend_repo = response['items'][:top_size]
    return trend_repo


def get_repos_and_issues(repos):
    list_of_repos = []
    for repo in repos:
        owner = repo['owner']['login']
        repo_name = repo['name']
        html_url = repo['html_url']
        response = requests.get('https://api.github.com/repos/{}/{}/issues'.
                                format(owner, repo_name)).json()
        issues_qty = len(response)
        list_of_repos.append({'owner': owner,
                              'repo_name': repo_name,
                              'html_url': html_url,
                              'count_of_issues': issues_qty
                              })
    return list_of_repos


def print_repo_info(repos):
    for repo in repos:
        print('owner: {}'.format(repo['owner']))
        print('repo_name: {}'.format(repo['repo_name']))
        print('open_issues: {}'.format(repo['count_of_issues']))
        print('html_url {}'.format(repo['html_url']))


if __name__ == '__main__':
    top_size = 20
    count_of_days = 7
    trending_repos = get_trending_repositories(top_size, count_of_days)
    repos_and_issues = get_repos_and_issues(trending_repos)
    print_repo_info(repos_and_issues)
