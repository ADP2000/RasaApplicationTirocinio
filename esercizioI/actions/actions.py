# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionAlfabetoASk(Action):
    def name(self) -> Text:
        return "action_ask_alfabeto"

    def risposte(self) -> Text:
        return "1-A-2-B-3-C-4-D-5-E-6-F-7-G-8-H-9-I-10-J-11-K-12-L-13-M-14-N-15-O-16-P-17-Q-18-R-19-S-20-T"
        

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nPer rispondere correttamente alterna numeri e lettere nel seguente modo 1-...-2-..."
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def risposte(self) -> Text:
        return "1-A-2-B-3-C-4-D-5-E-6-F-7-G-8-H-9-I-10-J-11-K-12-L-13-M-14-N-15-O-16-P-17-Q-18-R-19-S-20-T"

    def validate_alfabeto(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        errori = 0.0
        i = 0
        stringa = self.risposte().lower()
        for c in slot_value.lower():
            if(c != stringa[i]):
                errori += 1
            i += 1

        return {
            "alfabeto": slot_value,
            "numero_errori": errori,
        }