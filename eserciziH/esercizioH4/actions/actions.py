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

errori = -1

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
        return ["Faccio colazione", "Mi alzo dal letto","Mi vado a lavare", 
                "Mi levo il pigiama", "Sparecchio la colazione", "Mi metto i vestiti puliti", "Prendo i vestiti puliti",
                 "Mi sveglio"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nDevi prepararti per andare a lavoro la mattina.\nCosa fai per prima cosa?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionPasso2ASk(Action):
    def name(self) -> Text:
        return "action_ask_passo2"

    def risposte_domanda(self) -> List[Text]:
        return ["Faccio colazione", "Mi alzo dal letto","Mi vado a lavare", 
                "Mi levo il pigiama", "Sparecchio la colazione", "Mi metto i vestiti puliti", "Prendo i vestiti puliti",
                ]
   
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
        return ["Faccio colazione", "Mi vado a lavare", 
                "Mi levo il pigiama", "Sparecchio la colazione", "Mi metto i vestiti puliti", "Prendo i vestiti puliti",
                ]


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
        return [ "Mi vado a lavare", 
                "Mi levo il pigiama", "Sparecchio la colazione", "Mi metto i vestiti puliti", "Prendo i vestiti puliti",
                ]


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
        return [ "Mi vado a lavare", 
                "Mi levo il pigiama",  "Mi metto i vestiti puliti", "Prendo i vestiti puliti",
                ]


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
        return [ "Mi vado a lavare", 
                "Mi levo il pigiama",  "Mi metto i vestiti puliti", 
                ]

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
       return [ "Mi vado a lavare", 
                  "Mi metto i vestiti puliti", 
                ]

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
                 "Mi metto i vestiti puliti", 
                ]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nCosa fai dopo?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionFine(Action):
    def name(self) -> Text:
        return "action_fine"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        f = open("errori.txt","w")
        f.write(str(errori))
        f.close()
        dispatcher.utter_message(
            text = "Alla prossima volta",
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

        global errori
        if slot_value.lower() == "mi sveglio":
            if errori == -1:
                errori = 0
                dispatcher.utter_message(
                    text= "Corretto"
                )
                return{"passo1": slot_value}
            else:
                dispatcher.utter_message(
                    text= "Corretto"
                )
                return{"passo1": slot_value}
        else:
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"passo1": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"passo1": None}


    def validate_passo2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "mi alzo dal letto":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo2": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo2": None}

    def validate_passo3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "faccio colazione":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo3": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo3": None}

    def validate_passo4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "sparecchio la colazione":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo4": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo4": None}

    def validate_passo5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "prendo i vestiti puliti":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo5": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo5": None}

    def validate_passo6(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "mi levo il pigiama":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo6": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo6": None}
    
    def validate_passo7(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "mi vado a lavare":
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"passo7": slot_value}
        else:
            global errori
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo7": None}

    def validate_passo8(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        if slot_value.lower() == "mi metto i vestiti puliti":
            erroriTot = errori
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{
                "passo8": slot_value,
                "numero_errori": erroriTot
            }
        else:
            errori += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato.Dai riprova."
            )
            return {"passo8": None}
    
    

    
    

    


        


