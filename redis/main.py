# 접속
import redis
import time

# Connect_pool - 직접 연결을 생성해서 해제하는 방식을 사용해도 되지만, 미리 연결을 만들어두고 빌려쓰는 방식을 이용
redis_pool = redis.ConnectionPool(host='localhost', port=6379, max_connections=4)
with redis.StrictRedis(connection_pool=redis_pool) as conn:
    conn.set("name", "이름")

    data = conn.get("name")
    # 문자열 가져오기 - bytes로 리턴
    print(data)  # 한글은 decoding 해야 정상 출력
    print(data.decode('utf8'))  # 디코딩 결과 출력.

    conn.set("name", "이름", 10)
    # 만료 시간 확인
    print(conn.ttl("name")) # time to live

    conn.set("song", "노래")

    # 만료 시간 설정 가능함.
    conn.expire('song', 10)

    print(conn.get("song"))
    time.sleep(11)
    print(conn.get("song"))


    conn.lpush("album", "genesis")
    conn.rpush("album", "exodus")

    for album in conn.lrange("album", 0, 10):
        print(album)