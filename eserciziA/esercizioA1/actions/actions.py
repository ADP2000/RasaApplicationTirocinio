# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from ctypes import string_at
from pdb import Restart
from pickle import FLOAT
from random import Random, randint
from typing import Any, Text, Dict, List
from webbrowser import get

from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


risposte = ["muro", "estate", "chino tra i trifogli", "bianca e soffice", "dalle campagne"]

risposte_errori = -1

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionDomanda1ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda1"

    def risposte_domanda(self) -> List[Text]:
        return ["tetto", "muro", "finestra"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nDove si trova il gatto mentre guarda la nuvola?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def risposte_domanda(self) -> List[Text]:
        return ["inverno", "primavera", "estate", "autunno"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "In che periodo il gatto ammira la sua amica nuvola?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def risposte_domanda(self) -> List[Text]:
        return ["chino tra i trifogli", "disteso su un mucchio di paglia", "su un soffice e verde prato"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quando la nuvola cerca il suo amico gatto dove si trova?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def risposte_domanda(self) -> List[Text]:
        return ["grigia e cupa", "nera e tempestosa", "bianca e soffice"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Come si mostra la nuovola durante l'estate?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def risposte_domanda(self) -> List[Text]:
        return ["dal mare", "dalle campagne", "dalle colline"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Il muro su cui il nostro 'gattone' è solito posarsi, separa il villagio da che cosa?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def rispose_esatte(self) -> List[Text]:
        return risposte

    def validate_domanda1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global risposte_errori
        risposte_errori = 0
        if slot_value.lower() == self.rispose_esatte()[0]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda1": slot_value}
        else:
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda1": slot_value}
            
        
    def validate_domanda2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[1]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda2": slot_value}
        else:
            global risposte_errori
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda2": slot_value}
    
    def validate_domanda3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[2]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda3": slot_value}
        else:
            global risposte_errori
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda3": slot_value}

    def validate_domanda4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[3]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda4": slot_value}
        else:
            global risposte_errori
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda4": slot_value}

    def validate_domanda5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global risposte_errori
        risposte = risposte_errori
        risposte_errori = 0.0
        
        if slot_value.lower() == self.rispose_esatte()[4]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                "numero_errori": risposte,
                }
        else:
            risposte += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {
                "domanda5": slot_value,
                "numero_errori": risposte,
                }
    
