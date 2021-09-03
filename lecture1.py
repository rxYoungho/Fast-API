from fastapi import FastAPI, Path
from typing import Optional

# HOW TO START:  uvicorn myapi:app --reload
app = FastAPI()

students = {
    1: {
        "name": "danny",
        "age" : 17,
        "class": "year 12"
    },
    2: {
        "name": "danny",
        "age" : 22,
        "class": "year 12"
    },
    3: {
        "name": "danny",
        "age" : 24,
        "class": "year 12"
    }
}

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}")
# PATH를 통해 프론트엔드 개발자에게 코멘트를 남길 수 있음.
# PATH의 3번째 파라미터에는 gt, lt, ge, le를 통해 정수의 Limit을 정할 수 있음.
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

# get-by-name/1?name=danny&test=1 \
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id, name: Optional[str]=None, test : int): # Optional[] = None을 쓰면 Required 되지 않음
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not Found"}

#Combining PATH and QUERY Parameter -> 중괄호를 사용하여 @app.get("/{variable}")




#PATH: google.com/get-student/1 << 뒤에 있는 숫자는 유저마다 고유번호가 있을것이고 다이나믹하게 될거임 (파라미터)
#QUERY: google.com/results?search=Python
# amazon.com/create-user 
# GET - GET AN INFORMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE 
# DELETE - DELETE SOMETHING

