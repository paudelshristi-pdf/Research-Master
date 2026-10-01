import json
from pathlib import Path


def load_research(file_path):
    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    return None


file_path = Path(__file__).parent / "research.json"
research = load_research(file_path)

if research is None:
    print("No saved research found. Run main.py first.")
else:
    print(f"Question: {research['question']}")
    print(f"Sources: {len(research['sources'])}")

    for source in research["sources"]:
        print(f"- {source['title']}: {source['url']}")
        