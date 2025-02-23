#!/usr/bin/env python3
import argparse
import sys
import os
from backend.conspiracy_detector import ConspiracyDetector

def main():
    parser = argparse.ArgumentParser(description="ConspiraSee app modes")
    parser.add_argument(
        "--mode",
        choices=["cli", "agentic", "web"],
        default="cli",
        help="Which mode to run: 'cli', 'agentic', or 'web'."
    )
    args, remaining_args = parser.parse_known_args()

    model_name = "mistral"
    roberta_model_path = "/Users/shridpant/Downloads/brickhacks/models/roberta/"
    classification_model = ConspiracyDetector(roberta_model_path)
    
    if args.mode == "cli":
        from cli_mode import run_cli_mode
        # Remove '--mode' and its value from sys.argv before calling CLI mode
        sys.argv = [sys.argv[0]] + remaining_args
        run_cli_mode(model_name)

    elif args.mode == "agentic":
        from agentic_mode import run_agentic_mode
        sys.argv = [sys.argv[0]] + remaining_args
        run_agentic_mode(classification_model, model_name=model_name)

    elif args.mode == "web":
        import subprocess
        subprocess.call([sys.executable, "conspirasee.py"])

if __name__ == "__main__":
    main()