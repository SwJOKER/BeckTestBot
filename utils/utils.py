def get_diagnose(points: int) -> str:
    diagnose = f'Ваш результат: {points}\n'
    if points in range(0, 10):
        diagnose += 'Депрессивные симптомы отсутствуют.'
    elif points in range(10, 16):
        diagnose += 'Легкая депрессия'
    elif points in range(15, 20):
        diagnose += 'Умеренная депрессия'
    elif points in range(20, 30):
        diagnose += 'Выраженная депрессия'
    elif points in range(30, 64):
        diagnose += 'Тяжелая депрессия'
    return diagnose