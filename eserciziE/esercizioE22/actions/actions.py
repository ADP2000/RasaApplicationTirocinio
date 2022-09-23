# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import gtts
import os
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

storia = """C'era una volta una gara.....di ranocchi.
      L'obiettivo era arrivare in cima a una gran torre.
      Si radunò molta gente per vedere e fare il tifo per loro.
      Cominciò la gara.

      In realtà, la gente probabilmente non credeva possibile che i
      ranocchi raggiungessero la cima, e tutto quello che si ascoltava
      erano frasi tipo: "Che pena !!! Non ce la faranno mai!"

      I ranocchi cominciarono a desistere, tranne uno che continuava a  cercare di raggiungere la cima.  La gente continuava: 
      "... Che pena !!! Non ce la faranno mai!..."
      E i ranocchi si stavano dando per vinti tranne il solito ranocchio testardo che continuava ad insistere.
      Alla fine, tutti desistettero tranne quel ranocchio che, solo e con  grande sforzo, raggiunse alla fine la cima.
      Gli altri volevano sapere come avesse fatto. Uno degli altri ranocchi si avvicinò per chiedergli come avesse
      fatto a concludere la prova. Fu così che scoprirono... che era sordo !"""
errori = -1

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionNumeroAltriAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_altri"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quante volte viene ripetuta la parola 'ALTRI'?\nRispondi nel seguente modo: 1,2,3,..."
        )
        return []


class ActionStoria(Action):
    def name(self) -> Text:
        return "action_storia"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text= storia
        )
        tts = gtts.gTTS(storia, lang = "it")
        tts.save("storia.mp3")
        os.system("storia.mp3")
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

    def validate_numero_altri(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global errori
        if slot_value.lower() == "2":
            if errori == -1:
                errori = 0
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_altri": slot_value, "numero_errori": errori}
            else:
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_altri": slot_value, "numero_errori": errori}
        else:
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_altri": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_altri": None}

    