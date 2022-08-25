from pathlib import Path

import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

SCHEMA_FILEPATH = Path(__file__).with_name('user.asvc')

# Load schema
schema = avro.schema.parse(SCHEMA_FILEPATH.open('rb').read())

# Write file
writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

# Read file
reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
