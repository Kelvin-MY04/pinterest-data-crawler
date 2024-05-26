import urllib.parse

class IO:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def get_query() -> str:
        try:
            return urllib.parse.quote(input("Enter query: "))
        except Exception as e:
            raise e
        
    @staticmethod
    def get_queries() -> list:
        try:
            with open("data/import/query.txt", "r") as file:
                queries = file.read().split("\n")

            return queries
        except Exception as e:
            raise e