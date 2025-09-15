class BitwiseOps:
    def __init__(self, a: int, b: int = 0):
        self.a = a
        self.b = b

    # Basic operations
    def bit_and(self) -> int:
        return self.a & self.b

    def bit_or(self) -> int:
        return self.a | self.b

    def bit_xor(self) -> int:
        return self.a ^ self.b

    def bit_not(self) -> int:
        return ~self.a

    # Bit shift
    def shift_left(self, n: int) -> int:
        return self.a << n

    def shift_right(self, n: int) -> int:
        return self.a >> n

    # Helper: binary representation
    @staticmethod
    def to_binary(x: int) -> str:
        return f"{x} (bin: {bin(x)})"

    # Custom examples of use
    def custom_example(self) -> int:
        return self.a > 0 and (self.a & (self.a - 1)) == 0


def main():
    print("🔹 BitwiseOps Demo 🔹")
    a = int(input("Please provide the first number (a): "))
    b = int(input("Please provide the second number (b): "))

    ops = BitwiseOps(a, b)

    print("\nOperation result:")
    print(f"a AND b = {ops.to_binary(ops.bit_and())}")
    print(f"a OR  b = {ops.to_binary(ops.bit_or())}")
    print(f"a XOR b = {ops.to_binary(ops.bit_xor())}")
    print(f"NOT a   = {ops.to_binary(ops.bit_not())}")
    print(f"a << 2  = {ops.to_binary(ops.shift_left(2))}")
    print(f"a >> 2  = {ops.to_binary(ops.shift_right(2))}")

    print("\nExample of another use case:")
    print(f"Is number {a} a power of 2? -> {ops.custom_example()}")


if __name__ == "__main__":
    main()
