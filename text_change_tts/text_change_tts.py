from gtts import gTTS

text = "아이시떼루"

tts = gTTS(text=text, lang="ko")

#만약 실행 했는데 안되면 아랫줄 경로 문제임
tts.save(r"text_change_tts\Sound.mp3")
 