from crawler import WebCrawler

def main():
    # Configuration personnalisée
    start_url = "https://www.ouellet.com/fr-ca/"
    crawler = WebCrawler(
        start_url=start_url,
        max_depth=3  # Profondeur de crawling plus importante
    )
    
    # Démarrage du crawling
    crawler.crawl()

if __name__ == "__main__":
    main()
