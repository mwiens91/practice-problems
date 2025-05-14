# @leet start
class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        # Sort the jobs in order of descending profit
        profit, difficulty = zip(*sorted(zip(profit, difficulty), reverse=True))

        # Sort the workers in order of descending ability
        worker.sort(reverse=True)

        # Assign to each worker the highest paying job they have the
        # ability to do
        num_jobs = len(profit)
        num_workers = len(worker)

        job_ptr = 0
        worker_ptr = 0

        max_profit = 0

        while job_ptr < num_jobs:
            while (
                worker_ptr < num_workers and worker[worker_ptr] >= difficulty[job_ptr]
            ):
                max_profit += profit[job_ptr]

                worker_ptr += 1

            job_ptr += 1

        return max_profit


# @leet end
