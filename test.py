B = 12
Q = 256

def get_hash(pattern:str) -> int:
    global B, Q
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (B * result + ord(pattern[i])) % Q
    return result

def search_patterns_in_text(main_text: str, pattern: str) -> None:
    global B, Q
    pattern_len = len(pattern)
    print(pattern_len)
    main_text_len = len(main_text)

    multiplier = 1
    for i in range(1,pattern_len):
        multiplier = (multiplier * B) % Q

    pattern_hash = get_hash(pattern)
    print("ppattern hash:",pattern_hash)
    print(main_text[i:pattern_len])
    main_text_hash = get_hash(main_text[:pattern_len])
    print("main text hash:", main_text_hash)


search_patterns_in_text("mmmasdmm","a")


