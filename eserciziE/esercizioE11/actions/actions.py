# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from io import BytesIO
from typing import Any, Text, Dict, List
import gtts
import pygame
from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
storia = """"“Un giorno un lupo vide un agnello che bevevo presso un torrente e gli venne voglia di mangiarselo, ma con quale scusa? 
      Allora, standosene là a monte, cominciò ad accusarlo di sporcare l’acqua, così egli non poteva bere. 
      L’agnello gli fece notare che, per bere, sfiorava appena l’acqua col muso e che, stando a valle, non gli era possibile sporcare l’acqua che scorreva sopra di lui. 
      Ma a quel punto il lupo gli disse: “Non sei tu l’agnello che l’anno scorso ha insultato mio padre?”. 
      Ma l’agnello gli fece notare che a quella data egli non era ancora nato. “Bene”! -Concluse allora il lupo - “Se tu, caro agnello, sei così bravo a trovar delle scuse, io non posso rinunciare a mangiarti!”. 
      E se lo mangiò.” 
      La favola mostra che ci si può difendere con l’intelligenza, ma se qualcuno ha deciso di farti un torto, non c’è giusta difesa che tenga. 
      
      ESOPO."""
risposte_errori = -1

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
        f.write(str(risposte_errori))
        f.close()
        dispatcher.utter_message(
            text = "Alla prossima volta",
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

        global risposte_errori
        if slot_value.lower() == "5":
            if risposte_errori == -1:
                risposte_errori = 0
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_agnello": slot_value, "numero_errori": risposte_errori}
            else:
                dispatcher.utter_message(
                    text= "Corretto, la risposta è giusta"
                )
                return {"numero_agnello": slot_value, "numero_errori": risposte_errori}
        else:
            if risposte_errori == -1:
                risposte_errori = 1
                dispatcher.utter_message(
                    text= "OPS! Purtoppo hai sbagliato. Dai riprova."
                )
                return {"numero_agnello": None}
            else:
                risposte_errori += 1
                dispatcher.utter_message(
                    text= "OPS! Purtoppo hai sbagliato. Dai riprova."
                )
                return {"numero_agnello": None}

    
