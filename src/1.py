from pydub import AudioSegment

#오디오 파일 로드
audio = AudioSegment.from_file("laser.mp3")

# 시작 시간과 종료 시간 설정
start_time = 0  # 시작 시간(밀리초)
end_time = 300  # 종료 시간(밀리초)

# 오디오 파일 자르기
trimmed_audio = audio[start_time:end_time]

# 자른 오디오 파일 저장
trimmed_audio.export("output.wav", format="wav")

