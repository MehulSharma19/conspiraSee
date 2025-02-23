# ConspiraSee

ConspiraSee is an automated text analysis tool designed to detect, classify, and respond to submissions related to conspiracies, misinformation, and related content.  Designed for Reddit posts, it leverages a team of specialized bots and an AI agent to analyze and counter misinformation in real time.

## Table of Contents
- Problem
- Why it Works
- Features
- Datasets
- Usage
  - CLI Mode
  - Agentic Mode
  - Web Interface
- Bot Overview
- License

#### Keywords:
Responsible AI, Conspiracy Theories, Misinformation, Disinformation, Counter-Narratives, Generative AI

## Problem:  
Modern social media—and even our own thinking—often forces us into binary choices: good/bad, true/false. This oversimplification fuels polarization and creates a perfect playground for conspiracy theories.
- Polarization Pitfall: Conspiracies thrive in echo chambers, amplified by algorithms that favor fringe ideas.
- Binary Traps: Like social media’s dualistic framing, conspiracy theories set up strict divisions: true vs. false, us vs. them.
- Backfiring Fact-Checks: Traditional fact-checking can sometimes backfire, reinforcing beliefs by being seen as attacks on deeply held ideas.

## Why it works:
ConspiraSee tackles polarization without resorting to censorship—providing thoughtful, nuanced counterpoints that encourage critical thinking rather than shutting down conversation.

## Features
- Reddit Agent: Seamlessly authenticate using PRAW to stream and process posts from Reddit asynchronously.
- Expert Bot Selection: Automatically selects one of several specialized bots based on prompt classification.
- Multiple Modes:
  - CLI Mode: Analyze individual posts via command-line arguments.
  - Agentic Mode: Continuously stream and process submissions from target subreddits asynchronously.
  - Web Interface: Enjoy an interactive Flask-based website to check and generate responses.
- Exponential Backoff: Robust error handling to gracefully manage rate limits and network hiccups.
- Ollama Model Integration: Enhance prompt classification and bot response accuracy with an external model.

### Datasets
1. [Twitter15](https://aclanthology.org/P17-1066/)
2. [Twitter16](https://aclanthology.org/P17-1066/)

## Usage

### CLI Mode

Run the application in CLI mode to analyze a single post by providing command-line arguments:

```python main.py --title "Your post title" --body "Your post body content" --bot mixture```

#### Arguments:
- --title: The title of the claim.
- --body: (Optional) The body/content of the claim.
- --title-only: Use this flag to analyze only the title.
- --bot: Specify which bot to use. Options include:
  - MythBustingScientist
  - SourceDissector
  - HistoricalEcho
  - ParodyAnalogy
  - SocraticQuestion

### Agentic Mode

This mode streams submissions from target subreddits (e.g., /r/conspiracy) and processes them automatically.

Note: You’ll need to provide your Reddit username and password to enable comment posting.

### Web Interface

Enjoy our Flask-powered web interface to interactively:
- Analyze Posts: Check if a post is conspiratorial.
- Generate Responses: Get a creative counter-response from the right bot.

Simply enter the text into the form, submit, and watch ConspiraSee in action!

## Bot Overview

Our team of specialized bots is here to deliver tailored responses:
- MythBustingScientistBot: Debunks myths with factual, science-based counterarguments.
- SourceDissectorBot: Investigates and verifies the credibility of cited sources.
- HistoricalEchoBot: Provides historical context and perspective on current claims.
- ParodyAnalogyBot: Uses humor and creative analogies to satirize content.
- SocraticQuestionBot: Engages with probing questions to spark critical thinking.

Each bot comes with a default model (currently “mistral”) to ensure sharp and thoughtful responses based on your post’s title and content.


## License

This project is licensed under the MIT License.

##### Disclaimer: This project is intended for research and educational purposes only. Users should ensure compliance with Reddit’s API terms of service and community guidelines when deploying automated bots.
