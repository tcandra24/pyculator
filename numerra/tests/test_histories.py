from numerra.core.history import History
from numerra.models.history_item import HistoryItem
from numerra.data.storage import show_data

def test_add_history():
  history = History()
  history.add_history(HistoryItem(2, 5, "+", 7))
  history.add_history(HistoryItem(10, 5, "-", 5))

  json_histories = show_data()
  assert len(json_histories) == 2
  assert json_histories[0]['param1'] == 2
  assert json_histories[0]['param2'] == 5
  assert json_histories[0]['operator'] == "+"

