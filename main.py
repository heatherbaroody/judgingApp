import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.storage.jsonstore import JsonStore
#import csv
#import pandas as pd


class RiderListButton(ListItemButton):
    pass
       
#    def __init__(self, **kwargs):
#        super(CursorPosition, self).__init__(kwargs) 
#    def callprint(self):
#        print("why")
 
class JudgeBoxLayout(BoxLayout):
    
    score_input = ObjectProperty()
    bib_input = ObjectProperty()
    rider_input = ObjectProperty()
    rider_list = ObjectProperty()
    test_input = ObjectProperty()
    score_list = ObjectProperty()
    
    def add_rider(self):
        # Get the score from the TextInputs
        scoreValue = self.rider_input.text
 
        # Add the student to the ListView
        self.rider_list.adapter.data.extend([scoreValue])
 
        # Reset the ListView
        self.rider_list._trigger_reset_populate()
    
    def submit_score(self):
        # Get the score from the TextInputs
        scoreValue = "BIB: " + self.bib_input.text + "    SCORE: " + self.score_input.text
 
        # Add the student to the ListView
        self.score_list.adapter.data.extend([scoreValue])
 
        # Reset the ListView
        self.score_list._trigger_reset_populate()
    
    def add_bib(self, *args):
        # If a list item is selected
        if self.rider_list.adapter.selection:
            
            # Get the text from the item selected
            selection = self.rider_list.adapter.selection[0].text
 
            # Add to bib entry
            self.bib_input.text = selection

    def replace_score(self, *args):
 
        # If a list item is selected
        if self.rider_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.rider_list.adapter.selection[0].text
 
            # Remove the matching item
            self.rider_list.adapter.data.remove(selection)
 
            # Get the student name from the TextInputs
            scoreValue = "BIB: " + self.bib_input.text + "    SCORE: " + self.score_input.text
            
            # Add the updated data to the list
            self.rider_list.adapter.data.extend([scoreValue])
 
            # Reset the ListView
            self.rider_list._trigger_reset_populate()


    def delete_score(self):
        if self.score_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.score_list.adapter.selection[0].text
        
            # Remove the matching item
            self.score_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.score_list._trigger_reset_populate()
        if self.rider_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.rider_list.adapter.selection[0].text
 
            # Remove the matching item
            self.rider_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.rider_list._trigger_reset_populate()
    def export_list(self):
        print (self.score_list.adapter.data)
        scores = self.score_list.adapter.data
        store = JsonStore('score_data.json') 
        store.put('scores', data = scores)
#        with open('score_csv.csv', 'w', newline='') as df:
#            writer = csv.writer(df)
#            writer.writerows(data)
        
#        df = pd.DataFrame(data)
#        df.to_csv('score_csv.csv', index = False)
        

    def sort_list(self):
        self.rider_list.adapter.data.sort()
        self.rider_list._trigger_reset_populate()
        self.score_list.adapter.data.sort()
        self.score_list._trigger_reset_populate()
      
class judgeTest2App(App):
    def on_pause(self):
      # Here you can save data if needed
      return True

    def on_resume(self):
      # Here you can check if any data needs replacing (usually nothing)
      pass
  
    def build(self):
        return JudgeBoxLayout()
 
calcApp = judgeTest2App()
calcApp.run()