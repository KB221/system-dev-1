from merge_sort import merge_sort

def test_merge_sort_sorted():
    # 给定输入：[3,1,4,1,5,9,2,6]，预期输出：[1,1,2,3,4,5,6,9]
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_merge_sort_duplicates():
    # 含重复元素：[5,3,5,1,3]，预期输出：[1,3,3,5,5]
    assert merge_sort([5, 3, 5, 1, 3]) == [1, 3, 3, 5, 5]
