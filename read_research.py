import json
from pathlib import Path


file_path = Path(__file__).parent / "research.json"

if file_path.exists():
    with file_path.open("r", encoding="utf-8") as file:
        research = json.load(file)

    print(f"Question: {research['question']}")
    print(f"Sources: {len(research['sources'])}")

    for source in research["sources"]:
        print(f"- {source['title']}: {source['url']}")
else:
    print("No saved research found. Run main.py first.")