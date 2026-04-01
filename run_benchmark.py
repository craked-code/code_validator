import time
from benchmark import BENCHMARK_FUNCTIONS
from orchestrator import main

MODEL_PATH = "qwen2.5-coder:7b"
MAX_ITERATIONS = 10

def run_benchmark():
    function_names = list(BENCHMARK_FUNCTIONS.keys())
    total = len(function_names)
    conditions = ["with_coverage", "without_coverage"]

    print(f"Starting benchmark with {total} functions, 2 conditions each.")
    print(f"Total runs: {total * 2}")
    print(f"Model: {MODEL_PATH}")
    print(f"Max iterations per run: {MAX_ITERATIONS}")
    print("=" * 60)

    results = []

    for i, func_name in enumerate(function_names):
        code = BENCHMARK_FUNCTIONS[func_name]

        for condition in conditions:
            with_coverage = condition == "with_coverage"
            run_number = i * 2 + (0 if with_coverage else 1) + 1
            print(f"\n{'=' * 60}")
            print(f"Run {run_number}/{total * 2}: {func_name} | {condition}")
            print(f"{'=' * 60}")

            try:
                result = main(
                    initial_code=code,
                    model_path=MODEL_PATH,
                    function_name=func_name,
                    condition=condition,
                    with_coverage=with_coverage,
                    max_iterations=MAX_ITERATIONS
                )
                results.append({
                    "function": func_name,
                    "condition": condition,
                    "status": "completed"
                })
                print(f"\nCompleted: {func_name} | {condition}")
            except Exception as e:
                results.append({
                    "function": func_name,
                    "condition": condition,
                    "status": f"failed: {str(e)}"
                })
                print(f"\nFailed: {func_name} | {condition} | Error: {e}")

            print("Pausing 10 seconds before next run...")
            time.sleep(60)

    print(f"\n{'=' * 60}")
    print("BENCHMARK COMPLETE")
    print(f"{'=' * 60}")
    for r in results:
        status_marker = "OK" if r["status"] == "completed" else "FAIL"
        print(f"  [{status_marker}] {r['function']} | {r['condition']}")

    completed = sum(1 for r in results if r["status"] == "completed")
    print(f"\n{completed}/{len(results)} runs completed successfully.")
    print("Check experiment_logs/ folder for JSON files.")

if __name__ == "__main__":
    run_benchmark()