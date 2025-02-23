# cli_mode.py
import argparse
from backend.bots.MythBustingScientistBot import MythBustingScientistBot
from backend.bots.SourceDissectorBot import SourceDissectorBot
from backend.bots.HistoricalEchoBot import HistoricalEchoBot
from backend.bots.ParodyAnalogyBot import ParodyAnalogyBot
from backend.bots.SocraticQuestionBot import SocraticQuestionBot

from common import expert_selection

def run_cli_mode(model_name):
    """
    Parses command-line arguments and analyzes a claim using the selected bot.
    """
    parser = argparse.ArgumentParser(description="Analyze claims with a selected bot.")
    parser.add_argument("--title", type=str, required=True,
                        help="The title of the claim.")
    parser.add_argument("--body", type=str,
                        help="The body of the claim. If omitted and '--title-only' is used, only the title is analyzed.")
    parser.add_argument("--title-only", action="store_true",
                        help="Use only the title for analysis, ignoring the body.")
    parser.add_argument("--bot", type=str,
                        choices=[
                            "MythBustingScientist",
                            "SourceDissector",
                            "HistoricalEcho",
                            "ParodyAnalogy",
                            "SocraticQuestion",
                            "mixture"
                        ],
                        default="mixture",
                        help="Select which bot to use for the response. 'mixture' uses expert selection.")

    args = parser.parse_args()

    title = args.title
    body = "" if args.title_only else (args.body if args.body else "")

    # Bot selection logic
    if args.bot == "MythBustingScientist":
        bot = MythBustingScientistBot(model=model_name)
    elif args.bot == "SourceDissector":
        bot = SourceDissectorBot(model=model_name)
    elif args.bot == "HistoricalEcho":
        bot = HistoricalEchoBot(model=model_name)
    elif args.bot == "ParodyAnalogy":
        bot = ParodyAnalogyBot(model=model_name)
    elif args.bot == "SocraticQuestion":
        bot = SocraticQuestionBot(model=model_name)
    elif args.bot == "mixture":
        bot = expert_selection(title, body, model_name=model_name)
    else:
        bot = MythBustingScientistBot(model=model_name)

    response = bot.get_response(title, body)
    print(response.strip())