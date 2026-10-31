from src.ai.Map import Map
import json
if __name__ == '__main__':

    test_passes = 4

    # Test Case 1
    try:
        test1 = Map(goal='Indore', path=True, heurisitc=True)
        response = test1.neighbours(city='Ahmedabad')
        print(response)
        assert response['parent'] == 'Ahmedabad'
        assert list(response['neighbours']) == ['Indore', 'Surat']
        assert list(response['path_cost']) == [390, 267]
        assert response['parents_heuristic'] == 338
        assert response['heurisitc_cost'] == [0, 356]

        print("Test case 1 passed")

    except Exception as e:
        test_passes -= 1
        print("Test case 1 failed:", e)


    # Test Case 2
    try:
        test2 = Map(goal='Indore', path=True)
        response = test2.neighbours(city='Ahmedabad')
        print(response)
        assert response['parent'] == 'Ahmedabad'
        assert list(response['neighbours']) == ['Indore', 'Surat']
        assert list(response['path_cost']) == [390, 267]
        assert response['parents_heuristic'] == 338
        assert response['heurisitc_cost'] is None

        print("Test case 2 passed")

    except Exception as e:
        test_passes -= 1
        print("Test case 2 failed:", e)


    # Test Case 3
    try:
        test3 = Map(goal='Indore', heurisitc=True)
        response = test3.neighbours(city='Ahmedabad')
        print(response)
        assert response['parent'] == 'Ahmedabad'
        assert list(response['neighbours']) == ['Indore', 'Surat']
        assert response['path_cost'] is None
        assert response['parents_heuristic'] == 338
        assert response['heurisitc_cost'] == [0, 356]

        print("Test case 3 passed")

    except Exception as e:
        test_passes -= 1
        print("Test case 3 failed:", e)


    # Test Case 4
    try:
        test4 = Map(goal='Indore')
        response = test4.neighbours(city='Ahmedabad')
        print(response)
        assert response['parent'] == 'Ahmedabad'
        assert list(response['neighbours']) == ['Indore', 'Surat']
        assert response['path_cost'] is None
        assert response['heurisitc_cost'] is None

        print("Test case 4 passed")

    except Exception as e:
        test_passes -= 1
        print("Test case 4 failed:", e)


    print(f"\n{test_passes}/4 test cases passed")