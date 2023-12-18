import os
import sys
import uuid
import time
import asyncio
import requests
from dotenv import load_dotenv
from telegram.ext import filters, Application, CommandHandler, InlineQueryHandler, MessageHandler, CallbackContext
from telegram import Update, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.error import BadRequest

load_dotenv()

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

SEARCH_MOVIE = 1

async def restart(update: Update, context: CallbackContext):
    message = "🔄 Para reiniciar o bot, por favor, clique /start novamente."
    await update.message.reply_text(message)

async def tools(update: Update, context: CallbackContext):
    message = "🔎 Escolha uma ferramenta:"
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🎬 Pesquisar filmes ou séries", switch_inline_query_current_chat="")],
            [InlineKeyboardButton("👨🏻‍💻 Contato", "https://links.tifodao.com")],
        ]
    )
    await update.message.reply_text(message, reply_markup=keyboard)

async def send_info(update: Update, context: CallbackContext):
    message = "📤 Informações do desenvolvedor\n\n<b>👤 Nome</b>: Diego Melo - @tifodao\n<b>🛅 Linguagens de programação</b>: TypeScript, C#, Node.JS, PHP, Python, React.JS\n<b>🛄 Bancos de dados/servidores</b>: MySQL, Apache\n<b>🛗 Frameworks e bibliotecas</b>: Laravel, Angular.JS, Vue.JS\n\n<b>📝 Sobre mim</b>:\n\n Sou um desenvolvedor full-stack e hacker ético do Brasil com mais de uma década de experiência, especializado em desenvolvimento Web e Windows/Linux Desktop. Tenho experiência trabalhando como desenvolvedor individual e, às vezes, como cooperador de equipe em muitos projetos, proporcionando-me as habilidades de comunicação com os clientes para satisfazer suas necessidades.\n\n<i>Por curiosidade, trabalhei com diversas ferramentas para diferentes plataformas e sempre buscando aprender novas tecnologias</i>."
    await update.message.reply_text(message, parse_mode='HTML')

async def send_photo(update: Update, context: CallbackContext, photo_url: str):
    chat_id = update.message.chat_id
    await context.bot.send_photo(chat_id=chat_id, photo=photo_url)

async def inline_search_movies(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if not query:
        return
    url = f"https://api.themoviedb.org/3/search/movie"
    params = {
        'api_key': TMDB_API_KEY,
        'query': query,
        'language': 'pt-BR',
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        results = []

        for movie in data.get('results', []):
            try:
                thumb_url = f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}"
                article = InlineQueryResultArticle(
                    id=str(movie['id']),
                    title=movie['title'],
                    input_message_content=InputTextMessageContent(
                        f"{movie['id']}",
                    ),
                )
                results.append(article)
            except Exception as e:
                print(f"Erro ao criar InlineQueryResultArticle: {e}")

        await update.inline_query.answer(results, cache_time=60)
    except requests.RequestException as e:
        print(f"Erro na solicitação da API: {e}")
        await update.inline_query.answer([], cache_time=60)
    except BadRequest as e:
        if "Query is too old" not in str(e):
            raise e

async def display_movie_details(update: Update, context: CallbackContext):
    try:
        movie_id = update.message.text.split()[-1]
        movie_id = int(movie_id)
    except (ValueError, IndexError):
        await update.message.reply_text("Por favor, forneça um ID válido.")
        return

    chat_id = update.message.chat_id
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'pt-BR',
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        details = (
            f"🎬 *Título:* {data['title']}\n"
            f"📅 *Ano de lançamento:* {data['release_date'].split('-')[0]}\n\n"
            f"📖 *SINOPSE:*\n\n{data['overview']}"
        )

        photo_url = f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"

        try:
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=photo_url,
                caption=details,
                parse_mode='Markdown'
            )

            if details.strip():
                pass
            else:
                await context.bot.send_message(chat_id=chat_id, text="ℹ️ Sem informações disponíveis.")
        except BadRequest as e:
            print(f"Erro ao enviar a foto: {e}")
            await context.bot.send_message(chat_id=chat_id, text="ℹ️ Ocorreu um erro ao enviar a foto.")

        await asyncio.sleep(3)

    except requests.RequestException as e:
        print(f"Erro na solicitação da API: {e}")
        await context.bot.send_message(
            chat_id=chat_id, text="🚫 Erro ao obter detalhes do filmes ou séries.")

async def start(update: Update, context: CallbackContext):
    message = "Seja bem-vindo(a) dedicado a filmes e séries! 🍿🎬 \n\nAqui, você pode explorar e compartilhar suas recomendações favoritas. \n\nClique no botão abaixo 🎥✨"

    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🎬 Pesquisar filmes ou séries", switch_inline_query_current_chat="")]]
    )

    await update.message.reply_text(message, reply_markup=keyboard)

    instructions = "Para obter informações sobre um filme ou série, digite @ seguido pelo nome do filme ou série desejado."
    await update.message.reply_text(instructions)

if __name__ == "__main__":
    app = Application.builder().token("API_TOKEN").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tools", tools))
    app.add_handler(CommandHandler("info", send_info))
    app.add_handler(CommandHandler("restart", restart))
    app.add_handler(InlineQueryHandler(inline_search_movies))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, display_movie_details))

    app.run_polling()
