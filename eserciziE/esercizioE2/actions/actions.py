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

errori = 0.0

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionNumeroRanocchiAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_ranocchi"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola 'RANOCCHI'? \n\nRispondi nel seguente modo: 1,2,3,..."
        )
        return []


class ActionNumeroMaAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_altri"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola 'altri'? \nRispondi nel seguente modo: 1 volta,2 volte,3 volte,..."
        )
        return []


class ActionNumeroEspressioneAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_espressione"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la seguente espressione 'Che pena! Non ce la faranno mai'? \nRispondi nel seguente modo: 1 espressione,2 espressioni,3 espressioni,..."
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def validate_numero_ranocchi(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global errori
        if slot_value.lower() == "5":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_ranocchi": slot_value}
        else:
            errori += 1
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_ranocchi": None}

    def validate_numero_altri(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        if slot_value.lower() == "2 volte":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_altri": slot_value}
        else:
            errori += 1
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_altri": None}

    def validate_numero_espressione(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        global errori
        erroriTot = errori
        if slot_value.lower() == "2 espressioni":
            errori = 0.0
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
