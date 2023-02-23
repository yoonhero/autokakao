# Automation Kakao for Mac

Kakaotalk open chatting room and send message automatically with applescript.

![result](./docs/result.gif)

## Installation

```bash
pip install autokakao
```


## API

First import package.

```python
from autokakao.wrapper import KakaoAutomation
```

### Open kakao application manually

```python
kakao = KakaoAutomation()
kakao.open_kakao()
```

### Open chat room with chat room name

```python
kakao = KakaoAutomation()
kakao.open_chatroom("CHATROOM NAME")
```

### Write a message to send

```python
kakao = KakaoAutomation()
kakao.write_message("YOUR MESSAGE")
```


## Example 

```python
from autokakao.wrapper import KakaoAutomation

kakao = KakaoAutomation()

kakao.open_kakao()
kakao.open_chatroom("윤서준")

for i in range(1000):
    kakao.write_message("윤서준 바보")
```

## License 

MIT


