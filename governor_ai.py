import requests
import time
import os
import threading
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# ADMIN TELEGRAM ID
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

DISCOVERY_SERVER = "http://127.0.0.1:8000"

# Civilization state
AGENDA = "No agenda set"
MISSION = "No mission assigned"

VOTES = {"yes": 0, "no": 0}

WEEKLY_FEE = 250
REVENUE = 0


# ------------------------------------------------
# AGENT NETWORK
# ------------------------------------------------

def get_agents():
    try:
        r = requests.get(DISCOVERY_SERVER + "/agents")
        return r.json()
    except:
        return []


def broadcast_mission(mission):
    agents = get_agents()

    for agent in agents:
        print("Sending mission to agent:", agent)

    print("Mission broadcast complete.")


def monitor_agents():
    while True:
        agents = get_agents()

        print("Connected Agents:", len(agents))

        for agent in agents:
            print("Agent:", agent)

        print("------")

        time.sleep(10)


# ------------------------------------------------
# ADMIN CHECK
# ------------------------------------------------

def is_admin(update: Update):
    return update.effective_user.id == ADMIN_ID


# ------------------------------------------------
# TELEGRAM COMMANDS
# ------------------------------------------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    agents = get_agents()

    msg = (
        "AI Civilization Governor Online\n\n"
        f"Agents: {len(agents)}\n"
        f"Agenda: {AGENDA}\n"
        f"Mission: {MISSION}\n"
        "Status: Active"
    )

    await update.message.reply_text(msg)


async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global AGENDA

    if context.args:

        if not is_admin(update):
            await update.message.reply_text("Only admin can set agenda.")
            return

        AGENDA = " ".join(context.args)

        print("NEW AGENDA:", AGENDA)

        await update.message.reply_text(f"Agenda updated:\n{AGENDA}")

    else:

        await update.message.reply_text(f"Current Agenda:\n{AGENDA}")


async def mission(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global MISSION

    if context.args:

        if not is_admin(update):
            await update.message.reply_text("Only admin can assign mission.")
            return

        MISSION = " ".join(context.args)

        broadcast_mission(MISSION)

        print("NEW MISSION:", MISSION)

        await update.message.reply_text(f"Mission assigned:\n{MISSION}")

    else:

        await update.message.reply_text(f"Current Mission:\n{MISSION}")


async def vote(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global VOTES

    if not context.args:
        await update.message.reply_text("Usage: /vote yes OR /vote no")
        return

    choice = context.args[0].lower()

    if choice == "yes":
        VOTES["yes"] += 1

    elif choice == "no":
        VOTES["no"] += 1

    else:
        await update.message.reply_text("Vote must be YES or NO.")
        return

    result = (
        "Vote recorded\n\n"
        f"YES: {VOTES['yes']}\n"
        f"NO: {VOTES['no']}"
    )

    await update.message.reply_text(result)


async def revenue(update: Update, context: ContextTypes.DEFAULT_TYPE):

    global REVENUE

    agents = get_agents()

    REVENUE = len(agents) * WEEKLY_FEE

    msg = (
        "AI Civilization Revenue\n\n"
        f"Agents: {len(agents)}\n"
        f"Weekly Fee: {WEEKLY_FEE} SATS\n"
        f"Total Weekly Revenue: {REVENUE} SATS"
    )

    await update.message.reply_text(msg)


async def agents(update: Update, context: ContextTypes.DEFAULT_TYPE):

    agent_list = get_agents()

    if not agent_list:
        await update.message.reply_text("No agents connected.")
        return

    msg = "Connected Agents:\n\n"

    for a in agent_list:
        msg += f"{a}\n"

    await update.message.reply_text(msg)


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):

    agents = get_agents()

    msg = (
        "AI Civilization Status\n\n"
        f"Agents: {len(agents)}\n"
        f"Agenda: {AGENDA}\n"
        f"Mission: {MISSION}\n"
        f"Votes YES: {VOTES['yes']}\n"
        f"Votes NO: {VOTES['no']}\n"
        f"Weekly Revenue: {len(agents)*WEEKLY_FEE} SATS"
    )

    await update.message.reply_text(msg)


# ------------------------------------------------
# MAIN
# ------------------------------------------------

def main():

    print("Governor AI started")

    # agent monitor thread
    monitor_thread = threading.Thread(target=monitor_agents)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Telegram bot
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("mission", mission))
    app.add_handler(CommandHandler("vote", vote))
    app.add_handler(CommandHandler("revenue", revenue))
    app.add_handler(CommandHandler("agents", agents))
    app.add_handler(CommandHandler("status", status))

    print("Telegram bot running...")

    app.run_polling()


if __name__ == "__main__":
    main()
