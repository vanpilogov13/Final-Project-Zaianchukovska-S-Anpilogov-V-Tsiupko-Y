import csv
import curses

data_sources = []
metrics = []
print("\n" * 100)
print("Greetings! Welcome to the Operational Margin calculator v1.0")



def norm_column_name(column_name):
    if column_name is None:
        return ""
    return column_name.replace(" ", "").lower()


def add_new_data_source():
    while True:
        try:
            file_path = input("\nEnter data source: ")

            file_is_added = False
            for datasource in data_sources:
                if datasource['path'] == file_path:
                    file_is_added = True
                    break

            if file_is_added:
                print("\nFile is already added")
                continue

            file = open(file_path, 'r')
            reader = csv.reader(file)
            titles = next(reader)
            total = sum(1 for row in reader)
            file.close()

            data = {
                'name': file_path.split('/')[-1],
                'titles': [title.strip() for title in titles],
                'total': total,
                'path': file_path
            }

            data_sources.append(data)
            metrics.append(None)

            print("\n" * 100)
            print("Datasource structure:")
            print(" | ".join(data['titles']))
            print("Total records: " + str(data['total']))
            break
        except FileNotFoundError:
            print("\nFile not found")


def find_column(columns, column_name):
    normalized_name = norm_column_name(column_name)
    for column in columns:
        if norm_column_name(column) == normalized_name:
            return column
    return


def select_data_source(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    current_index = 0

    def print_menu(stdscr, current_index):
        stdscr.clear()
        stdscr.addstr(0, 0, "Select data source to calculate metric:")
        for i, source in enumerate(data_sources):
            if i == current_index:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(i + 1, 0, source['name'])
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(i + 1, 0, source['name'])
        stdscr.refresh()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    print_menu(stdscr, current_index)

    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(data_sources) - 1:
            current_index += 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            break
        print_menu(stdscr, current_index)

    return current_index


def calculate_metric():
    if not data_sources:
        print("\n" * 100)
        print("No data sources available")
        return

    selected_index = curses.wrapper(select_data_source)
    selected_data_source = data_sources[selected_index]

    file = open(selected_data_source['path'], 'r')
    reader = csv.DictReader(file)
    columns = [column.strip() for column in reader.fieldnames]

    revenue_column = find_column(columns, "revenue")
    if revenue_column:
        print("\nFound revenue column: " + revenue_column)
    else:
        while True:
            revenue_column_input = input("\nEnter the name of the revenue column: ").strip()
            revenue_column = find_column(columns, revenue_column_input)
            if revenue_column:
                print("\nFound revenue column: " + revenue_column)
                break
            else:
                print("Invalid column name. Try again!\nAvailable columns: " + ", ".join(columns))

    operating_income_column = find_column(columns, "operatingincome")
    if operating_income_column:
        print("\nFound operating income column: " + operating_income_column)
    else:
        while True:
            operating_income_column_input = input("Enter the name of the operating income column: ").strip()
            operating_income_column = find_column(columns, operating_income_column_input)
            if operating_income_column:
                print("\nFound operating income column: " + operating_income_column)
                break
            else:
                print("Invalid column name. Try again!\nAvailable columns: " + ", ".join(columns))

    total_revenue = 0
    total_operating_income = 0

    for row in reader:
        norm_row = {}
        for key, value in row.items():
            norm_key = norm_column_name(key)
            norm_row[norm_key] = value

        revenue_value = norm_row[norm_column_name(revenue_column)]
        operating_income_value = norm_row[norm_column_name(operating_income_column)]

        total_revenue += float(revenue_value.strip())
        total_operating_income += float(operating_income_value.strip())

    file.close()

    operating_margin = (total_operating_income / total_revenue) * 100
    metrics[selected_index] = operating_margin

    print("\n")
    print("Selected data source: " + selected_data_source['name'] + " | Total records: " +
          str(selected_data_source['total']))
    print("Congratulations! Your operational margin was calculated. Value is: " + str(round(operating_margin, 2)) + "%")


def check_existing_information():
    print("\n" * 100)
    if not data_sources:
        print("No data sources available.")
        return

    print("Existing Data Sources:")
    last_3_sources = data_sources[-3:]
    for i, datasource in enumerate(last_3_sources, start=1):
        metric = metrics[data_sources.index(datasource)]
        if metric is not None:
            print(str(i) + ") Datasource: " + datasource['name'] + " | Metric: Operational Margin = " +
                  str(round(metric, 2)) + "%")
        else:
            print(str(i) + ") Datasource: " + datasource['name'] + " | Metric: Not calculated")


def main_menu():
    print("\n")
    print("Select action")
    print("1. Check existing information")
    print("2. Add a new data source (file)")
    print("3. Calculate metric")
    print("4. Exit")
    action = input("Choose your action: ")
    return action


def main():
    while True:
        action = main_menu()
        if action == "1":
            check_existing_information()
        elif action == "2":
            add_new_data_source()
        elif action == "3":
            calculate_metric()
        elif action == "4":
            print("\n" * 100)
            print("Thank you for using me!")
            print("Authors: Zaianchukovska S. // Anpilogov V. // Tsiupko Y.")
            break
        else:
            print("Invalid action")


main()
