from code_63_unique_paths_ii import Solution

def test_example_1():
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]) == 2

def test_example_2():
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,1],[0,0]]) == 1

def test_29_failed():
    s = Solution()
    assert s.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]) == 0