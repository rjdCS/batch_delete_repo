# ================================
# Descripttion: 
# Author: RJD
# Date: 2021-05-25 16:36:36
# LastEditors: RJD
# LastEditTime: 2021-05-25 16:44:59
# FilePath: /undefined/Users/rjd/Desktop/new.py
# ================================
from time import sleep
import requests

headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "token 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", # 此处的XXX代表上面的token
    "X-OAuth-Scopes": "repo"
}

with open('./repo.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

url = "https://api.github.com/repos/{}/{}"
urls = []
for line in data:
    name, repo = line.strip().split("/")
    urls.append(url.format(name, repo))

for idx,l in enumerate(urls):
    requests.delete(url=l, headers=headers)
    print(f"已删除:{l} —— {idx+1}/{len(urls)}")
    sleep(2)