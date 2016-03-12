"""
Given J[] jobs and 2 shops, make makespan as small as possible.

First sort jobs decreasingly.
Then assign them to 2 shops.
"""

def offline_job_shop_scheduling_heuristic(J, m=2):
    J.sort(reverse=True)
    M = [0] * 2
    for x in J:
        if M[0] < M[1]:
            M[0] += x
        else:
            M[1] += x
    return max(M)

output = '{:10}{:10}'
print(output.format('Optimal', 'Achieved'))

T1 = [1, 2, 3, 4]
ans = offline_job_shop_scheduling_heuristic(T1)
print(output.format('5', str(ans)))

T2 = [4, 2, 5, 5, 4]
ans = offline_job_shop_scheduling_heuristic(T2)
print(output.format('10', str(ans)))
