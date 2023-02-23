from autokakao.wrapper import KakaoAutomation

kakao = KakaoAutomation()

kakao.open_kakao()
kakao.open_chatroom("윤승현")

for i in range(1000):
    kakao.write_message("윤서준 바보")

