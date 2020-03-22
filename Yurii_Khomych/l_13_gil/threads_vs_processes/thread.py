from concurrent import futures
from concurrent.futures import ThreadPoolExecutor


def do_something(*args, **kwargs):
    """ Stub function to use with futures - your processing logic """
    print("Do something in parallel")
    return "result processed"


def main():

    # The important part - concurrent futures
    # - set number of workers as the number of jobs to process

    # The number of workers you want to run in parallel
    workers_range = 3

    with ThreadPoolExecutor(max_workers=3) as executor:
        # Use list jobs for concurrent futures
        # Use list scraped_results for results
        jobs = []
        results_done = []
        # Here you identify how many parallel tasks you want
        # and what value you'll send to them
        values = ["value1", "value2", "value3"]  # as per workers_range

        for value in values:
            # Pass some keyword arguments if needed - per job
            kw = {"some_param": value}

            # Here we iterate 'number of dates' times, could be different
            # We're adding scrape_func, could be different function per call
            jobs.append(executor.submit(do_something, **kw))

        # Once parallell processing is complete, iterate over results
        for job in futures.as_completed(jobs):
            # Read result from future
            result_done = job.result()
            # Append to the list of results
            results_done.append(result_done)

        # Iterate over results scraped and do whatever is needed
        for result in results_done:
            print("Do something with me {}".format(result))


if __name__ == "__main__":
    main()
