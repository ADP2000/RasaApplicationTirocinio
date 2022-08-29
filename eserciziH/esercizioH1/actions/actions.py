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

errori = 0.0

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionPasso1ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo1"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta","Tolgo il filtro", "Metto l'acqua", "Rimetto il filtro",
                "Apro la macchinetta", "Accendo il fuoco","Metto caffè", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nDevi preparare la macchinetta del caffe.\nCosa fai per prima cosa?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso2ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo2"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta","Tolgo il filtro", "Metto l'acqua", "Rimetto il filtro", 
                "Accendo il fuoco","Metto caffè", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso3ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo3"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta", "Metto l'acqua", "Rimetto il filtro", 
                "Accendo il fuoco","Metto caffè", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso4ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo4"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta", "Rimetto il filtro", 
                "Accendo il fuoco","Metto caffè", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso5ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo5"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta", 
                "Accendo il fuoco","Metto caffè", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso6ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo6"

    def risposte_domanda(self) -> List[Text]:
        return ["Chiudo macchinetta", 
                "Accendo il fuoco", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso7ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo7"

    def risposte_domanda(self) -> List[Text]:
        return [ 
                "Accendo il fuoco", "Metto sui fornelli"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso8ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo8"

    def risposte_domanda(self) -> List[Text]:
        return [ 
                "Accendo il fuoco"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def validate_passo1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "apro la macchinetta":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo1": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo1": None}

    def validate_passo2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "tolgo il filtro":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo2": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo2": None}

    def validate_passo3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "metto l'acqua":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo3": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo3": None}

    def validate_passo4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "rimetto il filtro":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo4": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo4": None}

    def validate_passo5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "metto caffè":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo5": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo5": None}

    def validate_passo6(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "chiudo macchinetta":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo6": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo6": None}
    
    def validate_passo7(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "metto sui fornelli":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo7": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo7": None}

    def validate_passo8(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        errori_tot = errori
        errori = 0.0
        if slot_value.lower() == "accendo il fuoco":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo7": slot_value, "numero_errori": errori_tot}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai risprova."
            )
            return {"passo7": None}

    
    

    


        


