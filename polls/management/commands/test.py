import os
import csv
from django.core.management import BaseCommand
from polls.models import 


class Command(BaseCommand):
    """Command for importing a properly-formatted CSV file with
    customer data into the database.

    # Notes
    - Handles both creating and updating customer records.
    - Uses the file's `id` column as the `id` primary key for our database row.
    - Log messages uses stdout.

    # Expected format:
    ```csv
    id,first_name,last_name,email,gender,company,city,title
    1,Laura,Richards,lrichards0@reverbnation.com,Female,Meezzy,"Warner, NH",Biostatistician I
    ```
    """

    help = "Import customers from CSV into database. Expects one argument containing the file path."

    def add_arguments(self, parser):
        parser.add_argument('filepath', nargs='+', type=str)

    def handle(self, *args, **options):
        if not os.path.exists(options["filepath"][0]):
            self.stdout.write("you must insert a valid filepath")
            return
        self.stdout.write("Starting CSV Load...")

        with open(options["filepath"][0]) as file:
            csvreader = csv.reader(file)
            first = True
            for row in csvreader:
                if first: 
                    first = False
                    continue
                self.stdout.write(str(row))
