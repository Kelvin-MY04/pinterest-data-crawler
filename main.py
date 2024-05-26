from app.classes.IO import IO
from app.classes.DataCrawler import DataCrawler

def main():
    # query = IO.get_query()
    queries = IO.get_queries()
    for i, query in enumerate(queries):
        print(f"({i + 1}/{len(queries)}) {query} is crawling...")
        crawler = DataCrawler(query)
        crawler.crawl_data()


if __name__ == "__main__":
    main()