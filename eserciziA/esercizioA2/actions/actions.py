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


risposte = ["girgenti", "di piante selvatiche", "con un asino", "giugno", 
            "sono tristi ma il loro sorriso nasconde il sentimento"]

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
        return ["Girgenti", "Agrigento", "Siracusa"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nIn che città si trova la strada in cui i Tre camminano?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def risposte_domanda(self) -> List[Text]:
        return ["Di cipressi", "Di pini", "Di piante selvatiche", "Del mare"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Come dice il racconto, ogni loro passo era accompagnato da un odore, ma di cosa?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def risposte_domanda(self) -> List[Text]:
        return ["Con un cavallo", "Con un asino", "Con una mucca", "Con un cane"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nCon che animale stanno viaggiando i Tre?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def risposte_domanda(self) -> List[Text]:
        return ["Giugno", "Maggio", "Agosto", "Luglio"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nIn che mese dell'anno si trovano I tre mentre passeggiano?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def risposte_domanda(self) -> List[Text]:
        return ["Sono felici dato che sorridono", "Sono arrabiati per il troppo caldo", 
                "Sono tristi ma il loro sorriso nasconde il sentimento"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\nQuale è il vero stato d'animo dei Tre?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionFine(Action):
    def name(self) -> Text:
        return "action_fine"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        f = open("errori.txt","w")
        f.write(str(risposte_errori))
        f.close()
        dispatcher.utter_message(
            text = "Alla prossima volta",
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
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Girgenti'"
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
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Di piante selvatiche'"
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
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Con un asino'"
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
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Giugno'"
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
        if slot_value.lower() == self.rispose_esatte()[4]:
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                "numero_errori": risposte,
                }
        else:
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. La risposta giusta era 'Sono tristi ma il loro sorriso nasconde il sentimento'"
            )
            return {
                "domanda5": slot_value,
                "numero_errori": risposte_errori,
                }
    
