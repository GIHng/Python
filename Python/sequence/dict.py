dic = {}
dic["name"] = "A"
dic["job"] = "B"
dic["father"] = "pms"
dic["father"] = "ds"  # 마지막으로 들어간 값으로 적용 됨.

print(dic)

print(dic["job"])
print(dic.get("job", "nojob"))
# print(dic["score"])  # 존재하지 않는 key를 사용하는 KeyError 발생
print(dic.get("score", 0))  # 존재하지 않는 key를 사용하면 두번째 매개변수(default) 리턴
for key in dic:
    print(key)
