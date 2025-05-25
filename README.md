
## 🧠 Project Description

This project models a Coffee Shop with three classes:
- `Customer`: Represents a person who buys coffee.
- `Coffee`: Represents a type of coffee sold.
- `Order`: Represents the purchase of a coffee by a customer at a given price.

### Relationships:
- A `Customer` can place many `Orders`.
- A `Coffee` can have many `Orders`.
- Each `Order` links one `Customer` to one `Coffee`.

This structure creates a many-to-many relationship between `Customer` and `Coffee` via `Order`.

## 🛠️ How to Run the Project

1. **Clone the repo**:
   git clone <your-private-repo-url>
   cd coffee_shop
2 **Set up environment** (optional):
  python3 -m venv env
  source env/bin/activate
  pip install pytest

3 **Test it manually**:
   python debug.py

4 **Run tests**:
   pytest

✅ **Features Implemented**
Attribute validation using properties

Object relationships (one-to-many, many-to-many)

Aggregation (e.g., total orders, average prices)

Class method to find the top-spending customer on a coffee

Data encapsulation and private variables

Circular import fixes with TYPE_CHECKING

🧪 **Testing**
Unit tests are stored in the tests/ directory. Each file tests the behavior and edge cases for the respective class. Use pytest to run all tests and verify functionality.

💡 Concepts Covered
OOP: Classes, instances, methods, and properties

Data validation and encapsulation

Relationships and associations

Python packaging and virtual environments

Unit testing with pytest

📚 Author
Winnie — Student Developer | Phase 3 Python | Moringa School.
