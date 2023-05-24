import pickle
import os

def input_scores():
    scores = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        scores.append(n)
        i += 1
    return scores

def get_average(scores):
    total = 0
    for n in scores:
        total += n
    return total / len(scores)

def show_scores(scores):
    for n in scores:
        print(n, end=' ')
    print()

filename = 'score.bin' 

print('[점수 입력]')
scores = input_scores()
print('\n[점수 입력]')
print('개인 점수:', end='')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')

def save_data(scores, filepath):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            scores = pickle.load(file)
            print('[파일 읽기]')
            print('[점수 출력]')
            print('개인 점수:', end=' ')
            show_scores(scores)
            return scores
    else:
        return []

if os.path.exists(filename):
    print('[파일 읽기]')
    scores = load_data(filename)
else:
    scores = []
while True:
  if input_scores() == False :
     break

show_scores(scores)
save_data(scores, filename)