def safe_get(data, *keys):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return None