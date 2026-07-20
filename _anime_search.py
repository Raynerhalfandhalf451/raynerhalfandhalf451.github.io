import json, urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8')

queries = [
    'anime+jekyll+theme',
    'acg+jekyll+theme',
    'cute+jekyll+theme',
    '二次元+jekyll+theme',
    'anime+hugo+theme',
]

seen = set()
for q in queries:
    url = f'https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=8'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
        with urllib.request.urlopen(req, timeout=8) as f:
            data = json.load(f)
        for r in data.get('items', []):
            if r['full_name'] not in seen:
                seen.add(r['full_name'])
                desc = (r['description'] or 'No description')[:100]
                print(f'{r["full_name"]}')
                print(f'   Stars: {r["stargazers_count"]}  Updated: {r["pushed_at"][:10]}')
                print(f'   {desc}')
                print(f'   {r["html_url"]}')
            print()
    except:
        pass
