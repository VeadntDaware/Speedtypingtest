import time

def calculate_typing_speed(start_time, end_time, text):
    total_time = end_time - start_time
    words = text.split()
    num_words = len(words)
    typing_speed = num_words / total_time
    return typing_speed

def run_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready to start.")

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, user_input)
    print("Your typing speed is {:.2f} words per minute.".format(typing_speed * 60))

run_typing_test()
