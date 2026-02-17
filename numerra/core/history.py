from numerra.models.history_item import HistoryItem
from numerra.data.storage import push_data, show_data

class History:
  def __init__(self, max_history: int = 5, auto_save: bool = True):
    self.histories: list[HistoryItem] = []
    self.max_history = max_history
    self.auto_save = auto_save
      
  def show(self):
    print('=============== HISTORY =================')
    json_histories = show_data()
    if len(json_histories) > 0:
      for index, history in enumerate(json_histories):
        print(f"{index + 1}. {history['param1']} {history['operator']} {history['param2']} = {history['result']}")
    else:
      print("============ HISTORY KOSONG =============")
    print('=========================================')

  def add_history(self, item: HistoryItem):
    json_histories = show_data()
    self.histories = [HistoryItem(**history) for history in json_histories]
    if self.auto_save:
      if len(self.histories) >= self.max_history:
        self.histories = self.histories[-self.max_history + 1:]

      self.histories.append(item)
      push_data([history.__dict__ for history in self.histories])

  def clear(self):
    self.histories = []
    push_data([])