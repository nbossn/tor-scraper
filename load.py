from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count
from tqdm import tqdm


def threading_data(data, fn, *args, **kwargs):
    executor = ThreadPoolExecutor(max_workers=cpu_count())
    futures = [executor.submit(fn, d, *args, **kwargs) for d in data]
    results = []
    for future in tqdm(futures):
        results.append(future.result())
    return results
