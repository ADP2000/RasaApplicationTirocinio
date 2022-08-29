# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from ctypes import string_at
from pdb import Restart
from pickle import FLOAT
from random import Random, randint
from typing import Any, Text, Dict, List
from webbrowser import get

from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

# storia ="""Eccolo lì, quel vecchio gattaccio randagio. Al mattino è già lì, ronfante, al confine del minuscolo paese, sul vecchio muro che separa le case dallo strapiombo che dà alle campagne. Chissà dove dorme. Chissà dove, e soprattutto quando, mangia. Se ne sta lì tutto il giorno, eppure è rotondo. Certo è soddisfatto, come solo un gatto libero di lungo corso sa essere.

# \nPare che passi il suo tempo a guardare il cielo. Non è così. Non è proprio così. Se stiamo più attenti, ci accorgiamo che osserva una piccola nuvola. A volte è un po’ più tonda e compatta, altre più lunga e stracciata, ma è proprio sempre la stessa nuvola, ogni giorno.

# \nLa nuvola, dal canto suo, sembra proprio lusingata da tutta quell’attenzione. Proprio lei, piccola e comune tra milioni di sorelle maestose, alte nel cielo, ha trovato un pubblico così attento. Ha trovato un amico.

# \nCi fosse Rodari, saprebbe ascoltarli, e riferirci le storie meravigliose che quei due si raccontano. Ma noi, piccoli osservatori curiosi, possiamo solo guardare e, forse, immaginare.

# \nI giorni passano e passano e sembrano tutti uguali, nel sonnacchioso villaggio, mentre l’estate incurante completa il suo viaggio. Ogni giorno il gatto è lì, a guardare in alto. Anche la nuvola è lì, ogni giorno con qualcosa di nuovo per il suo amico affezionato. Una corsa su un vento fresco d’alta quota, una forma strana che forse il gatto indovinerà, un giocare a far piccolo il sole, coprendolo per un attimo. Arriva la sera e i due amici si salutano silenziosi e chissà dove vanno, a passare la notte.

# \nL’estate ha finito la sua strada. Venti freddi e mandrie di sciocche nubi basse e grigie tengono lontana la nuvola dal suo amico. Quando finalmente torna, il muretto è vuoto, il gatto non c’è. E nemmeno il giorno dopo. E nemmeno quello dopo ancora. La nuvola, che durante la loro estate l’ha sempre trovato lì, si agita, prende forme strane e nervose, si mette a cercarlo per tutta la campagna. I vecchi del paesello, osservando quella nuvola che si muove infischiandosene dei venti, scuotono la testa e annunciano tempesta.

# \nCerca e cerca, alla fine trova il suo amico. E’ lì, nella campagna, chino tra i trifogli. Se n’è andato contento e soddisfatto, come ha sempre vissuto, l’ultimo topo degli infiniti che ha acchiappato a riempirgli la pancia. Non avrebbe desiderato nulla di meglio, ma la sua amica non lo sa, nuvole e gatti non si capiscono. E lei, la nostra nuvola d’estate bianca e soffice, soffre per aver perso il suo compagno di giochi. Si gonfia e si gonfia e diventa grigia e diventa nera.

# \nL’aria si ferma, e lei si scioglie in pioggia. Piange e piange sul suo amico finché la terra si rivolta e copre entrambi, portando con sé una piccola ghianda matura.

# \nPassa l’autunno e passa l’inverno. A primavera il paese è ancora lì e sembra sempre uguale a se stesso.

# \nSe però guardiamo bene, affacciandoci da quel muro che separa il villaggio dalle campagne, vediamo una giovane quercia che cresce in fretta. Una quercia che è un po’ la nostra nuvola e un po’ il nostro libero gattone. Crescerà e crescerà e rimarrà lì per tanto tempo. Tanto tempo, come è dato solo ai frutti degli incontri più insoliti e più belli.""" 


risposte = ["muro", "estate", "chino tra i trifogli", "bianca e soffice", "dalle campagne"]

risposte_giuste = 0.0

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'iniziamo' per giocare di nuovo")
        return [Restarted()]

class ActionDomanda1ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda1"

    def risposte_domanda(self) -> List[Text]:
        return ["tetto", "muro", "finestra"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text ="\nDove si trova il gatto mentre guarda la nuvola?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda2ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda2"

    def risposte_domanda(self) -> List[Text]:
        return ["inverno", "primavera", "estate", "autunno"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "In che periodo il gatto ammira la sua amica nuvola?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda3ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda3"

    def risposte_domanda(self) -> List[Text]:
        return ["chino tra i trifogli", "disteso su un mucchio di paglia", "su un soffice e verde prato"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Quando la nuvola cerca il suo amico gatto dove si trova?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda4ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda4"

    def risposte_domanda(self) -> List[Text]:
        return ["grigia e cupa", "nera e tempestosa", "bianca e soffice"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Come si mostra la nuovola durante l'estate?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ActionDomanda5ASk(Action):
    def name(self) -> Text:
        return "action_ask_domanda5"

    def risposte_domanda(self) -> List[Text]:
        return ["dal mare", "dalle campagne", "dalle colline"]

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text = "Il muro su cui il nostro 'gattone' è solito posarsi, separa il villagio da che cosa?",
            buttons=[{"title": r, "payload": r} for r in self.risposte_domanda()]
        )
        return []

class ValidatePlayForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_play_form"

    def rispose_esatte(self) -> List[Text]:
        return risposte

    def validate_domanda1(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 

        if slot_value.lower() == self.rispose_esatte()[0]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda1": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda1": slot_value}
        
    def validate_domanda2(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[1]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda2": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda2": slot_value}
    
    def validate_domanda3(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[2]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda3": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda3": slot_value}

    def validate_domanda4(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() == self.rispose_esatte()[3]:
            global risposte_giuste
            risposte_giuste += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return{"domanda4": slot_value}
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {"domanda4": slot_value}

    def validate_domanda5(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        global risposte_giuste
        risposte = risposte_giuste
        risposte_giuste = 0.0
        if slot_value.lower() == self.rispose_esatte()[4]:
            risposte += 1
            dispatcher.utter_message(
                text= "Corretto"
            )
            return {
                "domanda5": slot_value,
                "numero_risposte_giuste": risposte,
                }
        else:
            dispatcher.utter_message(
                text= "OPS! Purtoppo hai sbagliato."
            )
            return {
                "domanda5": slot_value,
                "numero_risposte_giuste": risposte,
                }
    
