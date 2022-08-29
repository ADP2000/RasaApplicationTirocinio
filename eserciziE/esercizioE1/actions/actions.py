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


class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionNumeroAgnelloAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_agnello"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola agnello? \n\nRispondi nel seguente modo: 1,2,3,..."
        )
        return []


class ActionNumeroMaAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_ma"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola 'ma'? \nRispondi nel seguente modo: 1 volta,2 volte,3 volte,..."
        )
        return []


class ActionNumeroEspressioneAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_espressione"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la seguente espressione 'gli fece notare che'? \nRispondi nel seguente modo: 1 espressione,2 espressioni,3 espressioni,..."
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def validate_numero_agnello(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "5":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_agnello": slot_value}
        else:
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_agnello": None}

    def validate_numero_ma(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "4 volte":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_ma": slot_value}
        else:
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_ma": None}

    def validate_numero_espressione(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == "2 espressioni":
            dispatcher.utter_message(
                text= "Corretto, la risposta è giusta"
            )
            return {"numero_espressione": slot_value}
        else:
            dispatcher.utter_message(
                text = "OPS! Hai sbagliato. Dai riprova"
            )
            return {"numero_espressione": None}
