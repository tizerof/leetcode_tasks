def benchmark(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('- Время выполнения: {} секунд.'.format(end-start))
        return result
    return wrapper
