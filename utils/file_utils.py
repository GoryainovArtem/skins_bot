def read_html_file(file_path: str, mode):
    """Получить содержимое html файла."""
    with open(file_path, mode) as file:
        content = file.read()
        return content


# print(read_html_file("../static/card.html"))
