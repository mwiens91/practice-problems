# @leet start
class Solution:
    def hardestWorker(
        self, n: int, logs: list[list[int]]  # pylint: disable=unused-argument
    ) -> int:
        longest_time_employee_id, longest_time = logs[0]

        for (_, prev_task_end_time), (employee_id, task_end_time) in zip(
            logs, logs[1:]
        ):
            task_time = task_end_time - prev_task_end_time

            if task_time == longest_time:
                # Always choose the smallest employee id for equally
                # long tasks
                longest_time_employee_id = min(longest_time_employee_id, employee_id)
            elif task_time > longest_time:
                longest_time_employee_id = employee_id
                longest_time = task_time

        return longest_time_employee_id


# @leet end
