from lib.most_often import *

# check if list comes back
def test_if_list_returns():
    most_often = MostOften(["banana"])
    assert most_often.starting_list == ["banana"]

# check if list adds something new
def test_if_list_adds_new_content():
    most_often = MostOften(["banana"])
    most_often.add_new("pear")
    assert most_often.starting_list == ["banana", "pear"]

# # check if items in list are set
# def test_if_items_are_set():
#     most_often = MostOften(["banana", "pear", "watermelon", "banana", "cucumber", "tomato"])
#     assert

# check if list returns a clear winner
def test_if_clear_winner_is_returned():
     most_often = MostOften(["banana", "pear", "watermelon", "banana", "cucumber", "tomato"])
     assert most_often.get_most_often() == "banana"
      
     
# check if list returns no clear winner
def test_if_no_clear_winner_returns():
    most_often = MostOften([1, 2, 3, 4, 5, 6])
    assert most_often.get_most_often() == "no clear winner"