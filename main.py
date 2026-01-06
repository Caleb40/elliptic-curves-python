from __future__ import annotations

from typing import List


class FieldElement:
    def __init__(self, order: int, num: int):
        if num >= order:
            error = 'Num {} not in field range 0 to {}'.format(
                num, order - 1)
            raise ValueError(error)
        self.order = order
        self.num = num

    def check_order(self, other: FieldElement) -> None:
        if self.order != other.order:
            raise TypeError(
                f"Field mismatch: source element has the order {self.order}, target element has the order {other.order}")
        return

    def __repr__(self) -> str:
        # return f"FieldElement[<order: {self.order}, num: {self.num}>]"
        return f"FieldElement_{self.order}({self.num})"

    def __eq__(self, other: FieldElement) -> bool:
        if other is None:
            return False
        if not isinstance(other, self.__class__):
            return False
        return self.order == other.order and self.num == other.num

    def __add__(self, other: FieldElement) -> FieldElement:
        self.check_order(other)
        return self.__class__(self.order, (self.num + other.num) % self.order)

    def __neg__(self) -> FieldElement:
        # return FieldElement(self.order, (self.order - self.num) % self.order) functionally equivalent
        return self.__class__(self.order, (-self.num) % self.order)

    def __sub__(self, other: FieldElement) -> FieldElement:
        self.check_order(other)
        return self + (-other)

    def __mul__(self, other: FieldElement) -> FieldElement:
        self.check_order(other)
        return self.__class__(self.order, (self.num * other.num) % self.order)

    def __pow__(self, power: int) -> FieldElement:
        return self.__class__(self.order, (self.num ** power) % self.order)

    def __matmul__(self, value: int) -> List[FieldElement]:
        values = []
        for i in range(self.num):
            elem = self.__class__  (self.order, i)
            product = elem * self.__class__(self.order, value)
            values.append(product)
        return values


f44 = FieldElement(57, 44)
f33 = FieldElement(57, 33)
res = f44 + f33
print(f"Field element 44 added to field element 33 is:", res)
print(f"Negated value of field element 44 is {-res}\n")

print(f"Field Element 44 - 33 is: {f44 - f33}")
print(f"Field Element 33 - 44 is: {f33 - f44}")
f46 = FieldElement(57, 46)
print(f"Field Element 46 + 44 is: {f46 + f44}\n")

print(f"Product of Element 46 with itself is: {f46 * f46}")
print(f"Exponent of Element 46 with 2 is: {f46 ** 2}")
# Check:
print(f"CHECK: 46^2 and 46 * 46 are equivalent: {f46 * f46 == f46 ** 2}\n")

f_small = FieldElement(57, 22)
print(f"Result of Mat mul operation by {3} is: {f_small @ 3}")
