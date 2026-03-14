

class MessageAnalyzer:
    def __init__(self, text="", unknown_contact=False, group_message=False, email=False):
        # store message in all lowercase
        self.text = text.lower()
        self.unknown_contact = unknown_contact
        self.group_message = group_message
        self.email = email
        # only class methods can add flags/change risk score
        self._flags = []
        self._risk_score = 0

    def detect_urgency(self):
        urgency_keywords = ["urgent", "immediately", "asap", "act now",
                            "respond immediately", "time sensitive", "take action now", "must act now"]
        # add a flag for each time an urgency word appears in the message
        for word in urgency_keywords:
            if word in self.text:
                self.add_flag(f"urgency language: {word}", 5)

    def detect_pressure(self):
        pressure_keywords = ["limited time", "last chance", "ending soon",
                             "expires soon", "final hours", "almost gone", "while supplies last"]
        for word in pressure_keywords:
            if word in self.text:
                self.add_flag(f"pressuring language: {word}", 5)

    def detect_threat(self):
        threat_keywords = ["final notice", "legal action", "pending legal action", "account suspension", "account termination",
                           "service suspension", "failure to respond", "failure to comply", "penalty", "fine", "noncompliance", "overdue", "past due"]
        for word in threat_keywords:
            if word in self.text:
                self.add_flag(f"threatening language: {word}", 15)

    # adds flag to list of flags and increases risk score based on the specific flag
    def add_flag(self, reason, score):
        self._flags.append(reason)
        self._risk_score += score

    def get_flags(self):
        return self._flags

    def get_risk_score(self):
        return self._risk_score

    def run_analysis(self):
        self.detect_urgency()
        self.detect_pressure()
        self.detect_threat()
