# removed time pkg because it useless!
# edit katakana table here
def katakana(char):
    katakana_char = {
        'a': 'ア',
        'i': 'イ',
        'u': 'ウ',
        'e': 'エ',
        'o': 'オ',
        'ka': 'カ',
        'ki': 'キ',
        'ku': 'ク',
        'ke': 'ケ',
        'ko': 'コ',
        'ga': 'ガ',
        'gi': 'ギ',
        'gu': 'グ',
        'ge': 'ゲ',
        'go': 'ゴ',
        'sa': 'サ',
        'shi': 'シ',
        'su': 'ス',
        'se': 'セ',
        'so': 'ソ',
        'za': 'ザ',
        'ji': 'ジ',
        'zu': 'ズ',
        'ze': 'ゼ',
        'zo': 'ゾ',
        'ta': 'タ',
        'chi': 'チ',
        'tsu': 'ツ',
        'te': 'テ',
        'to': 'ト',
        'da': 'ダ',
        'di': 'ディ',  # Included for completeness
        'du': 'ドゥ',  # Included for completeness
        'de': 'デ',
        'do': 'ド',
        'na': 'ナ',
        'ni': 'ニ',
        'nu': 'ヌ',
        'ne': 'ネ',
        'no': 'ノ',
        'ha': 'ハ',
        'hi': 'ヒ',
        'fu': 'フ',
        'he': 'ヘ',
        'ho': 'ホ',
        'ba': 'バ',
        'bi': 'ビ',
        'bu': 'ブ',
        'be': 'ベ',
        'bo': 'ボ',
        'pa': 'パ',
        'pi': 'ピ',
        'pu': 'プ',
        'pe': 'ペ',
        'po': 'ポ',
        'ma': 'マ',
        'mi': 'ミ',
        'mu': 'ム',
        'me': 'メ',
        'mo': 'モ',
        'ya': 'ヤ',
        'yu': 'ユ',
        'yo': 'ヨ',
        'ra': 'ラ',
        'ri': 'リ',
        'ru': 'ル',
        're': 'レ',
        'ro': 'ロ',
        'wa': 'ワ',
        'wo': 'ヲ',
        'n': 'ン'
    }
    output = ''
    for word in char:
        output += katakana_char.get(word, word)
    return output
# edit hiragana table here
def hiragana(char):
    hiragana_char = {
    'a': 'あ',
    'i': 'い',
    'u': 'う',
    'e': 'え',
    'o': 'お',
    'ka': 'か',
    'ki': 'き',
    'ku': 'く',
    'ke': 'け',
    'ko': 'こ',
    'ga': 'が',
    'gi': 'ぎ',
    'gu': 'ぐ',
    'ge': 'げ',
    'go': 'ご',
    'sa': 'さ',
    'shi': 'し',
    'su': 'す',
    'se': 'せ',
    'so': 'そ',
    'za': 'ざ',
    'ji': 'じ',
    'zu': 'ず',
    'ze': 'ぜ',
    'zo': 'ぞ',
    'ta': 'た',
    'chi': 'ち',
    'tsu': 'つ',
    'te': 'て',
    'to': 'と',
    'da': 'だ',
    'di': 'ぢ',
    'du': 'づ',
    'de': 'で',
    'do': 'ど',
    'na': 'な',
    'ni': 'に',
    'nu': 'ぬ',
    'ne': 'ね',
    'no': 'の',
    'ha': 'は',  # Particle "wa"
    'hi': 'ひ',
    'fu': 'ふ',
    'he': 'へ',
    'ho': 'ほ',
    'ba': 'ば',
    'bi': 'び',
    'bu': 'ぶ',
    'be': 'べ',
    'bo': 'ぼ',
    'pa': 'ぱ',
    'pi': 'ぴ',
    'pu': 'ぷ',
    'pe': 'ぺ',
    'po': 'ぽ',
    'ma': 'ま',
    'mi': 'み',
    'mu': 'む',
    'me': 'め',
    'mo': 'も',
    'ya': 'や',
    'yu': 'ゆ',
    'yo': 'よ',
    'ra': 'ら',
    'ri': 'り',
    'ru': 'る',
    're': 'れ',
    'ro': 'ろ',
    'wa': 'は',  # Sound "wa"
    'wo': 'を',
    'n': 'ん'
}
    output = ''
    for word in char:
        output += hiragana_char.get(word, word)
    return output

def run():
    print("Please Add spacing between words for example kata will be ka ta!")
    msg = input("Enter Japanese spelling in English: ")
    char = msg.split(' ')
    print(char)
    try:
        choice = int(input("""
        ======= Choose one of the following options!
        ===== のいずれかを選択する！
            > (1) Hiragana
            > (2) Katakana
            Enter the number!
            番号を入力する！
        """))
        if choice == 1:
            print(hiragana(char))
        elif choice == 2:
            print(katakana(char))
        else:
            print("Please enter 1 or 2")
            run()
    except ValueError:
        print("""
Please enter a valid number like 1 or 2!
Choice is an int(), not a str()! 💢
        """)
        run()

run()
