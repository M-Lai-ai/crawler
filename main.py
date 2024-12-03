from crawler import WebCrawler

def main():
    # URL de départ pour le crawling
    start_url = "https://example.com/fr-ca/"  # Remplacez par votre URL
    
    # Création d'une instance du crawler
    crawler = WebCrawler(start_url, max_depth=3)
    
    # Démarrage du crawling
    crawler.crawl()

if __name__ == "__main__":
    main()
