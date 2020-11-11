def string_task(s):
    blocked = ["a", "o", "y", "e", "u", "i"]
    s = s.lower()
    letters = list(s)

    for i in letters:
        if i in blocked:
            letters.remove(i)
        listToStr = '.'.join([str(i) for i in letters])
        result = "." + listToStr
    print(result)
    return(result)

string_task("Tour")  # WHY IT RETURN WITH "U" LETTER!??!
