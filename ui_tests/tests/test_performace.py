import subprocess
import json

import pytest


@pytest.mark.performance
def test_performance():
    # Executa o Locust
    result = subprocess.run(
        ["locust", "-f", "locustfile.py", "--headless", "-u", "100", "-r", "10", "--run-time", "5s",
         "--host=http://localhost:5001"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    combined_output = result.stdout + "\n" + result.stderr

    if result.returncode != 0:
        assert False, "Locust command returned a non-zero exit code"

    # Captura a linha com as métricas desejadas
    users_line = next((line for line in combined_output.splitlines() if "GET" in line and "/users" in line), None)

    if not users_line:
        assert False, "Unable to parse Locust output"

    try:
        columns = users_line.split()
        fails = int(columns[3].split("(")[0])
        avg_resp = float(columns[5])
    except (ValueError, IndexError) as e:
        print("Error parsing metrics from Locust output")
        print("Exception:", str(e))
        assert False, "Parsing failed"

    # Resultados do teste de performance
    performance_results = {
        "average_response_time_ms": avg_resp,
        "number_of_failures": fails,
        "test_type": "performance"
    }

    # Exibe os resultados no console
    print(json.dumps(performance_results, indent=4))

    # Adiciona ou atualiza o relatório JSON
    report_data = {}
    try:
        with open("report.json", "r") as report_file:
            report_data = json.load(report_file)
    except FileNotFoundError:
        pass

    # Caso o relatório já tenha um campo “tests”, adiciona o novo teste
    if "tests" not in report_data:
        report_data["tests"] = []

    report_data["tests"].append(performance_results)

    # Salva o relatório atualizado
    with open("report.json", "w") as report_file:
        json.dump(report_data, report_file, indent=4)

    # Verifica as condições de aprovação
    assert fails == 0, f"Test failed due to {fails} failures"
    assert avg_resp <= 2000, f"Test failed due to high response time: {avg_resp}ms"