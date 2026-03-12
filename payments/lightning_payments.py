from config.settings import LIGHTNING_ADDRESS,WEEKLY_FEE

def request_payment():

    print("Lightning Payment Required")

    print("Send",WEEKLY_FEE,"SATS")

    print("Lightning Address:",LIGHTNING_ADDRESS)

def confirm_payment(agent):

    print("Payment confirmed for",agent)
