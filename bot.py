import telegram
import responses as R
import asyncio
import constants as keys
from telegram.ext import *

print("Welcome sir , i am on..")

#dispatcher = Application.builder().token(keys.API_KEY).build()



API_KEY = '6181065795:AAGcjUfkFpkzfQpzUQ0nMIr6Kb8bHVmJMns'

def start_command(update, context):
    update.message.reply_text("Welcome to the Job Search bot! How can I help you today? Type /help to know more about commands")


def help(update, context):
    update.message.reply_text(
        """
        /start -> welcome to the channel
/help -> displays the reply for each command
/job_roles -> for finding your job role

        """
    )
def job_roles(update, context):
    update.message.reply_text(
        """type /Software_Engineer for Software Engineer roles
type /web_developer for web developer roles
type /marketingmanager for marketing manager roles
type /HR for HR roles
type /Teacher for Teacher roles
type /Doctor for Doctor roles
type /Bank for Bank roles
"""
    ) 
 
def Software_Engineer(update, context):
    update.message.reply_text(
        """ Apply for software engineering role ! : https://www.linkedin.com/jobs/search/?currentJobId=3391306352&keywords=software%20engineer&refresh=true """
    )
    # Use conversation handler to handle user input and continue scheduling process



def web_developer(update, context):
    update.message.reply_text("""Apply for web developer role ! : https://www.linkedin.com/jobs/search/?currentJobId=3435932071&geoId=102713980&keywords=web%20developer&location=India&refresh=true""")

def marketingmanager(update, context):
    update.message.reply_text("""Apply for marketing manager role !: https://www.linkedin.com/jobs/search/?currentJobId=3456622170&geoId=102713980&keywords=marketing%20manager&location=India&refresh=true""")

def HR(update, context):
    update.message.reply_text("""Apply for HR  role !: https://www.linkedin.com/jobs/search/?currentJobId=3408354525&geoId=102713980&keywords=hr&location=India&refresh=true """)

def Teacher(update,context):
     update.message.reply_text("""Apply for Teacher  role !:https://www.linkedin.com/jobs/search/?currentJobId=3446742926&geoId=102713980&keywords=teacher&location=India&refresh=true """)

def Doctor(update,context):
     update.message.reply_text("""Apply for Doctor role !: https://www.linkedin.com/jobs/search/?currentJobId=3455266718&geoId=102713980&keywords=doctor&location=India&refresh=true""")

def Bank(update,context):
     update.message.reply_text("""Apply for Bank role !: https://www.linkedin.com/jobs/search/?currentJobId=3442122154&geoId=102713980&keywords=banking&location=India&refresh=true""")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)
    update.message.reply_text(response)
# Use conversation handler to handle user input and continue scheduling process
# def cancel(update, context):
#     update.message.reply_text("What date is the appointment you would like to cancel?")
#     # Use conversation handler to handle user input and continue cancelling process

def error(update, context):
    print(f"Update {update} caused error {context.error}")


# ... (import statements and other code)

def main():
    bot = telegram.Bot(token = keys.API_KEY)
    updater = Updater(bot = bot, use_context = True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('job_roles', job_roles))
    dispatcher.add_handler(CommandHandler('web_developer', web_developer))
    dispatcher.add_handler(CommandHandler('marketingmanager', marketingmanager))
    dispatcher.add_handler(CommandHandler('HR', HR))
    dispatcher.add_handler(CommandHandler('software_engineer', Software_Engineer))
    dispatcher.add_handler(CommandHandler('teacher', Teacher))
    dispatcher.add_handler(CommandHandler('doctor', Doctor))
    dispatcher.add_handler(CommandHandler('bank', Bank))

    # Only add the MessageHandler once
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
