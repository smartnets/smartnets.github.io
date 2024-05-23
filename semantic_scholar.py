import requests
import json

def fetch_recent_publications(author_id, num_publications=20):
    base_url = f"https://api.semanticscholar.org/graph/v1/author/{author_id}/papers"
    params = {
        "fields": "url,venue,year,title,authors",
        "limit": num_publications
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    papers_data = response.json()
    
    publications = []
    for paper in papers_data['data']:
        venue = paper.get('venue', 'arXiv.org')
        pub_info = {
            "title": paper.get('title', 'N/A'),
            "author": ", ".join([author['name'] for author in paper.get('authors', [])]),
            "venue": venue if venue else 'arXiv.org',
            "year": paper.get('year', 'N/A'),
            "url": paper.get('url', 'N/A'),
        }
        publications.append(pub_info)

    return publications

author_id = "2065219256"  # Leandros Tassiulas ID
publications = fetch_recent_publications(author_id)

# Save publications data to a JSON file
with open('_data/publications.json', 'w') as f:
    json.dump(publications, f, indent=4)
