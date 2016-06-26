
import heapq

def merge_sorted_lists(*lists):
    merged = []
    heap = []

    # reverse each list for convenient pop()
    for mlist in lists:
        mlist.reverse()

    for idx, mlist in enumerate(lists):
        if len(mlist) > 0:
            heapq.heappush(heap, (mlist.pop(), idx))

    while len(heap) > 0:
        item, idx = heapq.heappop(heap)
        merged.append(item)
        if len(lists[idx]) > 0:
            heapq.heappush(heap, (lists[idx].pop(), idx))

    # undo reverse each list for convenient pop()
    for mlist in lists:
        mlist.reverse()

    return merged