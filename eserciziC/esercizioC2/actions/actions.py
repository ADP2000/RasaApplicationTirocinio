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
import gtts
import os

risposte_errate = -1
fruit_list = ["banane", "mele"]
ham_list = ["salsiccia", "bistecca"]
hygiene_list = ["sapone", "bagnoschiuma"]
prodotti = """
    Banane

    Mele

    Salsiccia
      
    Bistecca
      
    Sapone
      
    Bagnoschiuma
"""
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
            text ="\n\nSono nel reparto macelleria cosa devo comprare?"
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto macelleria, cos'altro devo comprare?"
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono nel reparto igiene personale cosa devo comprare?"
        )
        return []

class ActionDomanda6ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda6"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\n\nSono ancora nel reparto di igiene personale, cos'altro devo comprare?"
        )
        return []

class ActionProdotti(Action):
    def name(self) -> Text:
        return "action_prodotti"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(
        #     text= prodotti
        # )
        tts = gtts.gTTS(prodotti, lang = "it")
        tts.save("prodotti.mp3")
        os.system("prodotti.mp3")
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

    def lista_macelleria(self) -> List:
        return ham_list

    def lista_igiene(self) -> List:
        return hygiene_list

    def validate_domanda1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global risposte_errate
        if slot_value.lower() in self.lista_frutta():
            if risposte_errate == -1:
                risposte_errate = 0
                self.lista_frutta().remove(slot_value.lower())
                dispatcher.utter_message(
                    text= "Corretto"
                )
                return{"domanda1": slot_value}
            else:
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
        
        if slot_value.lower() in self.lista_macelleria():
            self.lista_macelleria().remove(slot_value.lower())
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
        
        if slot_value.lower() in self.lista_macelleria():
            self.lista_macelleria().remove(slot_value.lower())
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
        
        if slot_value.lower() in self.lista_igiene():
            self.lista_igiene().remove(slot_value.lower())
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
        
        global risposte_errate
        if slot_value.lower() in self.lista_igiene():
            errate = risposte_errate
            self.lista_igiene().remove(slot_value.lower())
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{
                "domanda6": slot_value,
                "numero_risposte_sbagliate": errate
            }
        else:
            risposte_errate += 1
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato. Dai riprova"
            )
            return {"domanda6": None}


        
    
