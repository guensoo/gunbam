from collections import defaultdict, Counter

def find_string(strings, index_map, x):
    for s in strings:
        if x in index_map[s]:
            return s
    return None

def solution(s, query):
    strings = [s]
    index_map = {s: set(range(1, len(s) + 1))}
    result = []

    for q in query:
        parts = q.split()
        if parts[0] == '1':
            x, y = int(parts[1]), int(parts[2])
            str_x = find_string(strings, index_map, x)
            str_y = find_string(strings, index_map, y)
            if str_x == str_y:
                result.append("YES")
            else:
                result.append("NO")
        elif parts[0] == '2':
            x = int(parts[1])
            word = parts[2]
            str_x = find_string(strings, index_map, x)
            new_str = ''.join([ch for ch in str_x if ch not in word])
            if new_str:
                strings.append(new_str)
                index_map[new_str] = {i for i in index_map[str_x] if s[i - 1] not in word}
            strings.remove(str_x)
            del index_map[str_x]
        elif parts[0] == '3':
            x, y = int(parts[1]), int(parts[2])
            word = parts[3]
            str_x = find_string(strings, index_map, x)
            new_str = ''.join([s[i - 1] for i in range(x, y + 1) if s[i - 1] in word])
            if new_str:
                strings.append(new_str)
                index_map[new_str] = {i for i in range(x, y + 1) if s[i - 1] in word}
            remaining_str = ''.join([s[i - 1] for i in range(x, y + 1) if s[i - 1] not in word])
            if remaining_str:
                strings.append(remaining_str)
                index_map[remaining_str] = {i for i in range(x, y + 1) if s[i - 1] not in word}
            strings.remove(str_x)
            del index_map[str_x]
        elif parts[0] == '4':
            x, y = int(parts[1]), int(parts[2])
            str_x = find_string(strings, index_map, x)
            str_y = find_string(strings, index_map, y)
            if str_x and str_y and str_x != str_y:
                new_str = str_x + str_y
                strings.append(new_str)
                index_map[new_str] = index_map[str_x] | index_map[str_y]
                strings.remove(str_x)
                strings.remove(str_y)
                del index_map[str_x]
                del index_map[str_y]
        elif parts[0] == '5':
            for s in strings:
                counter = Counter(s)
                alphabet_count = ' '.join(f"{ch} {count}" for ch, count in sorted(counter.items()))
                result.append(alphabet_count)

    return result

# 예제 사용
s = "aba"
query = ["1 1 3", "2 1 b", "3 1 3 a", "4 1 2", "5"]
print(solution(s, query))  # 쿼리 결과

# 테스트 케이스 추가
s1 = "programmers"
query1 = ["1 1 5", "2 1 rm", "1 1 5", "5"]
print(solution(s1, query1))  # ["YES", "NO", "a 1 e 1 g 1 o 1 p 1 s 1", "m 2 r 3"]

s2 = "abacadae"
query2 = ["3 1 4 aa", "1 1 5", "4 1 7", "1 1 5", "5"]
print(solution(s2, query2))  # ["NO", "YES", "a 4 b 1 c 1 d 1 e 1"]
