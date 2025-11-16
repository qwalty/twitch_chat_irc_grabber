import ahocorasick

# словарь: слово -> ссылка
words = {
    "python": "<a href='python_link'>python</a>",
    "код": "<a href='code_link'>код</a>",
    "поиск": "<a href='search_link'>поиск</a>",
}

A = ahocorasick.Automaton()

# добавляем слова
for word, link in words.items():
    A.add_word(word, (word, link))

A.make_automaton()

text = "Этот код показывает быстрый поиск слов на python."

result = []
pos = 0

i = 0
while i < len(text):
    match = A.get(text[i])
    if match:
        (end_index, (word, link)) = match
        start = i + end_index - len(word) + 1

        # добавляем текст до слова
        result.append(text[pos:start])
        # добавляем замену
        result.append(link)
        pos = start + len(word)
        i = pos
    else:
        break

# добавляем остаток
result.append(text[pos:])

out = "".join(result)
print(out)
