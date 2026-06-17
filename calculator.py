import streamlit as st
import logging
import sys
import socket
from prometheus_client import Counter, start_http_server, REGISTRY

# Metrics
try:
    CALCULATIONS_TOTAL = Counter(
        "calculator_operations_total",
        "Total calculator operations",
        ["operation"]
    )
except ValueError:
    CALCULATIONS_TOTAL = REGISTRY._names_to_collectors[
        "calculator_operations_total"
    ]

try:
    start_http_server(8000)
except OSError:
    pass

# Logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Send logs to Logstash
def send_log(message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("logstash", 5000))
        sock.sendall((message + "\n").encode("utf-8"))
        sock.close()
    except Exception as e:
        logging.error(f"Logstash connection error: {e}")

# UI
st.title("Calculator Monitoring & Logging Demo")

num1 = st.number_input("First Number", value=0.0)
num2 = st.number_input("Second Number", value=0.0)

operation = st.selectbox(
    "Operation",
    ["Add", "Subtract", "Multiply", "Divide"]
)

if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2
        op = "add"

    elif operation == "Subtract":
        result = num1 - num2
        op = "subtract"

    elif operation == "Multiply":
        result = num1 * num2
        op = "multiply"

    else:
        if num2 == 0:
            st.error("Division by zero")

            send_log(
                "ERROR | Operation=divide | Division by zero attempted"
            )

            st.stop()

        result = num1 / num2
        op = "divide"

    CALCULATIONS_TOTAL.labels(operation=op).inc()

    log_message = (
        f"Operation={op} "
        f"Num1={num1} "
        f"Num2={num2} "
        f"Result={result}"
    )

    # Send to container logs
    logging.info(log_message)

    # Send to Logstash
    send_log(log_message)

    st.success(f"Result: {result}")