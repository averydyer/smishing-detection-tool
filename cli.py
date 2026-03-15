import json
from engine.analyzer import MessageAnalyzer


def main():
    # opening json file
    # automatically closes when block ends
    with open("data/examples.json", "r") as f:
        # messages is a list of the texts and their data
        messages = json.load(f)
        # for each message, create a message analyzer object and analyze it
        for msg in messages:
            analyzer = MessageAnalyzer(
                msg["text"], msg["unknown_contact"], msg["group_message"], msg["email"])
            analyzer.run_analysis()
            # print results of the analysis
            print_results(
                msg["text"], analyzer.get_risk_score(), analyzer.get_flags())


# prints the original message along with its risk score and flags detected
def print_results(text, risk_score, flags):
    print("\n----------------------------------")
    print(f"Text analyzed: \n{text}")
    print(f"\nRisk Score: {risk_score}")
    print("Flags: ")
    # print list of flags detected
    for flag in flags:
        print(f" - {flag}")
    print("----------------------------------")


if __name__ == "__main__":
    main()
