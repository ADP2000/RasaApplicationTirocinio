# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from tkinter.messagebox import NO
from typing import Any, Text, Dict, List
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

risposte_errate = -1
fruit_list = ["fragole", "mandarini", "kiwi"]
product_list = ["senape", "maionese", "tonno"]
school_list = ["diario", "zaino", "astuccio"]

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
            text ="\n\nSono ancora nel reparto frutta, che cos'altro devo comprare?"
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto frutta, che cos'altro devo comprare?"
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto prodotti in scatola, cosa devo comprare?"
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto prodotti in scatola, che cos'altro devo comprare?"
        )
        return []

class ActionDomanda6ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda6"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto prodotti in scatola, che cos'altro devo comprare?"
        )
        return []

class ActionDomanda7ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda7"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto materiali scolastici, che cosa devo comprare?"
        )
        return []

class ActionDomanda8ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda8"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto materiali scolastici, che cos'altro devo comprare?"
        )
        return [] 

class ActionDomanda9ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda9"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto materiali scolastici, che cos'altro devo comprare?"
        )
        return []

class ActionFine(Action):
    def name(self) -> Text:
        return "action_fine"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        f = open("errori.txt","w")
        f.write(str(risposte_errate))
        f.close()
        dispatcher.utter_message(
            text = "Alla prossima volta",
        )
        return []


class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def lista_frutta(self) -> List:
        return fruit_list

    def lista_prodotti(self) -> List:
        return product_list

    def lista_scuola(self) -> List:
        return school_list

    def validate_domanda1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global risposte_errate
        if slot_value.lower() in self.lista_frutta():
            self.lista_frutta().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda1": slot_value}
        else:
            if risposte_errate == -1:
                risposte_errate = 1
                dispatcher.utter_message(
                    text= "OPS! Purtoppo hai sbagliato. Dai riprova."
                )
                return {"domanda1": None}
            else:
                risposte_errate += 1
                dispatcher.utter_message(
                    text= "OPS! Purtoppo hai sbagliato. Dai riprova."
                )
                return {"domanda1": None}
        
    def validate_domanda2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_frutta():
            self.lista_frutta().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda2": slot_value}
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova."
            )
            return {"domanda2": None}
    
    def validate_domanda3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_frutta():
            self.lista_frutta().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda3": slot_value}
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {"domanda3": None}

    def validate_domanda4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_prodotti():
            self.lista_prodotti().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda4": slot_value}
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {"domanda4": None}

    def validate_domanda5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_prodotti():
            self.lista_prodotti().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                }
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {
                "domanda5": None,
                }
    
    def validate_domanda6(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_prodotti():
            self.lista_prodotti().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda6": slot_value,
                }
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {
                "domanda6": None,
                }

    def validate_domanda7(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_scuola():
            self.lista_scuola().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda7": slot_value,
                }
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {
                "domanda7": None,
                }
    
    def validate_domanda8(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() in self.lista_scuola():
            self.lista_scuola().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda8": slot_value,
                }
        else:
            global risposte_errate
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {
                "domanda8": None,
                }

    def validate_domanda9(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global risposte_errate
        if slot_value.lower() in self.lista_scuola():
            errate = risposte_errate
            self.lista_scuola().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{
                "domanda9": slot_value,
                "numero_risposte_sbagliate": errate
            }
        else:
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {"domanda9": None}


        
    
