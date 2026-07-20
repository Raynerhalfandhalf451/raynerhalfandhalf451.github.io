import json, urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8')
seen = set()
for q in ['hexo+theme+anime', 'hexo+theme+ACG', 'hexo+theme+cute', 'hexo+theme+moe']:
    url = 'https://api.github.com/search/repositories?q=' + q + '&sort=stars&order=desc&per_page=5'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Python'})
        with urllib.request.urlopen(req, timeout=8) as f:
            for r in json.load(f).get('items', []):
                if r['full_name'] not in seen:
                    seen.add(r['full_name'])
                    d = (r['description'] or 'N/A')[:90]
                    print(f"{r['full_name']}")
                    print(f"   Stars: {r['stargazers_count']}  Updated: {r['pushed_at'][:10]}")
                    print(f"   {d}")
                    print(f"   {r['html_url']}\n")
    except:
        pass
