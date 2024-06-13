from emoji import emojize

def main():
    prompt = input('Input: ')
    prompt_emoji = emojize(prompt,language='alias')
    print(f'Output: {prompt_emoji}')


main()