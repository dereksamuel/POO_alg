import random


def merge_sorting(list):
  if len(list) > 1:
    midle = len(list) // 2
    left = list[:midle]
    right = list[midle:]
    print(left, "''" * 5, right)

    # recursive callings
    merge_sorting(left)
    merge_sorting(right)

    # Iterators for each two sublists
    l = 0
    r = 0
    # Iterator for principal list
    k = 0

    while l < len(left) and r < len(right):
      if left[l] < right[r]:
        list[k] = left[l]
        l += 1
      else:
        list[r] = right[r]
        r += 1

      k += 1

    while l < len(left):
      list[k] = left[l]
      l += 1
      k += 1

    while r < len(right):
      list[k] = right[r]
      r += 1
      k += 1

    print(f"left {left}, right {right}")
    print("list", list)
    print("--------" * 10)

  return list


if __name__ == "__main__":
  list_size = int(input("What is the size of your algorythm?"))

  list = [random.randint(0, 100) for item in range(list_size)]
  print(merge_sorting(list))

