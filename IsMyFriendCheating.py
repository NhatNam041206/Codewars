def find_smallest_multiple(number):
  """Finds the smallest multiple of a number."""
  i=2
  while number % i != 0:
    i += 1
  return i


smallest_multiple = find_smallest_multiple(5151)

print(smallest_multiple)