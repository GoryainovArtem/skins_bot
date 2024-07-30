def read_html_file(file_path: str):
    """Получить содержимое html файла."""
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
        return content


# print(read_html_file("../static/card.html"))
