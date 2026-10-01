import json
from pathlib import Path


def load_research(file_path):
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


reports_folder = Path(__file__).parent / "reports"
report_files = sorted(reports_folder.glob("research_*.json"))

if not report_files:
    print("No saved reports found. Run main.py first.")
else:
    print("Saved reports:")

    for number, file_path in enumerate(report_files, start=1):
        print(f"{number}. {file_path.name}")

    choice = input("\nEnter a report number: ").strip()

    try:
        report_number = int(choice)
    except ValueError:
        print("Please enter a whole number.")
    else:
        if 1 <= report_number <= len(report_files):
            selected_file = report_files[report_number - 1]
            research = load_research(selected_file)

            print(f"\nOpened: {selected_file.name}")
            print(f"Question: {research['question']}")
            print(f"Sources: {len(research['sources'])}")

            for source in research["sources"]:
                print(f"- {source['title']}: {source['url']}")
        else:
            print("That report number is out of range.")