from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionAskOrderID(Action):
    def name(self) -> Text:
        return "action_ask_order_id"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Please provide your order ID.")
        return []

class ActionGetOrderStatus(Action):
    def name(self) -> Text:
        return "action_get_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        order_id = tracker.latest_message.get("text").split()[-1]
        dispatcher.utter_message(text=f"Your order {order_id} is on the way and will arrive in 8 minutes 🛵")
        return []

class ActionSearchProduct(Action):
    def name(self) -> Text:
        return "action_search_product"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="We have Oatly Oat Milk for €2.99 and Alpro Almond Milk for €2.49.")
        return []

class ActionReportIssue(Action):
    def name(self) -> Text:
        return "action_report_issue"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I'm sorry to hear that. A refund will be processed within 24 hours.")
        return []

class ActionShowPromotions(Action):
    def name(self) -> Text:
        return "action_show_promotions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="🎉 Today’s offer: 20% off dairy with code DAIRY20!")
        return []

class ActionHandoff(Action):
    def name(self) -> Text:
        return "action_handoff"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Connecting you to a human agent… Please wait.")
        return []
