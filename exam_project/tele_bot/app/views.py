import re
import sys
import traceback

import logging
import requests
from bs4 import BeautifulSoup as bs
import datetime

from telegram import Update, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.utils.helpers import mention_html
from telegram.ext import Updater,\
    CallbackContext,\
    CommandHandler,\
    Filters,\
    MessageHandler,\
    ConversationHandler,\
    CallbackQueryHandler

from app import app, Config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

HOTEL_SEARCH = 1

"""define developer id - for traceback"""
developer_id = 532975480


def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu


def start(update: Update, context: CallbackContext):
    button_list = [
        InlineKeyboardButton('help', callback_data='help'),
        InlineKeyboardButton('Search for hotel', callback_data='hotels')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    update.message.reply_text(
        text=f'Hello, {update.effective_user.first_name}!'
             f' im your personal bot. Do you want to find a hotel?',
        reply_markup=reply_markup)


def help_menu(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""
    The following commands are available:
    
    /start -> Welcome Message
    /help -> This Message
    /hotels -> Information About hotels you search
    """)


def hotels(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Type city you want to search the hotels in.')
    return HOTEL_SEARCH


def search_hotels(update: Update, context: CallbackContext):
    if update.effective_message:
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        response = requests.get(f'https://www.hotels.com/search.do?q-destination='
                                f'{update.effective_message.text}'
                                f'&q-check-in={datetime.datetime.today().strftime("%Y-%m-%d")}'
                                f'&q-check-out={tomorrow.strftime("%Y-%m-%d")}'
                                f'&q-rooms=1&q-room-0-adults=1&q-room-0-children=0')

        html = bs(response.content, 'html.parser')
        base = html.find_all('div', class_="-RcIiD")
        if html:
            for element in base:
                hotels_data = element.find('div', class_="_3NQzWW")
                hotel_link = element.find('a', class_="_61P-R0").get('href')
                hotel_price = hotels_data.find('span', class_="_2R4dw5")
                hotel_text = hotels_data.find('div', class_="_15s9kr")
                name = hotel_text.find('h2', class_="_3zH0kn")
                address = hotel_text.find('p', class_="_2oHhXM")
                rating = hotel_text.find('span', class_="_1biq31 _2APCnh _3yXMS-")
                correct_link = re.findall('/ho[0-9]+/', hotel_link)
                button_list = []
                button_list.append(InlineKeyboardButton(name.text, callback_data=f"{correct_link[0]}"))
                reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))

                context.bot.send_message(chat_id=update.effective_chat.id, text=f"""
                Name: {name.text if name else 'No name'}
                Address: {address.text if address else 'No address'}
                Rating: {rating.text if rating else 'No rating'}
                Price:  {hotel_price.text if hotel_price else 'No price'}
                """,
                                         reply_markup=reply_markup)
                logger.info(f'Hotels list parsing. Name-{name.text if name else "No name"}')

        return HOTEL_SEARCH


def hotel_full_info(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'cancel':
        query.answer()
        return ConversationHandler.END
    else:
        query.answer()
        today = datetime.datetime.today()
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
        price_for_one = f'&q-check-in={today.strftime("%Y-%m-%d")}&q-check-out=' \
                        f'{tomorrow.strftime("%Y-%m-%d")}&q-rooms=1&q-room-0-adults=1&q-room-0-children=0'
        button_list = []
        button_list.append(InlineKeyboardButton('search one more time', callback_data="hotels"))
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'https://www.hotels.com{variant}{price_for_one}',
                                 reply_markup=reply_markup)
        return ConversationHandler.END


def button_help(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'help':
        query.answer()
    return help_menu(update, context)


def button_hotel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    return hotels(update, context)


def button_cancel(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    user = update.effective_message.from_user
    logger.info('User %s canceled the conversation.', user.first_name)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Thank you for choosing our service.')
    return ConversationHandler.END


def cancel(update: Update, context: CallbackContext):
    user = update.effective_message.from_user
    logger.info('User %s canceled the conversation.', user.first_name)
    update.effective_message.reply_text('Thank you for choosing our service.')
    return ConversationHandler.END


def unknown_message(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Sorry, I didn`t understand what you say.'
                                  'Type /help for help.')


def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Sorry, I didn`t understand that command.'
                                  'Type /help for help.')


def error(update: Update, context: CallbackContext):
    if update.effective_message:
        text = 'An error occurred while processing the message.' \
               'We are already working on the problem.'
        update.effective_message.reply_text(text)

    trace = ''.join(traceback.format_tb(sys.exc_info()[2]))
    payload = []

    if update.effective_user:
        bad_user = mention_html(update.effective_user.id, update.effective_user.first_name)
        payload.append(f'С пользователем {bad_user}')

    if update.effective_chat:
        payload.append(f' внутри чата <i>{update.effective_chat.title}</i>')
        if update.effective_chat.username:
            payload.append(f' (@{update.effective_chat.username})')

    if update.poll:
        payload.append(f' c id  опроса {update.poll.id}.')

    text = f'Ошибка <code>{context.error}</code> случилась {"".join(payload)}.' \
           f'Полная трасировка:\n\n<code>{trace}</code>'

    context.bot.send_message(developer_id, text, parse_mode=ParseMode.HTML)


@app.route('/', methods=['GET', 'POST'])
def init_bot():

    updater = Updater(token=Config.TBOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    """bot commands"""
    start_cmd = CommandHandler('start', start)
    help_cmd = CommandHandler('help', help_menu)
    cancel_cmd = CommandHandler('cancel', cancel)
    button_help_handler = CallbackQueryHandler(button_help, pattern='help')
    button_cancel_cmd = CallbackQueryHandler(button_cancel, pattern='cancel')

    """Bot conversation handler"""
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler('hotels', hotels),
            CallbackQueryHandler(button_hotel, pattern='hotels')
        ],
        states={
            HOTEL_SEARCH: [
                MessageHandler(Filters.text & (~Filters.command), search_hotels),
                CallbackQueryHandler(hotel_full_info)
            ]
        },
        fallbacks=[
            CommandHandler('cancel', cancel),
            CallbackQueryHandler(cancel, pattern='cancel')
        ]
    )
    """bot unknown message handlers"""
    unknown_message_handler = MessageHandler(Filters.text, unknown_message)
    unknown_command_handler = MessageHandler(Filters.command, unknown)

    """register in dispatcher all commands"""
    dispatcher.add_handler(start_cmd)
    dispatcher.add_handler(help_cmd)
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(button_help_handler)
    dispatcher.add_handler(button_cancel_cmd)
    dispatcher.add_handler(cancel_cmd)

    """register in dispatcher error handler"""
    dispatcher.add_error_handler(error)

    """register in dispatcher unknown command and unknown message handler"""
    dispatcher.add_handler(unknown_command_handler)
    dispatcher.add_handler(unknown_message_handler)

    """ Run bot"""
    updater.start_polling()  # timeout=15, read_latency=4
    return 'Bot started'


