import requests
import json
from datetime import datetime, timedelta


def get_trending_repositories(top_size, count_of_days):
    days_ago = (
        datetime.today() - timedelta(count_of_days)
    ).strftime('%Y-%m-%d')
    params = {'q': 'created>{}'.format(days_ago),
              'sort': 'stars', 'order': 'desc'}
    all_repos = requests.get(
        'https://api.github.com/search/repositories',
        params=params
    ).json()
    trend_repo = all_repos['items'][:top_size]
    return trend_repo


def get_repos_and_issues(owner, repo_name):
    data_issue = requests.get(
        'https://api.github.com/repos/{}/{}/issues'.format(
            owner,
            repo_name
        )
    ).json()
    return data_issue


def print_repo_info(repo_name, html_url, count_of_issues):
    print('Repository: {}'.format(repo_name))
    print('URL: {}'.format(html_url))
    print('Count of issues: {}'.format(count_of_issues))


if __name__ == '__main__':
    top_size = 20
    count_of_days = 7
    trending_repos = get_trending_repositories(top_size, count_of_days)
    for repo in trending_repos:
        issues = (get_repos_and_issues(repo['owner']['login'], repo['name']))
        print_repo_info(repo['name'], repo['html_url'], len(issues))
