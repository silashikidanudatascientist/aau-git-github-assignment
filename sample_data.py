"""Create and display a small fictional sample dataset.

This script is for learning Python and Git/GitHub. It contains no real
patient or personal information.
"""

sample_data = [
    {"id": 1, "name": "Example A", "age": 24, "department": "Emergency"},
    {"id": 2, "name": "Example B", "age": 31, "department": "Outpatient"},
    {"id": 3, "name": "Example C", "age": 28, "department": "Medical"},
    {"id": 4, "name": "Example D", "age": 35, "department": "Pediatrics"},
    {"id": 5, "name": "Example E", "age": 42, "department": "Surgery"},
]

if __name__ == "__main__":
    print("SAMPLE DATA")
    print("-" * 48)
    print(f"{'ID':<5}{'NAME':<15}{'AGE':<8}{'DEPARTMENT'}")
    print("-" * 48)

    for record in sample_data:
        print(
            f"{record['id']:<5}"
            f"{record['name']:<15}"
            f"{record['age']:<8}"
            f"{record['department']}"
        )

    print("-" * 48)
    print(f"Total records: {len(sample_data)}")
