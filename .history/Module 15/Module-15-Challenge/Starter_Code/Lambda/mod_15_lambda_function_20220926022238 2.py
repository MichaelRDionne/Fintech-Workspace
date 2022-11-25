### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
from botocore.vendored import requests

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }

def validate_data(age, investment_amount, risk_level):
    """
    Validates the data provided by the user.
    """

    # Validate that the user is under 65 years old
    if age is not None:
        age = parse_int(
            age
        )  # Since parameters are strings it's important to cast values
        if age > 65:
            return build_validation_result(
                False,
                "age",
                "You should be under 65 years old to use this service, "
                "please provide a different age.",
            )

    # Validate the investment amount, it should be >= 5000
    if investment_amount is not None:
        investment_amount = parse_int(
            investment_amount
        )  # Since parameters are strings it's important to cast values
        if investment_amount < 5000:
            return build_validation_result(
                False,
                "investmentAmount",
                "The amount to invest should be greater than 5000, "
                "please provide a correct amount in USD to invest.",
            )
    # Risk Level Validation
    if risk_level is not None:
        risk_level = risk_level.lower()
        if risk_level not in ["none", "low", "medium", "high"]:
            return build_validation_result(
                False,
                "riskLevel",
                "The risk level should be 'None', 'Low', 'Medium', or 'High'. "
                "Please provide a correct risk level.",
            )
          
    return build_validation_result(True, None, None)

    

### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]
      
       
    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        slots = get_slots(intent_request)

        # Get the initial validation result
        validation_result = validate_data(age, investment_amount, risk_level)

        # If the data provided is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )
        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))
     
    # Get the risk level response from the user
    risk_level = risk_level.lower()
    initial_recommendation = ""
    if risk_level == "none":
        initial_recommendation = "100% bonds (AGG), 0% equities (SPY)"
    elif risk_level == "low":
        initial_recommendation = "60% bonds (AGG), 40% equities (SPY)"

    elif risk_level == "medium":
        initial_recommendation = "40% bonds (AGG), 60% equities (SPY)"

    elif risk_level == "high":
        initial_recommendation = "20% bonds (AGG), 80% equities (SPY)"

    # Return a message with the initial recommendation based on the risk level
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "Thanks {} for your information. Based on your risk level of {}, we recommend an investment portfolio of {}".format(
                first_name, risk_level, initial_recommendation
            ),
        },
    )
    
### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "recommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
