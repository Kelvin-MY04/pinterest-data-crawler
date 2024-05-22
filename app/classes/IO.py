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