def isAnagram(s: str, t: str) -> bool:
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy')