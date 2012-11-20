def podaj_zadania(text):
    text = text.replace("\n", "")
    return text.split(".")

print(podaj_zadania("Avdads.\nasdas asdkjsa.\n asdjkasdk.\n"))
