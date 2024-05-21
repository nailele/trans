def extract_explanations(nested_list: list):
    result = []

    def recurse(lst):
        for item in lst:
            if isinstance(item, str):
                result.append(item)
            elif isinstance(item, list):
                recurse(item)
    recurse(nested_list)

    return result


def extract_translations(nested_list):
    result = {}

    def recurse(lst):
        for item in lst:
            if isinstance(item, list):
                if item and isinstance(item[0], str):
                    english_word = item[0]
                    russian_translations = item[2] if isinstance(item[2], list) else []
                    result[english_word] = russian_translations
                else:
                    recurse(item)
    recurse(nested_list)

    return result
