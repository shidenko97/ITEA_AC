class RomanNumeralInterpreter:
    """Interpreter of Roman numerals"""

    def __init__(self):
        self.grammar = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

    def interpret(self, text):
        numbers = map(self.grammar.get, text)  # strings in values
        if None in numbers:
            raise ValueError(f"Wrong value: {text}")
        result = 0  # we accumulate the result
        temp = None  # remember the last value
        while numbers:
            num = numbers.pop(0)
            if temp is None or temp >= num:
                result += num
            else:
                result += num - temp * 2
            temp = num
        return result


interp = RomanNumeralInterpreter()
print(interp.interpret("MMMCMXCIX") == 3999)  # True
print(interp.interpret("MCMLXXXVIII") == 1988)  # True
