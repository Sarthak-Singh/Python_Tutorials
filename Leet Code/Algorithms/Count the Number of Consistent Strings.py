def countConsistentStrings(allowed, words):
    allowed = set(allowed)
    count = 0
    for x in words:
        for y in x:
            if y not in allowed:
                count += 1
                break
    return len(words) - count


print(countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
