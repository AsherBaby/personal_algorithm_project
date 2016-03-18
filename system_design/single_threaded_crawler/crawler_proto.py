"""
Single thread crawler prototype
"""

list_task = 'http://stackoverflow.com/questions/tagged/python'
queue = deque()

while True:

    response = urlopen(list_task)
    page_tasks_matches = re.finditer(pattern, response.read())
    for page_task_match in page_tasks_matches:
        page_task = page_task_match.string
        if page_task not in bloomfilter:
            queue.append(page_task)

    while queue:
        page_task = queue.popleft()
        response = urlopen(page_task)
        response.read().save()  # save to db probably

    time.sleep(5*60)
