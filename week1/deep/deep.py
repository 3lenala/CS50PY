# This program aims to check whether the user has the answer to the Great Question of Life or not
# The answer to the great question of life is 42

def main():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    correct_answers = {'42','forty two','forty-two'}
    answer = answer.lower().strip()
    if answer in correct_answers:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
