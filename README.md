# Kitchen Service 

My Django project for managing a restaurant kitchen. Here, you can manage dish categories, add dishes (recipes, ingredients, prices), and keep track of chefs.

The main feature is that chefs can “assign” themselves to specific dishes (implemented via a Many-to-Many relationship).

---

## What the app can do:

- **Page protection:** Anonymous users see nothing; everything is restricted via `LoginRequiredMixin` (accessible only after logging in).
- **Home page:** Statistics on everything in the database (number of chefs, dishes, and categories).
- **Dish management:** Full CRUD.
- **List of chefs:** Database of kitchen staff.
- **Assign/Unassign button:** An interactive feature on the dish page. Log in to your account, click the button—and you’re already on the list of chefs for that dish. 
- **Pagination:** Lists are paginated with 5 items per page.

---

## Tech stack:
- Python 3
- Django
- Bootstrap 5
- SQLite

---

## How to run the project locally:

1. Clone the repository:
git clone [https://github.com/RustamHadoiev24/kitchen-service.git](https://github.com/RustamHadoiev24/kitchen-service.git)
cd kitchen-service
2. Set up a virtual environment:
python -m venv venv
venv\Scripts\activate
3. Install dependencies:
pip install -r requirements.txt
4. Run database migrations:
python manage.py migrate
5. Start the local server:
python manage.py runserver

Translated with DeepL.com (free version)