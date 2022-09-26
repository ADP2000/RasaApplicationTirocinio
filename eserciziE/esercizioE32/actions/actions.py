# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import gtts
import pygame
from io import BytesIO
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

storia = """Un giorno stavo tornando a casa da scuola, quando un cavallo, che era scappato con le redini sulla groppa, 
      superò un gruppo di noi ed entrò nel campo di un contadino alla ricerca di un po’ di acqua da bere. 
      Sudava abbondantemente, e il contadino non l’aveva visto, cosicché lo catturammo noi.
      Io saltai in groppa al cavallo e, visto che aveva le briglie, presi in mano le redini e dissi:”Hop! Hop!”, 
      indirizzandolo verso la strada. Sapevo che il cavallo avrebbe girato nella direzione giusta. 
      E il cavallo si mise a trottare e a galoppare lungo la strada.
      Ogni tanto si scordava di essere sulla strada e si buttava in qualche campo, 
      allora io gli davo una scrollatina e richiamavo la sua attenzione sul fatto che era sulla strada che doveva stare.
      E alla fine, a circa 4 miglia da dove gli ero salito in groppa, si infilò nel recinto di una fattoria e il contadino disse: 
      ”Dunque è così che è tornato quello scemo. Ma dove l’hai trovato?”, e io dissi:” A circa 4 miglia da qui”.
      “E come hai fatto a sapere che dovevi venire QUI?”. ”Io non lo sapevo”, risposi “Lo sapeva il cavallo. 
      Io non ho fatto altro che mantenere la sua attenzione sulla strada”."""
errori = -1

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionNumeroGroppaAsk(Action):
    def name(self) -> Text:
        return "action_ask_numero_groppa"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "\n\nQuante volte viene ripetuta la parola 'Groppa'?\nRispondi nel seguente modo: 1,2,3,..."
        )
        return []

class ActionStoria(Action):
    def name(self) -> Text:
        return "action_storia"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text= storia
        )
        def speak(text, language = 'it'):
            mp3_fo = BytesIO()
            tts = gtts.gTTS(text,lang = language)
            tts.write_to_fp(mp3_fo)
            return mp3_fo
        pygame.mixer.init()
        sound = speak(storia)
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

    def validate_numero_groppa(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global errori
        if slot_value.lower() == "3":
            if errori == -1:
                errori = 0
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_groppa": slot_value, "numero_errori": errori}
            else:
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_groppa": slot_value, "numero_errori": errori}    
        else:
            if errori == -1:
                errori = 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_groppa": None}
            else:
                errori += 1
                dispatcher.utter_message(text = "Purtroppo hai sbagliato.\nDai riprova")
                return {"numero_groppa": None}
