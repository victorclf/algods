from collections import namedtuple


def overlap(intervalA, intervalB):
    return not (intervalA.end <= intervalB.start or intervalA.start >= intervalB.end)


def isIntervalBetween(interval, intervalBefore, intervalAfter):
    return not (interval.start >= intervalBefore.end and interval.end <= intervalAfter.start)


def solveUnweightedActivitySelection(activities):
    """ Choose the maximum subset of non overlapping activities. Each activity has a 'start' and 'end' time.
    Uses a greedy algorithm to achieve a linear running time.
    """
    activities.sort(key=lambda x: x.end)
    selectedActivities = []
    for a in activities:
        if not selectedActivities or a.start >= selectedActivities[-1].end:
            selectedActivities.append(a)
    return selectedActivities


if __name__ == '__main__':
    startTimes = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    endTimes = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]
    Activity = namedtuple('Activity', 'start end')
    activities = [Activity(startTimes[i], endTimes[i]) for i in range(len(startTimes))]

    print(solveUnweightedActivitySelection(activities))
