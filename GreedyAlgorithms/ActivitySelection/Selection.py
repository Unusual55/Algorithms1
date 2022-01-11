from Activity import Activity


def activity_selection(activities: list[Activity]):
    activities.sort(key=lambda x: x.e, reverse=False)
    n = len(activities)
    a = {activities[0]}
    b = 0
    for i in range(1, n):
        if activities[i].is_overlapped(activities[b]):
            a = a.union({activities[i]})
            b = i
    return a


if __name__ == '__main__':
    ac = list()
    ac.append(Activity(1, 4))
    ac.append(Activity(3, 5))
    ac.append(Activity(0, 6))
    ac.append(Activity(5, 7))
    ac.append(Activity(3, 8))
    ac.append(Activity(5, 9))
    ac.append(Activity(6, 10))
    ac.append(Activity(8, 11))
    ac.append(Activity(8, 12))
    ac.append(Activity(2, 12))
    ac.append(Activity(12, 14))
    s = activity_selection(ac)
    for activity in s:
        print(str(activity.s) + " - " + str(activity.e))
