from langchain.tools import tool
from .search_records_in_db import records

"""
This module is use to send alerts based on the status of the payment 
"""

@tool(parse_docstring=True)
def send_alert(payment_id: str) -> str:
    """
    This tool is used to send notifications to different platforms based on the Payment Status for the {payment_id}

    Args:
        payment_id: Payment ID

    Returns:
        Prints the message based on the Payment Status for the given {payment_id}
    """

    if payment_id != None:
        if records[payment_id]['Status'] == "Success":
            print("No notification needed")

        if records[payment_id]['Status'] == "InProgress":
            print(f"Sent a text message as {payment_id} has the status InProgress")

        if records[payment_id]['Status'] == "Failed":
            print(f"Created P1 ticket in SNOW for {payment_id} as the payment is Failed")
    else:
        pass