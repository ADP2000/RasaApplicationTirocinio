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
import pygame
from io import BytesIO
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

numeri = ["1","2","3","4","5","6"]
errori = -1

class AskForNumeroPallaAction(Action):

    def name(self) -> Text:
        return "action_ask_numero_palla"
    

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        parole = "ORSO, PELLE, PALLA, POLIPO, SOLE, ALBERO, RANA, PALLA, PINO, PALLA, PINO, PALLA"
        dispatcher.utter_message(text = "\nQuante volte ho detto la parola palla?"
        + "\nRispondi con un numero: 1,2,3...") 
        def speak(text, language = 'it'):
            mp3_fo = BytesIO()
            tts = gtts.gTTS(text,lang = language)
            tts.write_to_fp(mp3_fo)
            return mp3_fo
        pygame.mixer.init()
        sound = speak(parole)
        pygame.mixer.music.load(sound, 'mp3')
        pygame.mixer.music.play()           
        return []
    
class AskForNumeroPalla2Action(Action):

    def name(self) -> Text:
        return "action_ask_numero_palla2"
    

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        parole = "PALLA, PELLE, BOLLA, MOLLA, PALLA, BALLA, PAROLA, BALLA, PALLA, MOLLA, COLLA"
        dispatcher.utter_message(text = "\nQuante volte ho detto la parola palla?"
        + "\nRispondi con un numero: 1 palla,2 palle,3 palle...") 
        def speak(text, language = 'it'):
            mp3_fo = BytesIO()
            tts = gtts.gTTS(text,lang = language)
            tts.write_to_fp(mp3_fo)
            return mp3_fo
        pygame.mixer.init()
        sound = speak(parole)
        pygame.mixer.music.load(sound, 'mp3')
        pygame.mixer.music.play()               
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

    def db_numeri2(self) -> List[Text]:
        return ["1 palla", "2 palle", "3 palle", "4 palle", "5 palle", "6 palle"]

    def validate_numero_palla(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
 
        global errori
        if slot_value.lower() not in self.db_numeri() or slot_value.lower() != "4":
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_palla": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_palla": None}

        else:
            if errori == -1:
                errori = 0        
                dispatcher.utter_message(
                    text = "Corretto, il numero è giusto!\nOra passerai ad un livello più difficile"
                )   
                return {"numero_palla": slot_value}
            else:
                dispatcher.utter_message(
                    text = "Corretto, il numero è giusto!"
                )   
                return {"numero_palla": slot_value}
                

    def validate_numero_palla2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
 
        global errori
        if slot_value.lower() not in self.db_numeri2() or slot_value.lower() != "3 palle":
            errori += 1
            dispatcher.utter_message(text = "Purtroppo hai sbagliato\nDai riprova")
            return {"numero_palla2": None}
         
        erroriTot = errori
        dispatcher.utter_message(
            text = "Corretto, il numero è giusto!"
        )   
        return {"numero_palla2": slot_value, "numero_errori": erroriTot}

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'giochiamo' per giocare di nuovo")
        return [Restarted()]


