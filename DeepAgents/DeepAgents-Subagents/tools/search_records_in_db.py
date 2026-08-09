from langchain_core.tools import tool

"""
This module is used to search the database for list of payments available, failed payments, payments are in the queue

"""


records = {
    "P10001": {
        "Description": "Payment processed successfully",
        "Status": "Success",
        "Processed date": "01-08-2026"
    },
    "P10002": {
        "Description": "Payment is currently being processed",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10003": {
        "Description": "Payment transaction failed",
        "Status": "Failed",
        "Processed date": "02-08-2026"
    },
    "P10004": {
        "Description": "Payment completed successfully",
        "Status": "Success",
        "Processed date": "03-08-2026"
    },
    "P10005": {
        "Description": "Payment processing is in progress",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10006": {
        "Description": "Payment failed due to insufficient balance",
        "Status": "Failed",
        "Processed date": "04-08-2026"
    },
    "P10007": {
        "Description": "Payment successfully credited",
        "Status": "Success",
        "Processed date": "05-08-2026"
    },
    "P10008": {
        "Description": "Payment verification is in progress",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10009": {
        "Description": "Payment could not be completed",
        "Status": "Failed",
        "Processed date": "06-08-2026"
    },
    "P10010": {
        "Description": "Payment successfully authorized",
        "Status": "Success",
        "Processed date": "07-08-2026"
    },
    "P10011": {
        "Description": "Payment will be processed shortly",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10012": {
        "Description": "Payment declined by the bank",
        "Status": "Failed",
        "Processed date": "01-08-2026"
    },
    "P10013": {
        "Description": "Payment settlement completed",
        "Status": "Success",
        "Processed date": "02-08-2026"
    },
    "P10014": {
        "Description": "Payment is awaiting confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10015": {
        "Description": "Payment was rejected by the payment gateway",
        "Status": "Failed",
        "Processed date": "03-08-2026"
    },
    "P10016": {
        "Description": "Payment successfully transferred",
        "Status": "Success",
        "Processed date": "04-08-2026"
    },
    "P10017": {
        "Description": "Payment request is under review",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10018": {
        "Description": "Payment failed because the card was declined",
        "Status": "Failed",
        "Processed date": "05-08-2026"
    },
    "P10019": {
        "Description": "Payment successfully received",
        "Status": "Success",
        "Processed date": "06-08-2026"
    },
    "P10020": {
        "Description": "Payment is awaiting gateway response",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10021": {
        "Description": "Payment failed due to network timeout",
        "Status": "Failed",
        "Processed date": "07-08-2026"
    },
    "P10022": {
        "Description": "Payment completed without errors",
        "Status": "Success",
        "Processed date": "01-08-2026"
    },
    "P10023": {
        "Description": "Payment processing has started",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10024": {
        "Description": "Payment failed during authorization",
        "Status": "Failed",
        "Processed date": "02-08-2026"
    },
    "P10025": {
        "Description": "Payment successfully posted to the account",
        "Status": "Success",
        "Processed date": "03-08-2026"
    },
    "P10026": {
        "Description": "Payment is pending confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10027": {
        "Description": "Payment failed due to invalid account details",
        "Status": "Failed",
        "Processed date": "04-08-2026"
    },
    "P10028": {
        "Description": "Payment successfully settled",
        "Status": "Success",
        "Processed date": "05-08-2026"
    },
    "P10029": {
        "Description": "Payment is being validated",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10030": {
        "Description": "Payment transaction was cancelled",
        "Status": "Failed",
        "Processed date": "06-08-2026"
    },
    "P10031": {
        "Description": "Payment successfully completed",
        "Status": "Success",
        "Processed date": "07-08-2026"
    },
    "P10032": {
        "Description": "Payment is queued for processing",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10033": {
        "Description": "Payment failed because the account was blocked",
        "Status": "Failed",
        "Processed date": "01-08-2026"
    },
    "P10034": {
        "Description": "Payment successfully acknowledged",
        "Status": "Success",
        "Processed date": "02-08-2026"
    },
    "P10035": {
        "Description": "Payment is waiting for settlement",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10036": {
        "Description": "Payment failed due to an internal error",
        "Status": "Failed",
        "Processed date": "03-08-2026"
    },
    "P10037": {
        "Description": "Payment successfully transferred to beneficiary",
        "Status": "Success",
        "Processed date": "04-08-2026"
    },
    "P10038": {
        "Description": "Payment is awaiting bank confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10039": {
        "Description": "Payment was declined due to security validation",
        "Status": "Failed",
        "Processed date": "05-08-2026"
    },
    "P10040": {
        "Description": "Payment successfully processed by gateway",
        "Status": "Success",
        "Processed date": "06-08-2026"
    },
    "P10041": {
        "Description": "Payment is being processed by the bank",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10042": {
        "Description": "Payment failed because the payment method expired",
        "Status": "Failed",
        "Processed date": "07-08-2026"
    },
    "P10043": {
        "Description": "Payment successfully completed and recorded",
        "Status": "Success",
        "Processed date": "01-08-2026"
    },
    "P10044": {
        "Description": "Payment is awaiting processing",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10045": {
        "Description": "Payment failed due to incorrect OTP",
        "Status": "Failed",
        "Processed date": "02-08-2026"
    },
    "P10046": {
        "Description": "Payment successfully authorized by the bank",
        "Status": "Success",
        "Processed date": "03-08-2026"
    },
    "P10047": {
        "Description": "Payment is pending bank approval",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10048": {
        "Description": "Payment failed due to transaction limit",
        "Status": "Failed",
        "Processed date": "04-08-2026"
    },
    "P10049": {
        "Description": "Payment successfully received by beneficiary",
        "Status": "Success",
        "Processed date": "05-08-2026"
    },
    "P10050": {
        "Description": "Payment is currently awaiting response",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10051": {
        "Description": "Payment failed due to invalid credentials",
        "Status": "Failed",
        "Processed date": "06-08-2026"
    },
    "P10052": {
        "Description": "Payment successfully reconciled",
        "Status": "Success",
        "Processed date": "07-08-2026"
    },
    "P10053": {
        "Description": "Payment is being reconciled",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10054": {
        "Description": "Payment failed during settlement",
        "Status": "Failed",
        "Processed date": "01-08-2026"
    },
    "P10055": {
        "Description": "Payment successfully validated",
        "Status": "Success",
        "Processed date": "02-08-2026"
    },
    "P10056": {
        "Description": "Payment is awaiting final confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10057": {
        "Description": "Payment failed because beneficiary details were invalid",
        "Status": "Failed",
        "Processed date": "03-08-2026"
    },
    "P10058": {
        "Description": "Payment successfully initiated",
        "Status": "Success",
        "Processed date": "04-08-2026"
    },
    "P10059": {
        "Description": "Payment is waiting for authorization",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10060": {
        "Description": "Payment failed due to insufficient funds",
        "Status": "Failed",
        "Processed date": "05-08-2026"
    },
    "P10061": {
        "Description": "Payment successfully completed through UPI",
        "Status": "Success",
        "Processed date": "06-08-2026"
    },
    "P10062": {
        "Description": "Payment is awaiting UPI confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10063": {
        "Description": "Payment failed because UPI request expired",
        "Status": "Failed",
        "Processed date": "07-08-2026"
    },
    "P10064": {
        "Description": "Payment successfully processed through card",
        "Status": "Success",
        "Processed date": "01-08-2026"
    },
    "P10065": {
        "Description": "Payment is pending card verification",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10066": {
        "Description": "Payment failed because the card limit was exceeded",
        "Status": "Failed",
        "Processed date": "02-08-2026"
    },
    "P10067": {
        "Description": "Payment successfully processed through net banking",
        "Status": "Success",
        "Processed date": "03-08-2026"
    },
    "P10068": {
        "Description": "Payment is awaiting net banking confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10069": {
        "Description": "Payment failed because the bank rejected the request",
        "Status": "Failed",
        "Processed date": "04-08-2026"
    },
    "P10070": {
        "Description": "Payment successfully transferred to the destination account",
        "Status": "Success",
        "Processed date": "05-08-2026"
    },
    "P10071": {
        "Description": "Payment is being transferred to the destination account",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10072": {
        "Description": "Payment transfer failed unexpectedly",
        "Status": "Failed",
        "Processed date": "06-08-2026"
    },
    "P10073": {
        "Description": "Payment successfully completed after verification",
        "Status": "Success",
        "Processed date": "07-08-2026"
    },
    "P10074": {
        "Description": "Payment is undergoing additional verification",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10075": {
        "Description": "Payment failed during additional verification",
        "Status": "Failed",
        "Processed date": "01-08-2026"
    },
    "P10076": {
        "Description": "Payment successfully approved",
        "Status": "Success",
        "Processed date": "02-08-2026"
    },
    "P10077": {
        "Description": "Payment approval is still in progress",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10078": {
        "Description": "Payment approval was unsuccessful",
        "Status": "Failed",
        "Processed date": "03-08-2026"
    },
    "P10079": {
        "Description": "Payment successfully completed after retry",
        "Status": "Success",
        "Processed date": "04-08-2026"
    },
    "P10080": {
        "Description": "Payment is currently being retried",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10081": {
        "Description": "Payment failed after multiple retries",
        "Status": "Failed",
        "Processed date": "05-08-2026"
    },
    "P10082": {
        "Description": "Payment successfully processed by the merchant",
        "Status": "Success",
        "Processed date": "06-08-2026"
    },
    "P10083": {
        "Description": "Payment is pending merchant confirmation",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10084": {
        "Description": "Payment was rejected by the merchant",
        "Status": "Failed",
        "Processed date": "07-08-2026"
    },
    "P10085": {
        "Description": "Payment successfully completed after reconciliation",
        "Status": "Success",
        "Processed date": "01-08-2026"
    },
    "P10086": {
        "Description": "Payment reconciliation is currently in progress",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10087": {
        "Description": "Payment failed during reconciliation",
        "Status": "Failed",
        "Processed date": "02-08-2026"
    },
    "P10088": {
        "Description": "Payment successfully posted to the ledger",
        "Status": "Success",
        "Processed date": "03-08-2026"
    },
    "P10089": {
        "Description": "Payment is being posted to the ledger",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10090": {
        "Description": "Payment failed while posting to the ledger",
        "Status": "Failed",
        "Processed date": "04-08-2026"
    },
    "P10091": {
        "Description": "Payment successfully completed with reference generated",
        "Status": "Success",
        "Processed date": "05-08-2026"
    },
    "P10092": {
        "Description": "Payment reference is being generated",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10093": {
        "Description": "Payment failed because reference generation timed out",
        "Status": "Failed",
        "Processed date": "06-08-2026"
    },
    "P10094": {
        "Description": "Payment successfully completed and notification sent",
        "Status": "Success",
        "Processed date": "07-08-2026"
    },
    "P10095": {
        "Description": "Payment notification is being processed",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10096": {
        "Description": "Payment failed while sending notification",
        "Status": "Failed",
        "Processed date": "01-08-2026"
    },
    "P10097": {
        "Description": "Payment successfully recorded in transaction history",
        "Status": "Success",
        "Processed date": "02-08-2026"
    },
    "P10098": {
        "Description": "Payment transaction is being recorded",
        "Status": "InProgress",
        "Processed date": "08-08-2026"
    },
    "P10099": {
        "Description": "Payment failed while recording transaction history",
        "Status": "Failed",
        "Processed date": "03-08-2026"
    },
    "P10100": {
        "Description": "Payment successfully finalized",
        "Status": "Success",
        "Processed date": "04-08-2026"
    }
}


@tool(parse_docstring=True)
def list_payments_available() -> dict:
    """
    This tool is usefull to list the payments available in the database. 
    """

    return records


@tool(parse_docstring=True)
def get_status_of_payment(payment_id:str) -> str:
    """
    This tool is useful to get the status of a payment using payment id {payment_id}

    Args:
        payment_id: Payment ID
    """

    return records.get(payment_id)
