import time
from datetime import datetime


def monitor_time(timeout_seconds: int = 30) -> None:
    """
    Monitor and display elapsed time until timeout is reached.

    Args:
        timeout_seconds: Number of seconds before the timer stops
    """
    try:
        # Initialize start time
        t0 = datetime.now()

        while True:
            current_time = datetime.now()
            elapsed_seconds = (current_time - t0).seconds

            if elapsed_seconds >= timeout_seconds:
                print(f"Timeout reached after {timeout_seconds} seconds")
                break

            print(f"Elapsed time: {elapsed_seconds} seconds")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nTimer interrupted by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    monitor_time(30)
