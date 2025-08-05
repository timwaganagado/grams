import csv

# 1. Design Hash Map Interface
class HashMap:
    def __init__(self, size=1000):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Simple hash function using built-in hash and modulo."""
        return hash(key) % self.size

    # 2. Implement Hash Map Accessors
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        return None

    # 3. Implement setitem
    def set(self, key, value=True):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def contains(self, key):
        return self.get(key) is not None


# 4. Read in Data, Skipping Duplicates
def remove_duplicates(input_file, output_file):
    hashmap = HashMap()
    unique_rows = []

    with open(input_file, 'r', newline='', encoding='utf-8') as f_in:
        reader = csv.DictReader(f_in)
        fieldnames = reader.fieldnames

        for row in reader:
            description = row.get("Description", "")
            if not hashmap.contains(description):
                hashmap.set(description)
                unique_rows.append(row)

    # 5. Write Results
    with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)

    print(f"{len(unique_rows)} unique rows written to {output_file}")


# Example usage (optional interactive CLI)
if __name__ == "__main__":
    input_csv = "melb_data.csv"
    output_csv = "melb_data_deduplicated.csv"
    remove_duplicates(input_csv, output_csv)
