class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for number in range(1, n + 1):
          if (number % 3 == 0) and (number % 5 == 0):
            answer.append("FizzBuzz")
          elif number % 5 == 0:
            answer.append("Buzz")
          elif number % 3 == 0:
            answer.append("Fizz")
          else:
            answer.append(str(number))
        return answer
    