def get_important_messages(lst: list[str]) -> list[str]:
    result = []
    patterns = ["кр", "дедлайн", "дз", "домашнее задание", "контрольная работа"]
    for string in lst:
    	for pattern in patterns:
            if string.lower().find(pattern) >= 0:
                result.append(string)
    return sorted(set(result))


print(get_important_messages(['Ура!', 'abcd', 'abcd', 'ДЗ', 'дз!!!', 'КР', 'КРРРРРР', 'ДЗ', 'ДЗ']))