def filter_spoiler(review, filtro):
    filtro = [f.strip().lower() for f in filtro]
    text = review.split()
    review_filter = [ '*'*len(t) if t.lower() in filtro else t  for t in text]
    return ' '.join(review_filter)