from decimal import Decimal

# 실수 표현의 한계 때문에 2개 연산 결과가 다르게 나온다.
print((1234.567 + 45.67844) + 0.0004)
print(1234.567 + (45.67844 + 0.0004))

print((Decimal('1234.567') + Decimal('45.67844')) + Decimal('0.0004'))
print(Decimal('1234.567') + Decimal(('45.67844') + Decimal('0.0004')))