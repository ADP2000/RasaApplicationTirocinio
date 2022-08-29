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


risposte = ["sale", "in un fiume", "delle spugne", "si gonfiano", 
            "viene trascinato via dalla corrente"]

risposte_giuste = 0.0

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
        return ["Grano","Sale", "Zucchero", "Acqua"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nChe carico sta trasportando l'asino all'inizio della storia?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def risposte_domanda(self) -> List[Text]:
        return ["Per terra", "In un fiume", "Nella paglia", "Nel mare"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Dove cade l'asino la prima volta?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def risposte_domanda(self) -> List[Text]:
        return ["Sempre il sale", "Acqua", "Delle spugne"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nCosa trasporta invece l'asino nel secondo tragitto?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def risposte_domanda(self) -> List[Text]:
        return ["Si gonfiano", "Si rimpiccioliscono", "Si sciolgono"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nCosa succede alle spugne quando l'asino si lascia cadere in acqua?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def risposte_domanda(self) -> List[Text]:
        return ["Esce dal fiume con un carico piu' pesante", 
                "Viene trascinato via dalla corrente", "Esce dal fiume senza carico di spugne"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nCosa succede all'asino subito dopo essere entrato in acqua con le spugne",
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

        if slot_value.lower() == self.rispose_esatte()[0]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda1": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Sale'"
            )
            return {"domanda1": slot_value}
        
    def validate_domanda2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[1]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda2": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'In un fiume'"
            )
            return {"domanda2": slot_value}
    
    def validate_domanda3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[2]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda3": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Delle spugne'"
            )
            return {"domanda3": slot_value}

    def validate_domanda4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[3]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda4": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Si gonfiano'"
            )
            return {"domanda4": slot_value}

    def validate_domanda5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global risposte_giuste
        risposte = risposte_giuste
        risposte_giuste = 0.0
        if slot_value.lower() == self.rispose_esatte()[4]:
            risposte += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                "numero_risposte_giuste": risposte,
                }
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Viene trascinato via dalla corrente'"
            )
            return {
                "domanda5": slot_value,
                "numero_risposte_giuste": risposte,
                }
    
