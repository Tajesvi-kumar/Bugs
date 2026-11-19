# AutoPatch Benchmark Test Suite (Seeded Real-World Defects)

This repository contains a curated benchmark suite of **real-world software defects** across Python and JavaScript, designed specifically for testing autonomous bug detection, Spectrum-Based Fault Localization (SBFL), Bug Reproducing Test (BRT) synthesis, and multi-phase patch verification with **[AutoPatch](http://localhost:3000/)**.

---

## Benchmark Defect Inventory

| Bug ID | Category | Target File | Target Function | Vulnerability / Defect Summary |
|---|---|---|---|---|
| **BUG-SEC-01** | Security (CWE-89) | `src/auth/service.py` | `get_user_by_token` | SQL Injection via raw formatted string in SQL query execution. |
| **BUG-NULL-01** | Null Pointer (CWE-476) | `src/auth/token_guard.py` | `extract_client_claims` | Unhandled `None` access on missing or malformed `Authorization` header. |
| **BUG-OBO-01** | Off-by-One | `src/inventory/service.py` | `reserve_stock` | Loop range `len(items) + 1` causes `IndexError` on boundary items. |
| **BUG-OBO-02** | Off-by-One | `src/pagination/helper.py` | `get_page_slice` | 1-based pagination offset omits `page - 1` shift, dropping page 1. |
| **BUG-OP-01** | Wrong Operator | `src/billing/discount.py` | `calculate_tiered_discount` | Inverted operator `<` instead of `<=` drops VIP tier discounts on threshold. |
| **BUG-CONC-01** | Concurrency | `src/payments/ledger.py` | `transfer_funds` | Unsynchronized balance mutation causing race condition double-spend. |
| **BUG-VAL-01** | Input Validation | `src/validators/user_validator.py` | `validate_username` | Accepts whitespace-only strings bypassing minimum length requirement. |
| **BUG-BOUND-01** | Boundary Check | `src/cache/lru.py` | `LRUCache.put` | Eviction guard triggers at `size > capacity + 1`, leaking cache memory. |
| **BUG-JS-01** | JavaScript Null | `src/js/router.js` | `handleRequest` | Uncaught TypeError on `undefined` header token split. |
| **BUG-JS-02** | JavaScript OBO | `src/js/csv_parser.js` | `parseCSVLine` | Off-by-one trailing delimiter slice dropping final column value. |

---

## How to Test with AutoPatch

### Option 1: Autonomous Repository Ingestion (Web Console)
1. Open the AutoPatch Console at [http://localhost:3000/app.html](http://localhost:3000/app.html) or [http://localhost:3000/](http://localhost:3000/).
2. Navigate to **Project Ingestion**.
3. In the Git Repository URL field, enter:
   ```
   https://github.com/Tajesvi-kumar/Bugs.git
   ```
4. Click **⚡ Run Autonomous Scan**.
5. Watch the **Live Pipeline Trace** as AutoPatch:
   - Constructs the NetworkX static call graph.
   - Calculates Ochiai SBFL suspiciousness coefficients.
   - Synthesizes isolated Bug Reproducing Tests (BRTs).
   - Generates minimal AST rewrite & LLM patches.
   - Verifies zero regressions in isolated Docker sandboxes.

### Option 2: Running Locally with Pytest
```bash
# Clone the benchmark suite
git clone https://github.com/Tajesvi-kumar/Bugs.git
cd Bugs

# Install test runner
pip install pytest

# Run the test suite (witness failing defect tests)
pytest tests/ -v
```

---

## Directory Structure
```
├── README.md
├── pytest.ini
├── requirements.txt
├── package.json
├── src/
│   ├── auth/           # SQLi & Null Pointer defects
│   ├── inventory/      # Off-by-one loop defects
│   ├── pagination/     # Pagination slice defects
│   ├── billing/        # Inverted operator logic
│   ├── payments/       # Concurrency ledger race conditions
│   ├── validators/     # Input sanitization bypasses
│   ├── cache/          # LRU boundary overflow
│   └── js/             # JavaScript runtime defects
└── tests/              # Comprehensive test oracles & regression suite
```

---
License: MIT
