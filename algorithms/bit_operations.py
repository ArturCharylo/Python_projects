class BitwiseOps:
    """A class to demonstrate various bitwise operations."""

    def __init__(self, a: int, b: int = 0):
        self.a = a
        self.b = b

    def bit_and(self) -> int:
        """Returns the result of bitwise AND."""
        return self.a & self.b

    def bit_or(self) -> int:
        """Returns the result of bitwise OR."""
        return self.a | self.b

    def bit_xor(self) -> int:
        """Returns the result of bitwise XOR."""
        return self.a ^ self.b

    def bit_not(self) -> int:
        """Returns the result of bitwise NOT on the first number."""
        return ~self.a

    def shift_left(self, n: int) -> int:
        """Shifts the bits of 'a' to the left by n positions."""
        return self.a << n

    def shift_right(self, n: int) -> int:
        """Shifts the bits of 'a' to the right by n positions."""
        return self.a >> n

    @staticmethod
    def to_binary(x: int) -> str:
        """Returns a string representation of an integer in decimal and binary."""
        return f"{x} (bin: {bin(x)})"

    def is_power_of_2(self) -> bool:
        """Checks if 'a' is a power of 2. Returns a boolean value."""
        # Return type hint to bool as it returns True/False
        return self.a > 0 and (self.a & (self.a - 1)) == 0


def main():
    print("🔹 BitwiseOps Demo 🔹")
    
    # Error handling for user input
    try:
        a = int(input("Please provide the first number (a): "))
        b = int(input("Please provide the second number (b): "))
    except ValueError:
        print("Invalid input! Please provide integer numbers.")
        return

    ops = BitwiseOps(a, b)

    print("\nOperation result:")
    print(f"a AND b = {ops.to_binary(ops.bit_and())}")
    print(f"a OR  b = {ops.to_binary(ops.bit_or())}")
    print(f"a XOR b = {ops.to_binary(ops.bit_xor())}")
    print(f"NOT a   = {ops.to_binary(ops.bit_not())}")
    print(f"a << 2  = {ops.to_binary(ops.shift_left(2))}")
    print(f"a >> 2  = {ops.to_binary(ops.shift_right(2))}")

    print("\nExample of another use case:")
    # is_power_of_2 returns a boolean, which is clear in the output
    print(f"Is number {a} a power of 2? -> {ops.is_power_of_2()}")


if __name__ == "__main__":
    main()