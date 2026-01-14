from datetime import datetime

def run():
    message = f"App ran successfully at {datetime.now()}"
    print(message)

    with open("run.log", "a") as f:
        f.write(message + "\n")

if __name__ == "__main__":
    run()
