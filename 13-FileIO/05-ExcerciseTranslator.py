from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open('test.txt', mode='r') as file:
        text = file.read()
        translation = translator.translate(text)
        # print(translation)
        with open('test-trans.txt', mode='w') as file2:
            file2.write(translation)
except FileNotFoundError:
    print('File not found')
