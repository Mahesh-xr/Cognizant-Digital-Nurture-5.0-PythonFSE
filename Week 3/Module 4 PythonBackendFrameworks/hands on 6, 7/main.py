from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, status, BackgroundTasks, Response
from fastapi.concurrency import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, init_db
from models import Course, Enrollment, Student
from schemas import CourseCreate, CourseResponse, CourseUpdate, StudentResponse, StudentCreate, StudentUpdate, EnrollmentResponse, EnrollmentCreate, EnrollmentUpdate


app = FastAPI(
    title="Course Management API",
    description="""
A REST API for managing departments, courses,
students, and enrollments using FastAPI.
""",
    version="1.0.0",
    contact={
        "name": "Maheshkumar K",
        "email": "mahesh@example.com",
    },
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


@app.get("/")
async def root():
    return {
        "message": "API running",
    }


@app.get("/api/courses/", response_model=list[CourseResponse], status_code=status.HTTP_200_OK, tags=["Courses"], summary="Get all courses",
    response_description="List of courses",
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Course)

    if department_id is not None:
        query = query.where(
            Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    courses = result.scalars().all()

    return courses


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    status_code=status.HTTP_200_OK,
    tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
         raise HTTPException(
             status_code=404,
             detail="Course not found"
            )

    return course


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"]
   
)
async def create_course(
    course: CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id,
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    response.headers["Location"] = f"/api/courses/{new_course.id}/"
    return new_course



@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    status_code=status.HTTP_200_OK,
    tags=["Courses"]
)
async def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
         raise HTTPException(
             status_code=404,
             detail="Course not found"
            )

    if course_data.name is not None:
        course.name = course_data.name

    if course_data.code is not None:
        course.code = course_data.code

    if course_data.credits is not None:
        course.credits = course_data.credits

    if course_data.department_id is not None:
        course.department_id = course_data.department_id

    await db.commit()

    await db.refresh(course)

    return course


@app.delete("/api/courses/{course_id}", tags=["Courses"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
         raise HTTPException(
             status_code=404,
             detail="Course not found"
            )

    await db.delete(course)

    await db.commit()

    return


@app.get("/api/courses/{course_id}/students/", tags=["Courses"])
async def get_course_students(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student)
        .join(Enrollment)
        .where(Enrollment.course_id == course_id)
    )

    students = result.scalars().all()

    return students


# ==============================
# Student CRUD
# ==============================

@app.get(
    "/api/students/",
    response_model=list[StudentResponse],
    status_code=status.HTTP_200_OK,
    tags=["Students"]
)
async def get_students(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Student)

    if department_id is not None:
        query = query.where(
            Student.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    students = result.scalars().all()

    return students


@app.get(
    "/api/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Students"]
)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    new_student = Student(
        first_name=student.first_name,
        last_name=student.last_name,
        email=student.email,
        enrollment_year=student.enrollment_year,
        department_id=student.department_id,
    )

    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)

    return new_student


@app.put(
    "/api/students/{student_id}",
    response_model=StudentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Students"]
)
async def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    if student_data.first_name is not None:
        student.first_name = student_data.first_name

    if student_data.last_name is not None:
        student.last_name = student_data.last_name

    if student_data.email is not None:
        student.email = student_data.email

    if student_data.enrollment_year is not None:
        student.enrollment_year = student_data.enrollment_year

    if student_data.department_id is not None:
        student.department_id = student_data.department_id

    await db.commit()

    await db.refresh(student)

    return student


@app.delete(
    "/api/students/{student_id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    await db.delete(student)

    await db.commit()

    return


# ==============================
# Enrollment CRUD
# ==============================

@app.get(
    "/api/enrollments/",
    response_model=list[EnrollmentResponse],
    status_code=status.HTTP_200_OK,
    tags=["Enrollments"]
)
async def get_enrollments(
    skip: int = 0,
    limit: int = 10,
    db: AsyncSession = Depends(get_db),
):
    query = select(Enrollment).offset(skip).limit(limit)

    result = await db.execute(query)

    enrollments = result.scalars().all()

    return enrollments


@app.get(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Enrollments"]
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found",
        )

    return enrollment



@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    new_enrollment = Enrollment(
        student_id=enrollment.student_id,
        course_id=enrollment.course_id,
        grade=enrollment.grade,
    )

    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)

    result = await db.execute(
        select(Student).where(
            Student.id == enrollment.student_id
        )
    )

    student = result.scalar_one_or_none()

    if student:
        background_tasks.add_task(
            send_confirmation_email,
            student.email,
        )

    return new_enrollment
@app.put(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_200_OK,
    tags=["Enrollments"]
)
async def update_enrollment(
    enrollment_id: int,
    enrollment_data: EnrollmentUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found",
        )

    if enrollment_data.student_id is not None:
        enrollment.student_id = enrollment_data.student_id

    if enrollment_data.course_id is not None:
        enrollment.course_id = enrollment_data.course_id

    if enrollment_data.grade is not None:
        enrollment.grade = enrollment_data.grade

    await db.commit()

    await db.refresh(enrollment)

    return enrollment


@app.delete(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(
            Enrollment.id == enrollment_id
        )
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found",
        )

    await db.delete(enrollment)

    await db.commit()

    return



def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")