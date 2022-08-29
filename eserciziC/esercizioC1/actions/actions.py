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

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto frutta cosa devo comprare?"
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto verdura cosa devo comprare?"
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto pasta cosa devo comprare?"
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto macelleria cosa devo comprare?"
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto panetteria cosa devo comprare?"
        )
        return []

class ActionDomanda6ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda6"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto pescheria cosa devo comprare?"
        )
        return []

class ActionDomanda7ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda7"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto latticini cosa devo comprare?"
        )
        return []

class ActionDomanda8ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda8"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto affettati cosa devo comprare?"
        )
        return []

class ActionDomanda9ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda9"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto dolci cosa devo comprare?"
        )
        return []

class ActionDomanda10ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda10"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto 'prodotti per la casa' cosa devo comprare?"
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

        if slot_value.lower() == "banane" or slot_value.lower() == "banana":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda1": slot_value}
        else:
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
        
        if slot_value.lower() == "insalata":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda2": slot_value}
        else:
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
        
        if slot_value.lower() == "pasta":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda3": slot_value}
        else:
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
        
        if slot_value.lower() == "salsiccie" or slot_value.lower() == "salsiccia":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda4": slot_value}
        else:
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
        
        global risposte_giuste
        if slot_value.lower() == "pizza":
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                }
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {
                "domanda5": slot_value,
                }
    
    def validate_domanda6(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == "gamberi":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda6": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda6": slot_value}

    def validate_domanda7(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == "formaggio" or slot_value.lower() == "formaggi":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda7": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda7": slot_value}

    def validate_domanda8(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == "prosciutto":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda8": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda8": slot_value}

    def validate_domanda9(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == "biscotti":
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda9": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda9": slot_value}

    def validate_domanda10(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global risposte_giuste
        risposte = risposte_giuste
        risposte_giuste= 0.0
        if slot_value.lower() == "ammorbidente":
            risposte +=1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{
                "domanda10": slot_value,
                "numero_risposte_giuste": risposte
            }
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return{
                "domanda10": slot_value,
                "numero_risposte_giuste": risposte
            }

        
    
