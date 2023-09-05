from fastapi import FastAPI
from models import Course, session

app = FastAPI()


@app.post("/create")
async def create_course(text: str, price:int):
    course = Course(text=text, price=price)
    session.add(course)
    session.commit()
    return {"course added": course.text}

@app.get("/")
async def get_all_courses():
    courses_query = session.query(Course)
    return courses_query.all()

@app.put("/update/{id}")
async def update_course(
    id: int,
    new_text: str = "",
    updated_price: int = 0 
):
    course_query = session.query(Course).filter(Course.id==id)
    course = course_query.first()
    if new_text:
        course.text = new_text
    course.price = updated_price
    session.add(course)
    session.commit()

@app.delete("/delete/{id}")
async def delete_course(id: int):
    course = session.query(Course).filter(Course.id==id).first()
    session.delete(course)
    session.commit()
    return {"course deleted": course.text}

