def sliding_window(input):
  initialize window
  initialize answer

  left = 0

  for right in range(len(input)):
    append input[right] to window
    while window is not valid
      remove input[left] from window
      left += 1
    answer = max(answer, window)

  return answer
