import requests
import json
from datetime import datetime, timedelta


def get_trending_repositories(top_size):
    last_week = (datetime.today() - timedelta(7)).strftime("%Y-%m-%d")
    params = {'q': 'created>{}'.format(last_week), 'sort': 'stars', 'order': 'desc'}
    response = requests.get('https://api.github.com/search/repositories', params=params).json()
    trend_repo = response["items"][:top_size]
    return trend_repo


def repo_info_view(repos):
    for repo in repos:
        print('name: {}'.format(repo["name"]))
        print('open_issues: {}'.format(repo["open_issues"]))
        print('html_url {}'.format(repo["html_url"]))


if __name__ == '__main__':
    top_size = 20
    repos = get_trending_repositories(top_size)
    repo_info_view(repos)
