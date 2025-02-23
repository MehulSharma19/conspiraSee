# agentic_mode.py
import random
import re
import time
import praw
from flask import Flask
from common import expert_selection

app = Flask(__name__)

def authenticate():
    """
    Authenticate to Reddit using credentials.
    """
    reddit = praw.Reddit(
        client_id='<client_id>',
        client_secret='<client_secret>',
        user_agent='script:ConspiraSee:v1.0 (by /u/<username>)',
        username='<username>',      
        password='<password>'      
    )
    return reddit

def contains_keywords(text):
    """
    Returns True if any of the defined keywords are present in the text.
    """
    FILTER_KEYWORDS = [
        r"\bconspiracy\b",
        r"\bconspiracy theories\b",
        r"\bmisinformation\b",
        r"\bdisinformation\b",
        r"\bcounter[- ]narratives\b",
        r"\bfake news\b",
        r"\bhoax\b",
        r"\bfalse information\b"
    ]
    FILTER_PATTERNS = [re.compile(pattern, re.IGNORECASE) for pattern in FILTER_KEYWORDS]
    return any(pattern.search(text) for pattern in FILTER_PATTERNS)

def stream_and_process(subreddit_names, classifier, model_name="mistral"):
    """
    Streams submissions from specified subreddits.
    For each submission that contains relevant keywords:
      - Classify the submission using the classifier.
      - If it's labeled as 'false rumor' (3), generate a response with a bot.
      - Post the response as a comment.
      - Exponential backoff for error handling.
    """
    reddit = authenticate()
    subreddits = '+'.join(subreddit_names)
    subreddit = reddit.subreddit(subreddits)
    print(f"Streaming submissions from: {subreddits}")

    backoff_delay = 10  # initial delay in seconds
    max_delay = 20      # maximum delay in seconds

    while True:
        try:
            for submission in subreddit.stream.submissions(skip_existing=False):
                # Combine title and selftext for classification
                text = f"{submission.title} {submission.selftext}"
                print(f"{text}\n")

                if contains_keywords(text):
                    label = classifier.classify(text)
                    print("Matched Post:")
                    print(f"Title: {submission.title}")
                    print(f"Predicted Label: {label}")
                    # Non-rumor (1): Verified, factual
                    # False rumor (3): Misinformation debunked
                    # True rumor (2): Unverified claims that turn out true
                    # Unverified rumor (0): Still uncertain

                    if label == 3:
                        # We detect 'false rumor' => generate response
                        bot = expert_selection(submission.title, submission.selftext, model_name=model_name)
                        response = bot.get_response(submission.title, submission.selftext).strip()
                        response += "\n\n*I am an automated bot aiming to help improve information quality.*"
                        print(f"Generated Response: {response}")

                        try:
                            submission.reply(response)
                            print("Comment posted successfully.")
                        except Exception as post_error:
                            print(f"Error posting comment: {post_error}")
                            time.sleep(random.uniform(5, 10))
                else:
                    print("Submission does not match keyword filter.")

            # Reset backoff delay if everything is okay
            backoff_delay = 10

        except Exception as e:
            print(f"Error encountered in stream: {e}")
            print(f"Backing off for {backoff_delay} seconds before retrying...")
            time.sleep(backoff_delay)
            backoff_delay = min(backoff_delay * 2, max_delay)


def run_agentic_mode(classifier, model_name="mistral"):
    """
    Runs the agentic mode: Streams from subreddits, uses classification + auto-bots.
    Also starts a minimal Flask server on port 5001 (if desired).
    """
    print("Running in agentic mode...")
    target_subreddits = ['conspiracy']

    # Start streaming in the background OR just do it here:
    stream_and_process(target_subreddits, classifier, model_name=model_name)

    # If you truly want a separate small Flask server for agentic mode:
    app.run(host="0.0.0.0", port=5001, debug=True)