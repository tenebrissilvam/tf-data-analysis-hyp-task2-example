import pandas as pd
import numpy as np


chat_id = 227118805 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    _, p_value = stats.ks_2samp(x, y)
    return p_value < 0.05 # Ваш ответ, True или False
