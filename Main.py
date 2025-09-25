
import os
import importlib.util

while True:
    sub_files = [f for f in os.listdir() if f.startswith("Zolv") and f.endswith(".py")]

    print("\nTest case files found:")
    for i, file in enumerate(sub_files, start=1):
        print(f"\033[38;5;208m{i}. {file}\033[0m")
    print(f"\033[38;5;208m{len(sub_files)+1}. Run ALL Test Cases\033[0m")
    print(f"\033[38;5;208m{len(sub_files)+2}. Exit\033[0m")

    choice = input("\033[38;5;129mEnter the number of the test case to run: \033[0m")

    try:
        choice = int(choice)

        if 1 <= choice <= len(sub_files):
            filename = sub_files[choice - 1]
            print(f"\n🔹 Running {filename}...\n")
            spec = importlib.util.spec_from_file_location("test_module", filename)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "run_test"):
                module.run_test()

        elif choice == len(sub_files) + 1:
            for file in sub_files:
                print(f"\n🔹 Running {file}...")
                spec = importlib.util.spec_from_file_location("test_module", file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                if hasattr(module, "run_test"):
                    module.run_test()

        elif choice == len(sub_files) + 2:
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid option.")

    except ValueError:
        print("❌ Please enter a valid number.")
