class KanaData():
    def __init__(cls):
        pass

    @classmethod
    def get_hirgana_to_romaji_dict(cls):
        return cls._hiragana_to_romaji

    @classmethod
    def get_romaji_to_hiragana_dict(cls):
        return cls._romaji_to_hiragana

#---------------------------------------------------------------- KANA DICTIONARIES ---------------------------------------------
    _hiragana_to_romaji = {
        "あ": "a",
        "い": "i",
        "う": "u",
        "え": "e",
        "お": "o",
        "か": "ka",
        "き": "ki",
        "く": "ku",
        "け": "ke",
        "こ": "ko",
        "が": "ga",
        "ぎ": "gi",
        "ぐ": "gu",
        "げ": "ge",
        "ご": "go",
        "ぎゃ": "gya",
        "ぎゅ": "gyu",
        "ぎょ": "gyo",
        "さ": "sa",
        "し": "shi",
        "す": "su",
        "せ": "se",
        "そ": "so",
        "ざ": "za",
        "じ": "ji",
        "ず": "zu",
        "ぜ": "ze",
        "ぞ": "zo",
        "しゃ": "sha",
        "しゅ": "shu",
        "しょ": "sho",
        "じゃ": "ja",
        "じゅ": "ju",
        "じぇ": "je",
        "じょ": "jo",
        "た": "ta",
        "ち": "chi",
        "つ": "tsu",
        "て": "te",
        "と": "to",
        "ちゃ": "cha",
        "ちゅ": "chu",
        "ちょ": "cho",
        "つぁ": "tsa",
        "つぃ": "tsi",
        "つぉ": "tso",
        "だ": "da",
        "ぢ": "ji",
        "づ": "zu",
        "で": "de",
        "ど": "do",
        "ぢゃ": "ja",
        "ぢゅ": "ju",
        "ぢょ": "jo",
        "な": "na",
        "に": "ni",
        "ぬ": "nu",
        "ね": "ne",
        "の": "no",
        "にゃ": "nya",
        "にゅ": "nyu",
        "にょ": "nyo",
        "は": "ha",
        "ひ": "hi",
        "ふ": "fu",
        "へ": "he",
        "ほ": "ho",
        "ひゃ": "hya",
        "ひゅ": "hyu",
        "ひょ": "hyo",
        "ふゃ": "fya",
        "ふゅ": "fyu",
        "ふょ": "fyo",
        "ふぁ": "fa",
        "ふぃ": "fi",
        "ふぇ": "fe",
        "ふぉ": "fo",
        "ば": "ba",
        "び": "bi",
        "ぶ": "bu",
        "べ": "be",
        "ぼ": "bo",
        "びゃ": "bya",
        "びゅ": "byu",
        "びょ": "byo",
        "ぱ": "pa",
        "ぴ": "pi",
        "ぷ": "pu",
        "ぺ": "pe",
        "ぽ": "po",
        "ぴゃ": "pya",
        "ぴゅ": "pyu",
        "ぴょ": "pyo",
        "ま": "ma",
        "み": "mi",
        "む": "mu",
        "め": "me",
        "も": "mo",
        "みゃ": "mya",
        "みゅ": "myu",
        "みょ": "myo",
        "や": "ya",
        "ゆ": "yu",
        "よ": "yo",
        "ら": "ra",
        "り": "ri",
        "る": "ru",
        "れ": "re",
        "ろ": "ro",
        "りゃ": "rya",
        "りゅ": "ryu",
        "りょ": "ryo",
        "わ": "wa",
        "を": ["wo", "o"],
        "ん": "n"
    }

    _romaji_to_hiragana = {
        "a" : "あ",
        "i" : "い",
        "u" : "う",
        "e" : "え",
        "o" : "お",
        "ka" : "か",
        "ki" : "き",
        "ku" : "く",
        "ke" : "け",
        "ko" : "こ",
        "ga" : "が",
        "gi" : "ぎ",
        "gu" : "ぐ",
        "ge" : "げ",
        "go" : "ご",
        "Ja" : "ぎゃ",
        "Ju" : "ぎゅ",
        "Jo" : "ぎょ",
        "chi" : "さ",
        "shi" : "し",
        "su" : "す",
        "se" : "せ",
        "so" : "そ",
        "Ji" : "ざ",
        "ji" : "じ",
        "zu" : "ず",
        "ze" : "ぜ",
        "zo" : "ぞ",
        "sha" : "しゃ",
        "shu" : "しゅ",
        "sho" : "しょ",
        "ja" : "じゃ",
        "ju" : "じゅ",
        "je" : "じぇ",
        "jo" : "じょ",
        "ta" : "た",
        "tsu" : "つ",
        "te" : "て",
        "to" : "と",
        "cha" : "ちゃ",
        "chu" : "ちゅ",
        "cho" : "ちょ",
        "tsa" : "つぁ",
        "tsi" : "つぃ",
        "tso" : "つぉ",
        "da" : "だ",
        "zu" : "づ",
        "de" : "で",
        "do" : "ど",
        "cha" : "ぢゃ",
        "chu" : "ぢゅ",
        "cho" : "ぢょ",
        "na" : "な",
        "ni" : "に",
        "nu" : "ぬ",
        "ne" : "ね",
        "no" : "の",
        "nya" : "にゃ",
        "nyu" : "にゅ",
        "nyo" : "にょ",
        "ha" : "は",
        "hi" : "ひ",
        "fu" : "ふ",
        "he" : "へ",
        "ho" : "ほ",
        "hya" : "ひゃ",
        "hyu" : "ひゅ",
        "hyo" : "ひょ",
        "fya" : "ふゃ",
        "fyu" : "ふゅ",
        "fyo" : "ふょ",
        "fa" : "ふぁ",
        "fi" : "ふぃ",
        "fe" : "ふぇ",
        "fo" : "ふぉ",
        "ba" : "ば",
        "bi" : "び",
        "bu" : "ぶ",
        "be" : "べ",
        "byo" : "ぼ",
        "pya" : "びゃ",
        "pyu" : "びゅ",
        "pyo" : "びょ",
        "pa" : "ぱ",
        "pi" : "ぴ",
        "pu" : "ぷ",
        "pe" : "ぺ",
        "po" : "ぽ",
        "pya" : "ぴゃ",
        "pyu" : "ぴゅ",
        "pyo" : "ぴょ",
        "mo" : "ま",
        "mi" : "み",
        "mu" : "む",
        "me" : "め",
        "mo" : "も",
        "mya" : "みゃ",
        "myu" : "みゅ",
        "myo" : "みょ",
        "ya" : "や",
        "yu" : "ゆ",
        "yo" : "よ",
        "ra" : "ら",
        "ri" : "り",
        "ru" : "る",
        "re" : "れ",
        "ro" : "ろ",
        "ryo" : "りゃ",
        "ryu" : "りゅ",
        "ryo" : "りょ",
        "wa" : "わ",
        "o" : "を",
        "n" : "ん"
    }
