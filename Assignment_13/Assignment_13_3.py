class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value < 2:
            return False
        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

    def Factors(self):
        print(f"Factors of {self.Value} are:", end=" ")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        total = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                total += i
        return total


def main():
    obj1 = Numbers(16)
    obj2 = Numbers(7)

    obj1.Factors()
    print("Prime", obj1.ChkPrime())
    print("Perfect", obj1.ChkPerfect())
    print("Sum of Factors:", obj1.SumFactors())

    obj2.Factors()
    print("Prime", obj2.ChkPrime())
    print("Perfect", obj2.ChkPerfect())
    print("Sum of Factors:", obj2.SumFactors())


if __name__ == "__main__":
    main()
