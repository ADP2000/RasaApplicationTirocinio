# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from ctypes import string_at
from pdb import Restart
from random import Random, randint
from typing import Any, Text, Dict, List
import gtts
import os
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

numeri = ["1","2","3","4","5","6"]
errori = -1

class AskForNumeroAction(Action):

    def name(self) -> Text:
        return "action_ask_numero"
    

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        parole = "IMBACUCCATO, ACCUCCIATO, IMBACUCCATO, ASSONNATO, IMPACCIATO, IMBACUCCATO, IMBAMBOLATO, IMPICCATO, INSTRADATO, IMBACUCCATO, IMBRANATO, IMBACUCCATO, ANNOIATO" 
        tts = gtts.gTTS(parole, lang = "it")
        tts.save("parole.mp3")
        os.system("parole.mp3")  
        dispatcher.utter_message(text =
        "\nQuante volte ho detto la parola IMBACUCCATO?"
        + "\nRispondi con un numero: 1,2,3...")                
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

    def db_numeri(self) -> List[Text]:
        return ["1","2","3","4","5","6"]

    def lista_numeri(self) -> List[Text]:
        return numeri

    def validate_numero(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
 
        global errori
        if slot_value.lower() not in self.db_numeri() or slot_value.lower() != "5":
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero": None}

        else:
            if errori == -1:
                errori = 0
                erroriTot = errori
                dispatcher.utter_message(
                    text = "Corretto, il numero è giusto!"
                )   
                return {"numero": slot_value, "numero_errori": erroriTot}
            else:
                erroriTot = errori
                dispatcher.utter_message(
                    text = "Corretto, il numero è giusto!"
                )   
                return {"numero": slot_value, "numero_errori": erroriTot}

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'giochiamo' per giocare di nuovo")
        return [Restarted()]


