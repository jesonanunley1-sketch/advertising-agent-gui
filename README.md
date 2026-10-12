# Advertising Agent GUI — Draft Only

A Windows desktop GUI for the synthetic e-commerce advertising assignment.

## Start
1. Extract the ZIP.
2. Open the extracted folder in File Explorer.
3. Click the address bar, type `powershell`, and press Enter.
4. Run `py main.py`.
5. Edit the JSON in the top box and click **Run**. The JSON result appears below.

Python 3.9+ is required. Tkinter is normally included with the official Windows Python installer. No pip packages, API keys, or internet connection are needed.

## Examples
Product draft:
```json
{"customer_code":"BD-2026-10-12-13","product":"Training desk lamp","price":1325,"approved_claim":"Aluminium body"}
```
Output:
```json
{"product":"Training desk lamp","price":1325,"claim":"Aluminium body","status":"draft"}
```

Echo fixture:
```json
{"action":"echo","customer_code":"BD-13","budget":19750}
```

Experiment proposal:
```json
{"action":"experiment_plan","budget":19750,"conversion_baseline":2.3}
```

Missing facts:
```json
{}
```
returns `{"error":"missing_input"}`.

## Tests
Run `py run_tests.py`. The test runner checks five examples; expected: all five show PASS.

## Important limitations
The GUI expects structured JSON, not arbitrary natural-language instructions. It does not publish ads, spend the budget, contact customers, or alter external accounts. The experiment plan is a proposal for owner review only. Functional tests do not prove business improvement.
