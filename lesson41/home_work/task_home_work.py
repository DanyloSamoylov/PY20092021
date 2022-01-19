from sqlalchemy import create_engine, Date, Numeric, Column, String, Integer, or_, text, ForeignKey,\
    Float, distinct, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, aliased


engine = create_engine('sqlite:///hr.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Countries(Base):

    __tablename__ = 'countries'

    country_id = Column(String, primary_key=True)
    country_name = Column(String, nullable=False)
    region_id = Column(Integer, nullable=False)


class Departments(Base):

    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, nullable=False)
    depart_name = Column(String, nullable=False)
    manager_id = Column(Integer, nullable=False)
    location_id = Column(Integer, nullable=True)


class Employees(Base):

    __tablename__ = 'employees'

    employee_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    hire_date = Column(Date, nullable=True)
    job_id = Column(String, nullable=False)
    salary = Column(Numeric, nullable=True)
    commission_pct = Column(Float, nullable=True)
    manager_id = Column(Integer, nullable=True)
    department_id = Column(Integer, nullable=True)
    Avg_Salary = Column(Numeric, nullable=True)


class Jobs(Base):

    __tablename__ = 'jobs'

    job_id = Column(String(10), primary_key=True, nullable=False)
    job_title = Column(String(25), nullable=False)
    min_salary = Column(Numeric, nullable=True)
    max_salary = Column(Numeric, nullable=True)


class Locations(Base):

    __tablename__ = 'locations'

    location_id = Column(Integer, primary_key=True, nullable=False)
    street_address = Column(String(25), nullable=False)
    postal_code = Column(String(12), nullable=True)
    city = Column(String(30), nullable=False)
    state_province = Column(String(12), nullable=True)
    country_id = Column(String(2), nullable=True)


def task1():
    session = Session()
    task1_ = session.query(Employees.first_name,
                           Employees.last_name,
                           Departments.department_id,
                           Departments.depart_name).\
        select_from(Employees).\
        join(Departments, Employees.department_id == Departments.department_id).all()
    session.close()
    return [data for data in task1_]


def task2():
    session = Session()
    task2_ = session.query(Employees.first_name,
                           Employees.last_name,
                           Departments.depart_name,
                           Locations.city,
                           Locations.state_province). \
        select_from(Employees). \
        join(Departments, Employees.department_id == Departments.department_id).\
        join(Locations, Departments.location_id == Locations.location_id).all()
    session.close()
    return [data for data in task2_]


def task3():
    session = Session()
    task3_ = session.query(Employees.first_name,
                           Employees.last_name,
                           Departments.department_id,
                           Departments.depart_name). \
        select_from(Employees). \
        join(Departments, Employees.department_id == Departments.department_id).\
        filter(Departments.department_id == 80 and Departments.department_id == 40).all()
    session.close()
    return [data for data in task3_]


def task4():
    session = Session()
    task4_ = session.query(distinct(Departments.depart_name)).select_from(Departments).all()
    session.close()
    return [data for data in task4_]


def task5():
    session = Session()
    task5_ = session.query(Departments.manager_id,
                           Employees.first_name,
                           Employees.employee_id).\
        select_from(Employees).\
        join(Departments, Departments.manager_id == Employees.manager_id).all()
    session.close()
    return [data for data in task5_]


def task6():
    session = Session()
    task6_ = session.query(Jobs.job_title,
                           Employees.first_name + ' ' + Employees.last_name,
                           Jobs.max_salary - Employees.salary). \
        select_from(Employees). \
        join(Jobs, Employees.job_id == Jobs.job_id).all()
    session.close()
    return [data for data in task6_]


def task7():
    session = Session()
    task7_ = session.query(Jobs.job_title,
                           func.avg(Employees.salary)).\
        select_from(Employees).\
        join(Jobs, Employees.job_id == Jobs.job_id).\
        group_by(Jobs.job_id).all()
    session.close()
    return [data for data in task7_]


def task8():
    session = Session()
    task8_ = session.query(Employees.first_name + ' ' + Employees.last_name,
                           Employees.salary,
                           Locations.city). \
        select_from(Employees). \
        join(Departments, Employees.department_id == Departments.department_id). \
        join(Locations, Departments.location_id == Locations.location_id).\
        filter(Locations.city == 'London').all()
    session.close()
    return [data for data in task8_]


def task9():
    session = Session()
    task9_ = session.query(Departments.depart_name,
                           func.count(Employees.department_id)). \
        select_from(Employees). \
        join(Departments, Employees.department_id == Departments.department_id). \
        group_by(Employees.department_id).all()
    session.close()
    return [data for data in task9_]


# print(task1())
# print(task2())
print(task3())
# print(task4())
# print(task5())
# print(task6())
# print(task7())
# print(task8())
# print(task9())
