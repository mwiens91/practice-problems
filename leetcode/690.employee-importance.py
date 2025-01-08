# @leet start
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        # Build up a dictionary which has employee IDs as keys and
        # Employee objects as values
        employee_dict: dict[int, Employee] = {}

        for employee in employees:
            employee_dict[employee.id] = employee

        # Now find the total importance value of the employee with the
        # passed in ID
        total_importance = 0
        ids_seen: set[int] = set()
        ids_to_process_list: list[int] = [id]

        while ids_to_process_list:
            # Add employee importance to total importance and enqueue
            # subordinates
            current_id = ids_to_process_list.pop()
            current_employee = employee_dict[current_id]

            total_importance += current_employee.importance

            for subordinate_id in current_employee.subordinates:
                if subordinate_id not in ids_seen:
                    ids_to_process_list.append(subordinate_id)
                    ids_seen.add(subordinate_id)

        return total_importance


# @leet end
