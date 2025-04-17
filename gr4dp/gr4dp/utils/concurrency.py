import concurrent.futures

def parallel_execute(func, inputs, max_workers=4):
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(func, i) for i in inputs]
        for f in futures:
            results.append(f.result())
    return results
