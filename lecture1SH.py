from fastapi import FastAPI, Path

app = FastAPI() 

# HOW TO START SERVER: uvicorn lecture1SH:app --reload

# GET - Front에서 Get 
# POST - Front가 Create 
# PUT - Front가 Update
# DELETE - Front가 Delete

# JSON
students = {
    1: {
        "name" : "danny",
        "age" : 17,
        "class" : "yesr 21"
    },
    2: {
        "name" : "john",
        "age" : 17,
        "class" : "yesr 21"
    }
}

# PATH: /
@app.get("/")
def index():
    return {"name" : "Danny"}

# ge, le, lt, gt

# PATH: google.com/get-student/1
# Query: google.com/results?search=Apple
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="기존 학생의 번호로 학생을 검색하는 API입니다.", gt=1)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(student_id, name:str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data" : "Not Found"}