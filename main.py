import re

def text_stat(filename):
    # Проверяем, что имя файла не пустое
    if not filename:
        return {'error': 'Имя файла не найдено'}

    try:
        with open(filename, 'r') as file:
            content = file.read()

            # Рассчитываем частоту использования каждой буквы
            letters_freq = {}
            for letter in content:
                if letter.isalpha():
                    if letter in letters_freq:
                        letters_freq[letter] += 1
                    else:
                        letters_freq[letter] = 1

            # Рассчитываем количество слов в тексте
            words = re.findall(r'\w+', content)

            word_amount = len(words)

            # Рассчитываем количество абзацев в тексте
            paragraphs = content.split('\n\n')
            paragraph_amount = len(paragraphs)

            # Рассчитываем долю слов, в которых встречается конкретная буква
            letter_word_ratio = {}
            for letter in letters_freq:
                letter_count = 0
                for word in words:
                    if letter in word:
                        letter_count += 1
                letter_word_ratio[letter] = letter_count / word_amount

            # Рассчитываем количество слов, в которых одновременно встречаются буквы обоих алфавитов
            bilingual_word_amount = 0
            for word in words:
                if any(c.isalpha() for c in word):
                    if any(c.isalpha() and ord(c) > 127 for c in word) and any(c.isalpha() and ord(c) <= 127 for c in word):
                        bilingual_word_amount += 1

            # Возвращаем словарь с результатами
            return {
                'letters_freq': letters_freq,
                'word_amount': word_amount,
                'paragraph_amount': paragraph_amount,
                'letter_word_ratio': letter_word_ratio,
                'bilingual_word_amount': bilingual_word_amount
            }

    except FileNotFoundError:
        return {'error': 'Файл не найден'}
    except:
        return {'error': 'Возникла ошибка при обработке файла'}
result = text_stat('example.txt')
print(result)
