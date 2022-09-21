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

errori = -1

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionNumeroCavalloAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_cavallo"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\n\nQuante volte viene ripetuta la parola 'Cavallo'? \n\nRispondi nel seguente modo: 1,2,3,..."
        )
        return []


class ActionNumeroGroppaAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_groppa"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola 'Groppa'? \nRispondi nel seguente modo: 1 volta,2 volte,3 volte,..."
        )
        return []


class ActionNumeroEspressioneAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_espressione"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la seguente espressione 'A circa 4 miglia'? \nRispondi nel seguente modo: 1 espressione,2 espressioni,3 espressioni,..."
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

    def validate_numero_cavallo(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global errori
        if slot_value.lower() == "5":
            if errori == -1:
                errori = 0
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_cavallo": slot_value}
            else:
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_cavallo": slot_value}    
        else:
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_cavallo": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_cavallo": None}


    def validate_numero_groppa(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        if slot_value.lower() == "3 volte":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_groppa": slot_value}
        else:
            errori += 1
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_groppa": None}

    def validate_numero_espressione(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        erroriTot = errori
        if slot_value.lower() == "2 espressioni":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_espressione": slot_value, "numero_errori": erroriTot}
        else:
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            errori += 1
            return {"numero_espressione": None}
