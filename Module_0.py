
# coding: utf-8

# In[10]:


import numpy as np


# In[11]:


def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# In[12]:


def game_core_v4(number):
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 3 #перепрыгиваем сразу на 3 шага
            if number < predict: #если перепрыгнули лишнего, то по шагу возвращаемся
                predict -= 2
            elif number < predict:
                predict -= 1
        elif number < predict: 
            predict -= 3
            if number > predict:
                predict +=2
            elif number > predict:
                predict +=1
                
    return(count) # выход из цикла, если угадали


# In[13]:


score_game(game_core_v4)

