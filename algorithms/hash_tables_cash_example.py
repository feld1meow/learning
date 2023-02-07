cache = {}


def get_page(url):
    if cache.get(url):
        return cache[url]  # возвращение кэшируемых данных
    else:
        data = get_data_from_server(url)
        cache[url] = data  # данные сначала сохраняются в кэше
        return data


get_page(any_url)
