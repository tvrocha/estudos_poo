from datetime import datetime

@lambda _: _()
def start_time() -> str:
    date = datetime.now()
    return f'{date:%T}'


print(start_time)
