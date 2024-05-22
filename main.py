from app.classes.IO import IO
from app.classes.DataCrawler import DataCrawler

def main():
    query = IO.get_query()
    crawler = DataCrawler(query)
    crawler.crawl_data()


if __name__ == "__main__":
    main()