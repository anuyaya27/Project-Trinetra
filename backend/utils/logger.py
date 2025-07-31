def log_event(event_type: str, details: str):
    with open("log.txt", "a") as log:
        log.write(f"[{event_type}] {details}\n")
