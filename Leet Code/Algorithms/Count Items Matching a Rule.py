def countMatches(items, ruleKey, ruleValue):
    count = 0
    if ruleKey == "type":
        ind = 0
    elif ruleKey == "color":
        ind = 1
    else:
        ind = 2
    for x in items:
        if x[ind] == ruleValue:
            count += 1
    return count


print(countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], "type", "phone"))
