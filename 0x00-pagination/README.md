HYPERMEDIA PAGINATION FOR POPULAR BABAY NAMES DATASET

This project provides a Python-based server class that allows hypermedia pagination for a dataset containing popular baby names. The server class, named Server, allows users to access and paginate the dataset, ensuring a seamless experience even when rows are removed between queries.

GETTING STARTED

Clone the repository or download the provided source code files to your local machine.

Ensure you have Python 3 installed on your system.

The project relies on the csv and math modules. These are standard Python modules and do not require additional installation.

Prepare the dataset by placing it in the project directory with the name Popular_Baby_Names.csv.

Server Class

The Server class provides the following functionalities:

Pagination with get_page method: The get_page method allows users to retrieve a specific page of the dataset based on provided pagination parameters, such as the page number and page size.

Advanced Pagination with get_hyper method: The get_hyper method provides advanced pagination details for the dataset. It returns a dictionary containing the current page's details, including the current page size, data, the next page number, the previous page number, and the total number of pages.

Deletion-Resilient Pagination with get_hyper_index method: The get_hyper_index method is designed to handle deletion-resilient pagination. It returns a dictionary containing pagination details for a specific start index (0-indexed) of the dataset. It ensures that users do not miss items from the dataset when changing pages, even if certain rows have been removed between queries.

Usage

Create an instance of the Server class:

server = Server()

Use the get_page method to retrieve a specific page from the dataset:

page_number = 3
items_per_page = 10
result = server.get_page(page_number, items_per_page)
print(result)

Utilize the get_hyper method for advanced pagination details:

page_number = 3
items_per_page = 10
result = server.get_hyper(page_number, items_per_page)
print(result)

Employ the get_hyper_index method for deletion-resilient pagination:

start_index = 60
items_per_page = 20
result = server.get_hyper_index(start_index, items_per_page)
print(result)
Note: Ensure that the dataset file, Popular_Baby_Names.csv, is placed in the project directory.

Requirements

Python 3.x
csv module (standard Python module)
math module (standard Python module)

CONTRIBUTIONS

Contributions to the project are welcome! Feel free to open issues or submit pull requests.

LICENSE

This project is licensed under the MIT License - see the LICENSE file for details.

Author

[Nana Gyamera] (https://github.com/[Nanagyamera])
