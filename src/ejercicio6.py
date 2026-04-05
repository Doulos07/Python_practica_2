from collections import Counter

def analisar_hastags (posts):
    hastags = [
        palabra
        for post in posts
        for palabra in post.split()
        if palabra.startswith('#')
    ]

    hastags = Counter(hastags)

    total = len(hastags)
    tendencia = {k : v for k, v in hastags.items() if int(v) > 1}
    
    return tendencia, total