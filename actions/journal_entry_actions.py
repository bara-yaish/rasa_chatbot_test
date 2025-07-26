from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher 

class ActionFindJournalEntry(Action):
    
    def name(self) -> Text:
        return "action_find_journal_entry"
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        message = """
        To find the Journal Entry screen, follow these steps:
        1. Go to the top screen and find Modules tab.
        2. Select the Financials menu.
        3. Select the Journal Entry sub-menu.
        You should be able to find them there.
        """

        dispatcher.utter_message(text=message)

        return []