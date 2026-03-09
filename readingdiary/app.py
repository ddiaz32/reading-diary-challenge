from readingdiary.view import UIConsole
from datetime import datetime




def main():
    ui = UIConsole()
    ui.run()


if __name__ == '__main__':
    main()


class Note:
    def __init__(self, text: str, page: int, date:datetime):
        self.text = text
        self.page = page
        self.date = date 

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"