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

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nDove vagava la volpe all'inizio del racconto?\nRispondi con una singola parola (ad es. gatto,cane...).",
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Cosa vide la volpe quando i brontolii al pancino si facevano sonori?\nRispondi con una singola parola (ad es. gatto,cane...)."
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Cosa cerca di afferrare per tutta la storia la volpe?\nRispondi con una singola parola (ad es. gatto,cane...).",
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Dopo che la volpe non è riuscita a prendere l'uva come se la immagina quest'ultima?\nRispondi con una singola parola (ad es. gatto,cane...).",
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

    def validate_domanda1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global risposte_errori
        risposte_errori = 0
        if slot_value.lower() == "bosco":
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
        
        if slot_value.lower() == "vigna":
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
        
        if slot_value.lower() == "uva":
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
        
        global risposte_errori
        risposte = risposte_errori
        if slot_value.lower() == "acerba":
            
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{
                "domanda4": slot_value,
                "numero_errori": risposte
            }
        else:
            risposte_errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {
                "domanda4": slot_value,
                "numero_errori": risposte_errori
            }

    