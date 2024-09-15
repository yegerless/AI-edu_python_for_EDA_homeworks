def interesting_trunc(lst: list[str]) -> list[str]:
    return [string[:5].lower() if len(string) > 5 else string.lower() for string in lst]
