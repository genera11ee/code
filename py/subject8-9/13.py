for i in range(5):
    current_step = str(i + 1)
    step_word = ""
    if current_step == "1":
        step_word = " step"
    else:
        step_word = " steps"
    print(current_step + step_word)
