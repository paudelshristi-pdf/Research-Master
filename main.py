import json
from pathlib import Path
from datetime import datetime
    
def save_research(research, file_path):
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(research, file, indent=4)

question = input("What would you like to research? ").strip()

if not question:
    print("Please enter a research question.")
else:
    print(f"\nResearch Master\nQuestion: {question}")

    sources = []

    while True:
        title = input("\nEnter a source title (or 'done'): ").strip()

        if title.lower() == "done":
            break

        url = input("Enter its URL: ").strip()

        if title and url:
            source = {
                "title": title,
                "url": url
            }

            exists = False

            for saved_source in sources:
                if saved_source["url"] == url:
                    exists = True
                    break

            if exists:
                print("This URL has already been added.")
            else:
                sources.append(source)
                print("Source added!")
        else:
            print("Both a title and a URL are required.")

    print(f"\nYou collected {len(sources)} sources.")

    for source in sources:
        print(f"- {source['title']}: {source['url']}")

    research = {
        "question": question,
        "sources": sources
    }

    reports_folder = Path(__file__).parent / "reports"
    reports_folder.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = reports_folder / f"research_{timestamp}.json"

    save_research(research, file_path)

    print(f"\nResearch saved to: {file_path.resolve()}")