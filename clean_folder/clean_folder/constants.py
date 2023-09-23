CATEGORIES = {
    "Archives": [".zip", ".gz", ".tar"],
    "Audio": [".mp3", ".wav", ".flac", ".wma", ".ogg"],
    "Video": [".avi", ".mp4", ".mov", ".mkv"],
    "Images": [".jpeg", ".png", ".jpg", ".svg", ".gif"],
    "Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
    "Python": [".py", ".rpy", ".pyw", ".cpy", ".gyp", ".gypi", ".pui", ".ipy", ".pyt", ".whl"],
    "Other": [],
}

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "jo",
    "zh",
    "z",
    "y",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "`",
    "y",
    "'",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[c] = l
    TRANS[c.upper()] = l.upper()